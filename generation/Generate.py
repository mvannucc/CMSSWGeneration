import argparse 
import json
import sys
import os
import subprocess
from random import randint
import glob
import shutil
from textwrap import dedent
def insensitive_glob(pattern):
    def either(c):
        return '[%s%s]' % (c.lower(), c.upper()) if c.isalpha() else c
    return glob.glob(''.join(map(either, pattern)))

def create_CMSSW_tar(release, singularity):

    if singularity:
        script = """
        #!/bin/bash
        cd data/CMSSWs/;
        cat /etc/redhat-release
        source /cvmfs/cms.cern.ch/cmsset_default.sh
        scram p {}
        cd {}/src/
        eval `scramv1 runtime -sh`
        scram b
        cd ../../
        tar -zcf {}.tgz {}
        rm -rf {}
        """.format(release, release, release, release, release)
        nameTmpScript = "script_{}.sh".format(randint(100000,900000))
        with open(nameTmpScript, "w") as file:
            file.write(dedent(script))
        process = subprocess.Popen("chmod +x {}; cmssw-env --cmsos slc6 --command-to-run  $(echo $(pwd)/{}); rm {}".format(nameTmpScript,nameTmpScript,nameTmpScript), shell=True)
        process.wait()
        
    else:
        script  = "#!/bin/bash\n"
        # script += "export SCRAM_ARCH={} \n".format(scram)
        script += "source /cvmfs/cms.cern.ch/cmsset_default.sh\n"
        script += "cd data/CMSSWs\n"
        script += "scram project CMSSW {}\n".format(release)
        script += "cd {}/src\n".format(release)
        script += "eval `scramv1 runtime -sh`\n"
        if release =="CMSSW_10_2_22" or release =="CMSSW_10_2_24":
            script += "git cms-init\n"
            script += "git cms-merge-topic giorgiopizz:patch_10_2_22_nanoAOD_reweight\n"
            # Little fix because last commit of giorgio branch does not work in 10_2_22 
            # but does work in 10_2_24
            if release =="CMSSW_10_2_22":
               script += "git checkout 0c5417182b0\n" 
        if release == "CMSSW_10_6_26":
            script += "git cms-init\n"
            script += "git cms-merge-topic acmbulla:10_6_26_reweight_patch\n"
        #elif release == "CMSSW_10_2_6":
        #    print("--> Patching 10_2_6")
        #    script += "git cms-init\n"
        #    script += "git cms-merge-topic GiacomoBoldrini:patch_10_2_6_gridpack\n"
        script += "scram b\n"
        script += "cd ../..\n"
        script += "tar -zcf {}.tgz {}\n".format(release, release)
        script += "rm -rf {}\n".format(release)
        nameTmpScript = "script_{}.sh".format(randint(100000,900000))
        with open(nameTmpScript, "w") as file:
            file.write(script)
        process = subprocess.Popen("chmod +x {}; ./{}; rm {}".format(nameTmpScript,nameTmpScript,nameTmpScript), shell=True)
        process.wait()

def generate(name, year, gridpack, removeOldRoot, dipoleRecoil, events, jobs, doBatch, eos_out_path):
    with open("Steps.json") as file:
        Steps = json.load(file) 
    gridpack = os.path.expanduser(gridpack)
    if not os.path.isfile(gridpack):
        print("Gridpack path is not correct")
        return

    totalYears = Steps.keys()
    if year not in totalYears:
        print("Year not valid")
        print("Valid years are: {}".format(", ".join(totalYears)))
        return
  
    totalSteps = Steps[year]["steps"]

    cmssws = []
    singularities = []
    # scrams = []
    # print(Steps[year].keys())
    for k in totalSteps:
        cmssws.append(Steps[year][k]['release'])
        if "singularity" in Steps[year][k]:
            singularities.append(Steps[year][k]['singularity'])
        else:
            singularities.append(False)
    cmssws = list(set(cmssws))
    print("ppppppppppppppppppppppppppppppppp")
    print(cmssws)

    for i in range(len(cmssws)):
        cmssw = cmssws[i]
        singularity = singularities[i]
        if not os.path.isfile("data/CMSSWs/{}.tgz".format(cmssw)):
            print("Should create CMSSW tgz for release {}".format(cmssw))
            create_CMSSW_tar(cmssw, singularity)


    if os.path.isdir("output/"+name):
        print("Dir with name: {} already present, can't create directory if they exist in python2 (blame Giacomo)".format(name))
        return
    os.makedirs("output/{}/root".format(name))
    os.makedirs("output/{}/log".format(name))




    # if the gridpack is on eos then we can't give it as input instead we eos cp from the executable script

    if gridpack.startswith("/eos"): fileToTransfer = []
    else: fileToTransfer = [gridpack]

    inputsCfg = glob.glob("data/input_{}/*.py".format(year))
    inputsCfg = list(map(lambda k: os.path.abspath(k), inputsCfg))
    fileToTransfer.extend(inputsCfg)
    print(insensitive_glob("data/input_{}/*{}*.py".format(year, totalSteps[-1])))
    outputFile = insensitive_glob("data/input_{}/*{}*.py".format(year, totalSteps[-1]))[0].split("/")[-1].split("_1_")[0]
    for cmssw in cmssws:
        fileToTransfer.append(os.path.abspath(glob.glob("data/CMSSWs/{}.tgz".format(cmssw))[0]))
     
    if doBatch == 1:
        jdl = "Universe = vanilla \n"
        jdl += "Executable = wrapper.sh\n"
        if eos_out_path != "":
           jdl += "outfilename = {}/$(proc)_$(ClusterId)_$(ProcId).root\n".format(eos_out_path)
           jdl += "arguments = $(Step) $(outfilename)\n"
        else: 
           jdl += "arguments = $(Step)\n"
        jdl += "use_x509userproxy = true\n"
        jdl += " +JobFlavour = \"nextweek\"\n"
        # jdl += "request_cpus = 8 \n"
        # jdl += "request_disk = 35000000 \n" 
        jdl += "should_transfer_files = YES\n"
        jdl += "Error = log/$(proc).err_$(Step)\n"
        jdl += "Output = log/$(proc).out_$(Step)\n"
        jdl += "Log = log/$(proc).log_$(Step)\n"
        jdl += "transfer_input_files = {}\n".format(", ".join(fileToTransfer))
        if eos_out_path == "":
           jdl += 'transfer_output_remaps = "{}.root = {}/$(proc)_$(Cluster)_$(Step).root"\n'.format(outputFile, os.path.abspath("output/{}/root".format(name)))
           jdl += "when_to_transfer_output = ON_EXIT\n"
        jdl += "Queue {} proc in ({})\n".format(jobs, name)

        with open("output/{}/submit.jdl".format(name), "w") as file:
            file.write(jdl)
    else:
        workdir = "output/{}/workdir".format(name)
        os.makedirs(workdir)
        jdl = "#!/bin/bash\n"
        for f in fileToTransfer:
            jdl += "cp {} workdir \n".format(f)

        jdl += "cp wrapper.sh workdir\n"
        jdl += "cd workdir; ./wrapper.sh\n"

        with open("output/{}/run.sh".format(name), "w") as file:
            file.write(jdl)
        process = subprocess.Popen("chmod +x output/{}/run.sh".format(name), shell=True)

    wrapper =  "#!/bin/bash\n"
    wrapper += "export EOS_MGM_URL=root://eosuser.cern.ch\n"
    wrapper += 'echo "Starting job on " `date` #Date/time of start of job\n'
    wrapper += 'echo "Running on: `uname -a`" #Condor job is running on this node\n'
    wrapper += 'echo "System software: `cat /etc/redhat-release`" #Operating System on that node\n'
    wrapper += 'source /cvmfs/cms.cern.ch/cmsset_default.sh\n'
    
    if gridpack.startswith("/eos"):

       wrapper += 'eos cp {} .\n'.format(gridpack)
    
    openCMSSW = ""
    files = glob.glob("data/input_{}/*.py".format(year))
    files = list(map(lambda k: k.split("/")[-1], files))
    totalStepsCorrect = [x for x in totalSteps]
    stepFiles = []
    for step in totalSteps:
        a = sorted(list(filter(lambda k: step.lower() in k.lower(), files)))
        stepFiles.extend(a)
        if len(a)>1 and totalSteps.count(step)==1:
            for i in range(1, len(a)):
                totalStepsCorrect.insert(totalStepsCorrect.index(step),step)       
    print(stepFiles, totalStepsCorrect)
    print(list(zip(totalStepsCorrect, stepFiles)))        
 
    # premix has 2 steps tipically
    if "premix" in totalSteps: 
       totalSteps.insert(1, "premix")
    filesToRemove = [gridpack.split("/")[-1]]
    for k, file in zip(totalStepsCorrect, stepFiles):
        wrapper += "#Working on {} step\n\n".format(k)

        if k == 'lhe':
            wrapper += "sed -i 's#^.*tarball.tar.xz.*$#    args = cms.vstring(\"../{}\"),#' -i {}\n".format(gridpack.split("/")[-1], file)
            # input = cms.untracked.int32(274)
            wrapper += "sed -i 's#^.*input[^=]*=[^=]*cms.untracked.int32.*$#    input = cms.untracked.int32({})#g' -i {}\n".format(events, file)
            wrapper += 'sed -i "s/^.*nEvents = .*$/    nEvents = cms.untracked.uint32({}),/g" -i {}\n'.format(events, file)
            wrapper += 'if grep -qF "process.RandomNumberGeneratorService.externalLHEProducer.initialSeed" {}; then \n'.format(file)
            wrapper += 'sed -i "s/^process.RandomNumberGeneratorService.externalLHEProducer.initialSeed.*$/process.RandomNumberGeneratorService.externalLHEProducer.initialSeed=int($(($1+1)))/g" {} \n'.format(file)
            wrapper += 'else \n'
            wrapper += 'sed -i "/^# Customisation from command line/a process.RandomNumberGeneratorService.externalLHEProducer.initialSeed=int($(($1+1)))" {} \n'.format(file)
            wrapper += 'fi \n'

            if dipoleRecoil:
                wrapper += "if ! grep -qF 'SpaceShower:dipoleRecoil = on' {}; then \n".format(file)
                wrapper += "sed -i '/^.*pythia8CP5Settings[^=]*=.*/i \ \ \ \ \ \ \ \ processParameters = cms.vstring(\"SpaceShower:dipoleRecoil = on\"),' -i {}\n".format(file)
                wrapper += 'fi \n'
          
        if Steps[year][k]['release'] != openCMSSW:
            if openCMSSW != "":
                wrapper += "rm -rf {}\n".format(openCMSSW)
            wrapper += 'echo "Opening {}"\n'.format(Steps[year][k]['release'])
            wrapper += 'tar -xzvf {}.tgz\n'.format(Steps[year][k]['release'])
            # wrapper += 'rm {}.tgz\n'.format(Steps[year][k]['release'])
            wrapper += 'cd {}/src/\n'.format(Steps[year][k]['release'])
            # wrapper += 'export SCRAM_ARCH={}\n'.format(Steps[year][k]['SCRAM_ARCH'])
            wrapper += 'scramv1 b ProjectRename # this handles linking the already compiled code - do NOT recompile\n'
            wrapper += 'eval `scramv1 runtime -sh` # cmsenv is an alias not on the workers\n'
            wrapper += 'echo $CMSSW_BASE "is the CMSSW we have on the local worker node"\n'
            wrapper += 'cd ../../\n'
            openCMSSW = Steps[year][k]['release']
        wrapper += "date\n"
        wrapper += "cmsRun {}\n".format(file)
        if removeOldRoot:
            if k == "lhe" and totalSteps[-1] != "lhe":
                filesToRemove.append(file.split("_")[0]+".root")
                filesToRemove.append(file.split("_")[0]+"_inLHE.root")
              
            elif k == "premix" and "_1_" not in file and totalSteps[-1] != "premix":
                filesToRemove.append(file.split("_")[0]+".root")
                filesToRemove.append(file.split("_")[0]+"_0.root")
            elif k == "miniAOD" and totalSteps[-1] != "miniAOD":
                filesToRemove.append(file.split("_")[0]+".root")
        wrapper += "\n\n"
    wrapper += "rm CMSSW_*tgz\n"
    wrapper += "rm {}\n".format(" ".join(filesToRemove))
    wrapper += "rm -rf {} *py\n".format(openCMSSW)

    if eos_out_path != "":
       wrapper += "eos cp SMP-RunIIAutumn18NanoAODv7-00058.root $2\n".format(eos_out_path) 
 
    wrapper += "date\n"

    with open("output/{}/wrapper.sh".format(name), "w") as file:
        file.write(wrapper)



    process = subprocess.Popen("chmod +x output/{}/wrapper.sh".format(name), shell=True)
    process.wait()
    if (doBatch==1):
        process = subprocess.Popen('cd output/{}; condor_submit submit.jdl; cd -'.format(name), shell=True)
        process.wait()

def helperJsonParse(Samples, sample):
    params = []
    paramsD = {
        "removeOldRoot": True,
        "dipoleRecoil": True,
        "events": 2500,
        "jobs": 400,
        "doBatch": 0,
        "eosPath": "",
    }
    if not sample in Samples.keys():
        print("Sample {} not present in Samples.json".format(sample))
        return True, []
    required_params = ["year", "gridpack"]
    for p in required_params:
        if p not in Samples[sample].keys() or Samples[sample][p] =="":
            print("{} not present in Samples.json dict for {}".format(p, sample))
            return True, []
        paramsD[p] = Samples[sample][p]
  
    optional_params = ["removeOldRoot", "dipoleRecoil", "events", "jobs", "doBatch", "eosPath"]
    for p in optional_params:
        if p in Samples[sample].keys():
            paramsD[p] = Samples[sample][p]

    for p in required_params + optional_params:
        params.append(paramsD[p])
    return False, params




if __name__ == "__main__":
    argsT = sys.argv[1:]
    #by default using Samples.json, might specify which samples of Samples to use with -s SAMPLE_NAME1 SAMPLE_NAME2 ... 
    if len(argsT)==0 or argsT[0]=='-s':
        # use Samples.json
        print("Using Samples.json")
        with open("Samples.json") as file:
            Samples = json.load(file)

        if len(argsT)>1:
            samples_to_generate = argsT[1:]
        elif len(argsT)==0:
            samples_to_generate = list(filter(lambda k: not os.path.isdir("output/"+k), Samples.keys()))
        else:
            print("Invalid syntax, use -s SAMPLE_NAME1 SAMPLE_NAME2 (specify at least one sample)")
            sys.exit(-1)
        print("Generating samples: {}".format(", ".join(samples_to_generate)))
        for sample in samples_to_generate:
            print("\n\nNow working on sample {}\n\n".format(sample))
            skip, params = helperJsonParse(Samples, sample)
            if skip:
                continue
            print("Generating with params: {}".format([sample]+params))
            generate(*([sample]+params))


    else:
        parser = argparse.ArgumentParser()
        parser.add_argument("-n","--name", help="Name for the generation, will be used for creating directories" , required=True)
        parser.add_argument("-y","--year", help="Year" , required=True)
        parser.add_argument("-gp","--gridpack", help="Path to gridpack", required=True)
        parser.add_argument("-r","--removeOldRoot", help="Option to remove intermediate root files (inLHE, miniAOD...), default = True", default=True)
        parser.add_argument("-dr","--dipoleRecoil", help="Whether to use dipole recoil in pythia, default = True", default=True)
        parser.add_argument("-e","--events", help="Number of events per file", default=2500)
        parser.add_argument("-j","--jobs", help="Number of jobs", default=400)
        parser.add_argument("-b","--doBatch", help="Wheter to submit or not (--doBatch=1)", default=0)
        args = parser.parse_args(argsT)
        generate(args.name, args.year, args.gridpack, args.removeOldRoot, args.dipoleRecoil, args.events, args.jobs, args.doBatch)
