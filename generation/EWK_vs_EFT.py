import xml.etree.ElementTree as ET
import itertools
from matplotlib import pyplot as plt
from decimal import Decimal, getcontext
import numpy as np
import os

output_folder = "histograms_output"
os.makedirs(output_folder, exist_ok=True)

getcontext().prec = 50

CROSS_SECTIONS = {}
LUMINOSITY = 59.8  # Luminosity in fb^-1

lhe_file_paths = {'EFT': 'lhe/cmsgrid_final_EFT.lhe', 'SM': 'lhe/cmsgrid_final_SM.lhe'}

# Extract cross sections from the LHE files
for label, lhe_file_path in lhe_file_paths.items():
    with open(lhe_file_path, 'r') as lhe_file:
        in_init_block = False
        init_lines = []
        for line in lhe_file:
            if '<init>' in line:
                in_init_block = True
                continue
            if '</init>' in line:
                break
            if in_init_block:
                init_lines.append(line.strip())
        if len(init_lines) >= 2:
            cross_section_line = init_lines[1]
            cross_section = float(cross_section_line.split()[0])  # cross section [pb]
            CROSS_SECTIONS[label] = cross_section * 1000  # Convert to fb
        else:
            print(f"Warning: Could not find cross section in {lhe_file_path}")

electron_pids = [11, -11]  # e-, e+
muon_pids = [13, -13]      # mu-, mu+
jet_pids = [1, -1, 2, -2, 3, -3, 4, -4, 5, -5, 6, -6]

Z_MASS = Decimal('91.1876')  

data = {}
weight_sums = {label: {} for label in lhe_file_paths}  
filtered_event_counts = {label: 0 for label in lhe_file_paths}  
total_histogram_weights = {label: 0.0 for label in lhe_file_paths}
less_lep = {label: 0.0 for label in lhe_file_paths}

def get_invariant_mass_two(p1, p2):
    px = Decimal(p1.px) + Decimal(p2.px)
    py = Decimal(p1.py) + Decimal(p2.py)
    pz = Decimal(p1.pz) + Decimal(p2.pz)
    energy = Decimal(p1.e) + Decimal(p2.e)
    mass_squared = energy**2 - (px**2 + py**2 + pz**2)
    if mass_squared < 0:
        mass_squared = Decimal(0)
    return float(mass_squared.sqrt())

def get_particle_pt(particle):
    px = Decimal(particle.px)
    py = Decimal(particle.py)
    pt_squared = px**2 + py**2
    return float(pt_squared.sqrt())

def get_particle_eta(particle):
    px = Decimal(particle.px)
    py = Decimal(particle.py)
    pz = Decimal(particle.pz)
    p = (px**2 + py**2 + pz**2).sqrt()
    if p != abs(pz):
        eta = Decimal('0.5') * ((p + pz) / (p - pz)).ln()
    else:
        eta = Decimal('Infinity')
    return float(eta)

for label, lhe_file_path in lhe_file_paths.items():
    print(f"Processing file: {lhe_file_path}")

    context = ET.iterparse(lhe_file_path, events=('end',))
    event_number = 0

    for event, elem in context:
        if elem.tag == 'event':
            event_number += 1

            event_text = elem.text.strip()
            lines = event_text.strip().split('\n')

            event_header = lines[0].strip().split()
            num_particles = int(event_header[0])

            particles = []
            for line in lines[1:num_particles+1]:
                pdata = line.strip().split()
                particle = {
                    'id': int(pdata[0]),
                    'status': int(pdata[1]),
                    'px': float(pdata[6]),
                    'py': float(pdata[7]),
                    'pz': float(pdata[8]),
                    'e': float(pdata[9]),
                    'm': float(pdata[10]),
                }
                particles.append(particle)

            base_weight = 1.0

            # For EFT, apply additional weight from rwgt
            if label == 'EFT':
                rwgt_elem = elem.find('rwgt')
                rwgt_1_value = 1.0
                if rwgt_elem is not None:
                    for wgt in rwgt_elem.findall('wgt'):
                        if wgt.attrib['id'] == 'rwgt_1':
                            rwgt_1_value = float(wgt.text.strip())
                            break
                base_weight *= rwgt_1_value

            class Particle:
                def __init__(self, id, status, px, py, pz, e, m):
                    self.id = id
                    self.status = status
                    self.px = px
                    self.py = py
                    self.pz = pz
                    self.e = e
                    self.m = m

            event_particles = [Particle(**p) for p in particles]

            if label not in data:
                data[label] = {'default': {
                    'invMass_Z1': [],
                    'invMass_Z2': [],
                    'Lepton1_Pt': [], 'Lepton2_Pt': [], 'Lepton3_Pt': [], 'Lepton4_Pt': [],
                    'Lepton1_Eta': [], 'Lepton2_Eta': [], 'Lepton3_Eta': [], 'Lepton4_Eta': [],
                    'Jet1_Pt': [], 'Jet2_Pt': [],
                    'Jet_DeltaEta': []
                }}

            leptons, jets = [], []
            for particle in event_particles:
                if particle.status != 1:
                    continue
                pid = particle.id
                if pid in electron_pids + muon_pids:
                    leptons.append(particle)
                if pid in jet_pids:
                    jets.append(particle)

            if len(leptons) >= 4:
                # Order leptons and jets by pt
                leptons = sorted(leptons, key=get_particle_pt, reverse=True)
                jets = sorted(jets, key=get_particle_pt, reverse=True)

                for idx, lepton in enumerate(leptons[:4]):  
                    pt = get_particle_pt(lepton)
                    eta = get_particle_eta(lepton)
                    lepton_label_pt = f'Lepton{idx+1}_Pt'
                    lepton_label_eta = f'Lepton{idx+1}_Eta'
                    data[label]['default'][lepton_label_pt].append((pt, base_weight))
                    data[label]['default'][lepton_label_eta].append((eta, base_weight))

                if len(jets) >= 2:
                    jet1, jet2 = jets[0], jets[1]

                    jet1_pt = get_particle_pt(jet1)
                    jet2_pt = get_particle_pt(jet2)

                    jet1_eta = get_particle_eta(jet1)
                    jet2_eta = get_particle_eta(jet2)

                    delta_eta = abs(jet1_eta - jet2_eta)

                    data[label]['default']['Jet1_Pt'].append((jet1_pt, base_weight))
                    data[label]['default']['Jet2_Pt'].append((jet2_pt, base_weight))
                    data[label]['default']['Jet_DeltaEta'].append((delta_eta, base_weight))

                if len(leptons) >= 4:
                    total_histogram_weights[label] += base_weight
                    filtered_event_counts[label] += 1
                    sfos_pairs = []
                    for (i1, l1), (i2, l2) in itertools.combinations(enumerate(leptons), 2):
                        if l1.id + l2.id == 0 and abs(l1.id) == abs(l2.id):
                            sfos_pairs.append(((i1, l1), (i2, l2)))

                    if len(sfos_pairs) >= 2:
                        best_pair, min_mass_diff = None, Decimal('Infinity')
                        for (idx1, l1), (idx2, l2) in sfos_pairs:
                            mass = Decimal(get_invariant_mass_two(l1, l2))
                            mass_diff = abs(mass - Z_MASS)
                            if mass_diff < min_mass_diff:
                                min_mass_diff = mass_diff
                                best_pair = ((l1, l2), mass)
                                idx_Z1 = {idx1, idx2}

                        Z1_mass = float(best_pair[1])
                        remaining_indices = set(range(4)).difference(idx_Z1)
                        l3, l4 = [leptons[i] for i in remaining_indices]
                        Z2_mass = get_invariant_mass_two(l3, l4)

                        data[label]['default']['invMass_Z1'].append((Z1_mass, base_weight))
                        data[label]['default']['invMass_Z2'].append((Z2_mass, base_weight))
            else:
                less_lep[label] += 1

            total_weight = base_weight
            if 'default' not in weight_sums[label]:
                weight_sums[label]['default'] = 0
            weight_sums[label]['default'] += total_weight

            elem.clear()

            if event_number == 30000:
                break

    # Clean up
    del context

print("\nData Summary:")
for label, hist_data in data.items():
    print(f"\nLabel: {label}")
    print(f"  Cross section: {CROSS_SECTIONS[label]/1000} pb")
    print(f"  Total histogram weight: {total_histogram_weights[label]}")
    print(f"  Filtered event counts: {filtered_event_counts[label]}")
    print(f"  Events with less than 4 leptons: {less_lep[label]}")
    for wgt_id in hist_data:
        print(f"  Weight ID: {wgt_id}")
        for var, values in hist_data[wgt_id].items():
            print(f"    {var} - Entries: {len(values)}")

colors = {'EFT': 'blue', 'SM': 'orange'}

scaling_factors = {
    label: (CROSS_SECTIONS[label] * LUMINOSITY) / total_histogram_weights[label] 
    for label in lhe_file_paths
}

def plot_separated_histograms_with_error_lines(data, variables, x_labels, x_ranges, bins, colors, output_filename, scaling_factors):
    xsec_ratio = CROSS_SECTIONS['EFT'] / CROSS_SECTIONS['SM']

    num_vars = len(variables)
    fig, axes = plt.subplots(nrows=2, ncols=num_vars, figsize=(5 * num_vars, 8), gridspec_kw={'height_ratios': [3, 1]})
    plt.subplots_adjust(hspace=0.3, wspace=0.3)

    for i, (var, x_label, x_range, bin_num) in enumerate(zip(variables, x_labels, x_ranges, bins)):
        ax_hist = axes[0, i]
        ax_ratio = axes[1, i]  

        histograms = {}

        for label in data:
            histograms[label] = {}

            values, weights = zip(*data[label]['default'][var]) if data[label]['default'][var] else ([], [])
            if values:
                weights = np.array(weights)
                weights_squared = weights ** 2

                counts, bin_edges = np.histogram(values, bins=bin_num, range=x_range, weights=weights)
                sumw2, _ = np.histogram(values, bins=bin_num, range=x_range, weights=weights_squared)
                errors = np.sqrt(sumw2)

                scaling_factor = scaling_factors[label]
                counts *= scaling_factor
                errors *= scaling_factor

                histograms[label]['counts'] = counts
                histograms[label]['errors'] = errors
                histograms[label]['bin_edges'] = bin_edges

                ax_hist.bar(bin_edges[:-1], counts, width=np.diff(bin_edges), align='edge', label=label, color=colors[label], alpha=0.6, edgecolor='black', linewidth=1)

                ax_hist.errorbar(
                    (bin_edges[:-1] + bin_edges[1:]) / 2,
                    counts,
                    yerr=errors,
                    fmt='none',
                    ecolor=colors[label],
                    elinewidth=1.5,
                    capsize=3
                )
            else:
                print(f"Warning: No data to plot for {label}, {var}")

        if 'EFT' in histograms and 'SM' in histograms:
            counts_EFT = histograms['EFT']['counts']
            errors_EFT = histograms['EFT']['errors']
            counts_SM = histograms['SM']['counts']
            errors_SM = histograms['SM']['errors']
            bin_centers = (histograms['EFT']['bin_edges'][:-1] + histograms['EFT']['bin_edges'][1:]) / 2

            with np.errstate(divide='ignore', invalid='ignore'):
                ratio = counts_EFT / counts_SM
                ratio_uncertainty = ratio * np.sqrt(
                    (errors_EFT / counts_EFT) ** 2 + (errors_SM / counts_SM) ** 2
                )

            ratio[counts_SM == 0] = np.nan
            ratio_uncertainty[counts_SM == 0] = np.nan


            ax_ratio.errorbar(bin_centers, ratio, yerr=ratio_uncertainty, fmt='o', color='black', capsize=3)
            #ax_ratio.axhline(y=1, color='gray', linestyle='--', label='Ratio = 1')  # Reference line at ratio = 1
            ax_ratio.axhline(y=xsec_ratio, color='red', linestyle='-', label=f'Ratio = {xsec_ratio:.2f}')  
            ax_ratio.set_ylim(0, max(2 * xsec_ratio, 4))  # Adjust y-limit dynamically

        ax_hist.set_ylabel('Normalized Events')
        ax_hist.set_title(var)
        ax_hist.legend()
        ax_ratio.set_ylabel('Ratio EFT/SM')
        ax_ratio.set_xlabel(x_label)
        ax_ratio.grid(True)

    plt.tight_layout()
    plt.savefig(output_filename)
    plt.close(fig)

plot_separated_histograms_with_error_lines(
    data=data,
    variables=['Jet1_Pt', 'Jet2_Pt', 'Jet_DeltaEta'],
    x_labels=['$p_T (j_1)$ [GeV]', '$p_T (j_2)$ [GeV]', '$\Delta \eta_{jj}$'],
    x_ranges=[(0, 700), (0, 400), (0, 10)],
    bins=[10, 10, 10],
    colors=colors,
    output_filename=os.path.join(output_folder, 'jets.png'),
    scaling_factors=scaling_factors
)

plot_separated_histograms_with_error_lines(
    data=data,
    variables=['invMass_Z1', 'invMass_Z2'],
    x_labels=['$M_{Z_1}$ [GeV]', '$M_{Z_2}$ [GeV]'],
    x_ranges=[(70, 110), (60, 120)],
    bins=[6, 8],
    colors=colors,
    output_filename=os.path.join(output_folder, 'z_mass.png'),
    scaling_factors=scaling_factors
)

plot_separated_histograms_with_error_lines(
    data=data,
    variables=['Lepton1_Pt', 'Lepton2_Pt', 'Lepton3_Pt', 'Lepton4_Pt'],
    x_labels=['$p_T (\ell_1)$ [GeV]', '$p_T (\ell_2)$ [GeV]', '$p_T (\ell_3)$ [GeV]', '$p_T (\ell_4)$ [GeV]'],
    x_ranges=[(0, 600), (0, 400), (0, 300), (0, 200)],
    bins=[10, 10, 10, 10],
    colors=colors,
    output_filename=os.path.join(output_folder, 'lepton_pt.png'),
    scaling_factors=scaling_factors
)

plot_separated_histograms_with_error_lines(
    data=data,
    variables=['Lepton1_Eta', 'Lepton2_Eta', 'Lepton3_Eta', 'Lepton4_Eta'],
    x_labels=['$\eta (\ell_1)$', '$\eta (\ell_2)$', '$\eta (\ell_3)$', '$\eta (\ell_4)$'],
    x_ranges=[(-5, 5), (-5, 5), (-5, 5), (-5, 5)],
    bins=[10, 10, 10, 10],
    colors=colors,
    output_filename=os.path.join(output_folder, 'lepton_eta.png'),
    scaling_factors=scaling_factors
)
