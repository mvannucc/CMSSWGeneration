import pylhe
import itertools
from matplotlib import pyplot as plt
from decimal import Decimal, getcontext
import numpy as np
import os

output_folder = "histograms_output"
os.makedirs(output_folder, exist_ok=True)

# Set precision for Decimal calculations
getcontext().prec = 50

# Constants for normalization
CROSS_SECTIONS = {'EFT': 0.8325, 'EWK': 0.427}  # Cross sections in fb
LUMINOSITY = 59.8  # Luminosity in fb^-1

# LHE file paths
lhe_file_paths = {'EFT': 'lhe/cmsgrid_final_EFT.lhe', 'EWK': 'lhe/cmsgrid_final_EWK.lhe'}

# PDG IDs for electrons, muons, taus, neutrinos, and photons
electron_pids = [11, -11]  # e-, e+
muon_pids = [13, -13]      # mu-, mu+
tau_pids = [15, -15]       # tau-, tau+
exclude_pids = electron_pids + muon_pids + tau_pids + [12, -12, 14, -14, 16, -16, 22]  # Exclude neutrinos and photons

Z_MASS = Decimal('91.1876')  # Known Z boson mass in GeV

data = {}
weight_sums = {label: {} for label in lhe_file_paths}  # To store total weights
filtered_event_counts = {label: 0 for label in lhe_file_paths}  # Count valid events only
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
    events = pylhe.read_lhe(lhe_file_path)

    event_number = 0
    with open(lhe_file_path, 'r') as lhe_file:
        for event in events:
            event_number += 1

            # Progress print every 10,000 events
            if event_number % 10000 == 0:
                print(f"Processed {event_number} events for {label}")
            
            # 17k max events
            if event_number == 17000:
                break

            
            has_electron = False
            has_muon = False
            tau_count = 0

            for particle in event.particles:
                if particle.status == 1:
                    if particle.id in electron_pids:
                        has_electron = True
                    elif particle.id in muon_pids:
                        has_muon = True
                    elif particle.id in tau_pids:
                        tau_count += 1

            # Skip event if it has two taus from a Z boson for the EWK sample
            # if label == 'EWK' and tau_count >= 2:
            #     continue

            base_weight = 1. 

            # Only for EFT, apply additional weight from <rwgt id='rwgt_1'>
            if label == 'EFT':
                rwgt_1_value = 1.0
                in_rwgt_block = False

                for line in lhe_file:
                    if "<rwgt>" in line:
                        in_rwgt_block = True
                    elif "</rwgt>" in line:
                        in_rwgt_block = False
                        break
                    elif in_rwgt_block and "id='rwgt_1'" in line:
                        rwgt_1_value = float(line.split(">")[1].split("<")[0].strip())
                        break

                base_weight *= rwgt_1_value

            event_weights = {'default': base_weight}

            # Initialize data structure if not already done
            if label not in data:
                data[label] = {wgt_id: {
                    'invMass_Z1': [],
                    'invMass_Z2': [],
                    'Lepton1_Pt': [], 'Lepton2_Pt': [], 'Lepton3_Pt': [], 'Lepton4_Pt': [],
                    'Lepton1_Eta': [], 'Lepton2_Eta': [], 'Lepton3_Eta': [], 'Lepton4_Eta': [],
                    'Jet1_Pt': [], 'Jet2_Pt': [],
                    'Jet_DeltaEta': []
                } for wgt_id in event_weights}

            # Process particles for analysis
            leptons, jets = [], []
            for particle in event.particles:
                if particle.status != 1:
                    continue
                pid = particle.id
                if pid in electron_pids + muon_pids:
                    leptons.append(particle)
                elif pid not in exclude_pids:
                    jets.append(particle)

            # Only proceed with events containing at least 4 leptons
            if len(leptons) >= 4:
                # Order leptons and jets by pt
                leptons = sorted(leptons, key=get_particle_pt, reverse=True)
                jets = sorted(jets, key=get_particle_pt, reverse=True)

                # Store leptons' pt and eta separately
                for idx, lepton in enumerate(leptons[:4]):  # Consider up to 4 leptons
                    pt = get_particle_pt(lepton)
                    eta = get_particle_eta(lepton)
                    lepton_label_pt = f'Lepton{idx+1}_Pt'
                    lepton_label_eta = f'Lepton{idx+1}_Eta'
                    for wgt_id in event_weights:
                        data[label][wgt_id][lepton_label_pt].append((pt, event_weights[wgt_id]))
                        data[label][wgt_id][lepton_label_eta].append((eta, event_weights[wgt_id]))

                # Process jets and store the two jets with highest pt separately
                if len(jets) >= 2:
                    jet1, jet2 = jets[0], jets[1]

                    jet1_pt = get_particle_pt(jet1)
                    jet2_pt = get_particle_pt(jet2)

                    jet1_eta = get_particle_eta(jet1)
                    jet2_eta = get_particle_eta(jet2)

                    delta_eta = abs(jet1_eta - jet2_eta)

                    for wgt_id in event_weights:
                        data[label][wgt_id]['Jet1_Pt'].append((jet1_pt, event_weights[wgt_id]))
                        data[label][wgt_id]['Jet2_Pt'].append((jet2_pt, event_weights[wgt_id]))
                        data[label][wgt_id]['Jet_DeltaEta'].append((delta_eta, event_weights[wgt_id]))
                

                # Calculate invariant masses if there are exactly 4 leptons
                if len(leptons) >= 4:
                    total_histogram_weights[label] += event_weights['default']
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

                        for wgt_id in event_weights:
                            data[label][wgt_id]['invMass_Z1'].append((Z1_mass, event_weights[wgt_id]))
                            data[label][wgt_id]['invMass_Z2'].append((Z2_mass, event_weights[wgt_id]))
            else : 
                less_lep[label] += 1    

            for wgt_id, weight in event_weights.items():
                if wgt_id not in weight_sums[label]:
                    weight_sums[label][wgt_id] = 0
                weight_sums[label][wgt_id] += weight

# Data Summary
print("\nData Summary:")
for label, hist_data in data.items():
    print(f"\nLabel: {label}")
    print(total_histogram_weights[label])
    print(filtered_event_counts[label])
    print(less_lep[label])
    for wgt_id in hist_data:
        print(f"  Weight ID: {wgt_id}")
        for var, values in hist_data[wgt_id].items():
            print(f"    {var} - Entries: {len(values)}")


colors = {'EFT': 'blue', 'EWK': 'orange'}

# Compute scaling factors
scaling_factors = {
    label: (CROSS_SECTIONS[label] * LUMINOSITY) / filtered_event_counts[label]
    for label in lhe_file_paths
}

def plot_separated_histograms_with_error_lines(data, variables, x_labels, x_ranges, colors, output_filename, scaling_factors):
    # Create a figure with a grid layout
    num_vars = len(variables)
    fig, axes = plt.subplots(nrows=2, ncols=num_vars, figsize=(5 * num_vars, 8), gridspec_kw={'height_ratios': [3, 1]})
    plt.subplots_adjust(hspace=0.3, wspace=0.3)

    for i, (var, x_label, x_range) in enumerate(zip(variables, x_labels, x_ranges)):
        
        ax_hist = axes[0, i]
        ax_ratio = axes[1, i]  # Bottom axis for the ratio plot

        histograms = {}

        # Process each label (EFT and EWK)
        for label in data:
            histograms[label] = {}

            values, weights = zip(*data[label]['default'][var]) if data[label]['default'][var] else ([], [])
            if values:
                weights = np.array(weights)
                weights_squared = weights ** 2

                counts, bin_edges = np.histogram(values, bins=20, range=x_range, weights=weights)  # Fixed 30 bins
                sumw2, _ = np.histogram(values, bins=20, range=x_range, weights=weights_squared)
                errors = np.sqrt(sumw2)

                # Apply normalization (scaling factor)
                scaling_factor = scaling_factors[label]
                counts *= scaling_factor
                errors *= scaling_factor

                histograms[label]['counts'] = counts
                histograms[label]['errors'] = errors
                histograms[label]['bin_edges'] = bin_edges

                # Plot filled rectangular histogram bars in the top axes
                ax_hist.bar(bin_edges[:-1], counts, width=np.diff(bin_edges), align='edge', label=label, color=colors[label], alpha=0.6, edgecolor='black', linewidth=1)

                
                ax_hist.errorbar(
                    (bin_edges[:-1] + bin_edges[1:]) / 2,  # X positions at bin centers
                    counts,                                # Y positions
                    yerr=errors,                           # Errors
                    fmt='none',                            # No marker
                    ecolor=colors[label],                  # Error bar color matches histogram
                    elinewidth=1.5,                        # Line thickness for error bars
                    capsize=3                              # Optional: small caps on error bars
                )
            else:
                print(f"Warning: No data to plot for {label}, {var}")

        # Compute ratio EFT / EWK 
        if 'EFT' in histograms and 'EWK' in histograms:
            counts_EFT = histograms['EFT']['counts']
            errors_EFT = histograms['EFT']['errors']
            counts_EWK = histograms['EWK']['counts']
            errors_EWK = histograms['EWK']['errors']
            bin_centers = (histograms['EFT']['bin_edges'][:-1] + histograms['EFT']['bin_edges'][1:]) / 2

            # Avoid division by zero
            with np.errstate(divide='ignore', invalid='ignore'):
                ratio = counts_EFT / counts_EWK
                ratio_uncertainty = ratio * np.sqrt(
                    (errors_EFT / counts_EFT) ** 2 + (errors_EWK / counts_EWK) ** 2
                )

            ratio[counts_EWK == 0] = np.nan
            ratio_uncertainty[counts_EWK == 0] = np.nan

            
            ax_ratio.errorbar(bin_centers, ratio, yerr=ratio_uncertainty, fmt='o', color='black', capsize=3)
            ax_ratio.axhline(y=1, color='gray', linestyle='--')  # Reference line at ratio = 1
            ax_ratio.set_ylim(0, 2)  # Adjust as needed

        
        ax_hist.set_ylabel('Normalized Events')
        ax_hist.set_title(var)
        ax_hist.legend()
        ax_ratio.set_ylabel('Ratio EFT/EWK')
        ax_ratio.set_xlabel(x_label)
        ax_ratio.grid(True)

    # Save the entire figure as one image file
    plt.tight_layout()
    plt.savefig(output_filename)
    plt.close(fig)


plot_separated_histograms_with_error_lines(
    data=data,
    variables=['Jet1_Pt', 'Jet2_Pt', 'Jet_DeltaEta'],
    x_labels=['Jet1 pT (GeV)', 'Jet2 pT (GeV)', 'Delta Eta between leading jets'],
    x_ranges=[(0, 300), (0, 300), (0, 10)],
    colors=colors,
    output_filename=os.path.join(output_folder, 'jets_histograms_with_error_lines.png'),
    scaling_factors=scaling_factors  # Include scaling_factors
)

plot_separated_histograms_with_error_lines(
    data=data,
    variables=['invMass_Z1', 'invMass_Z2'],
    x_labels=['Invariant Mass of Z1 (GeV)', 'Invariant Mass of Z2 (GeV)'],
    x_ranges=[(60, 120), (60, 120)],
    colors=colors,
    output_filename=os.path.join(output_folder, 'z_mass_histograms_with_error_lines.png'),
    scaling_factors=scaling_factors  
)

plot_separated_histograms_with_error_lines(
    data=data,
    variables=['Lepton1_Pt', 'Lepton2_Pt', 'Lepton3_Pt', 'Lepton4_Pt'],
    x_labels=['Lepton1 pT (GeV)', 'Lepton2 pT (GeV)', 'Lepton3 pT (GeV)', 'Lepton4 pT (GeV)'],
    x_ranges=[(0, 300), (0, 300), (0, 300), (0, 300)],
    colors=colors,
    output_filename=os.path.join(output_folder, 'lepton_pt_histograms_with_error_lines.png'),
    scaling_factors=scaling_factors  
)

plot_separated_histograms_with_error_lines(
    data=data,
    variables=['Lepton1_Eta', 'Lepton2_Eta', 'Lepton3_Eta', 'Lepton4_Eta'],
    x_labels=['Lepton1 Eta', 'Lepton2 Eta', 'Lepton3 Eta', 'Lepton4 Eta'],
    x_ranges=[(-5, 5), (-5, 5), (-5, 5), (-5, 5)],
    colors=colors,
    output_filename=os.path.join(output_folder, 'lepton_eta_histograms_with_error_lines.png'),
    scaling_factors=scaling_factors  
)

