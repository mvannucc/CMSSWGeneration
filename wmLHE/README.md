Dim6 operators
====

Some instructions here: 

    https://github.com/UniMiBAnalyses/D6EFTStudies
    
2017 production
====

Namely:

    cmsrel CMSSW_9_3_6
    
    cd CMSSW_9_3_6/src/
    
    cmsenv
    
    
    
    REQUEST=HIG-RunIIFall17wmLHEGS-01920
    wget --quiet -O request_fragment_check.py https://raw.githubusercontent.com/cms-sw/genproductions/master/bin/utils/request_fragment_check.py
    python request_fragment_check.py --bypass_status --prepid $REQUEST

    
The configuration file is created:

    HIG-RunIIFall17wmLHEGS-01920
    
    
Setup:

    export SCRAM_ARCH=slc6_amd64_gcc630
    source /cvmfs/cms.cern.ch/cmsset_default.sh


Here you get the actual configuration:

    curl -s --insecure https://cms-pdmv.cern.ch/mcm/public/restapi/requests/get_fragment/HIG-RunIIFall17wmLHEGS-01920 --retry 2 --create-dirs -o Configuration/GenProduction/python/HIG-RunIIFall17wmLHEGS-01920-fragment.py 

    scramv1 b
    
    
Now create:
    
    seed=$(($(date +%s) % 100 + 1))
    cmsDriver.py Configuration/GenProduction/python/HIG-RunIIFall17wmLHEGS-01920-fragment.py --fileout file:HIG-RunIIFall17wmLHEGS-01920.root --mc --eventcontent RAWSIM,LHE --datatier GEN-SIM,LHE --conditions 93X_mc2017_realistic_v3 --beamspot Realistic25ns13TeVEarly2017Collision --step LHE,GEN,SIM --geometry DB:Extended --era Run2_2017 --python_filename HIG-RunIIFall17wmLHEGS-01920_1_cfg.py --no_exec --customise Configuration/DataProcessing/Utils.addMonitoring --customise_commands process.source.numberEventsInLuminosityBlock="cms.untracked.uint32(100)"\\nprocess.RandomNumberGeneratorService.externalLHEProducer.initialSeed="int(${seed})" -n 145  

    cmsRun HIG-RunIIFall17wmLHEGS-01920_1_cfg.py
    
Now step 1 and 2, PreMix

    cmsrel CMSSW_9_4_7
    
    cd CMSSW_9_4_7/src/
    
    cmsenv

    voms-proxy-init -voms cms -rfc
    
    You need the grid certificate to get access to the premixed sample
    
    cmsDriver.py step1 --fileout file:HIG-RunIIFall17DRPremix-02533_step1.root  --pileup_input "dbs:/Neutrino_E-10_gun/RunIISummer17PrePremix-MCv2_correctPU_94X_mc2017_realistic_v9-v1/GEN-SIM-DIGI-RAW" --mc --eventcontent PREMIXRAW --datatier GEN-SIM-RAW --conditions 94X_mc2017_realistic_v11 --step DIGIPREMIX_S2,DATAMIX,L1,DIGI2RAW,HLT:2e34v40 --nThreads 8 --datamix PreMix --era Run2_2017 --python_filename HIG-RunIIFall17DRPremix-02533_1_cfg.py --no_exec --customise Configuration/DataProcessing/Utils.addMonitoring -n 1751 

    
    PS: it takes some time to run the previous job to create the configuration file ...
    
    cmsRun HIG-RunIIFall17DRPremix-02533_1_cfg.py 



    cmsDriver.py step2 --filein file:HIG-RunIIFall17DRPremix-02533_step1.root --fileout file:HIG-RunIIFall17DRPremix-02533.root --mc --eventcontent AODSIM --runUnscheduled --datatier AODSIM --conditions 94X_mc2017_realistic_v11 --step RAW2DIGI,RECO,RECOSIM,EI --nThreads 8 --era Run2_2017 --python_filename HIG-RunIIFall17DRPremix-02533_2_cfg.py --no_exec --customise Configuration/DataProcessing/Utils.addMonitoring -n 1751 
    
    cmsDriver.py step2 --filein file:HIG-RunIIFall17DRPremix-02533_step1.root --fileout file:HIG-RunIIFall17DRPremix-02533.root --mc --eventcontent AODSIM --runUnscheduled --datatier AODSIM --conditions 94X_mc2017_realistic_v11 --step RAW2DIGI,RECO --nThreads 8 --era Run2_2017 --python_filename HIG-RunIIFall17DRPremix-02533_2_cfg.py --no_exec --customise Configuration/DataProcessing/Utils.addMonitoring -n 1751 
    
    cmsRun HIG-RunIIFall17DRPremix-02533_2_cfg.py 
    
    
Now miniAOD

    cmsDriver.py step1 --filein "dbs:/GluGluHToWWTo2L2Nu_M125_13TeV_powheg2_JHUGenV714_pythia8/RunIIFall17DRPremix-PU2017_94X_mc2017_realistic_v11-v1/AODSIM" --fileout file:HIG-RunIIFall17MiniAODv2-02464.root --mc --eventcontent MINIAODSIM --runUnscheduled --datatier MINIAODSIM --conditions 94X_mc2017_realistic_v14 --step PAT --nThreads 4 --scenario pp --era Run2_2017,run2_miniAOD_94XFall17 --python_filename HIG-RunIIFall17MiniAODv2-02464_1_cfg.py --no_exec --customise Configuration/DataProcessing/Utils.addMonitoring -n 4800 
    
    cmsRun  HIG-RunIIFall17MiniAODv2-02464_1_cfg.py 
    
    
Now nanoAOD

    cmsrel CMSSW_10_2_15
    
    cd CMSSW_10_2_15/src/
    
    cmsenv


    cmsDriver.py step1 --filein "dbs:/GluGluHToWWTo2L2Nu_M125_13TeV_powheg2_JHUGenV714_pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM" --fileout file:HIG-RunIIFall17NanoAODv5-00331.root --mc --eventcontent NANOEDMAODSIM --datatier NANOAODSIM --conditions 102X_mc2017_realistic_v7 --step NANO --nThreads 2 --era Run2_2017,run2_nanoAOD_94XMiniAODv2 --python_filename HIG-RunIIFall17NanoAODv5-00331_1_cfg.py --no_exec --customise Configuration/DataProcessing/Utils.addMonitoring -n 10000

    cmsRun  HIG-RunIIFall17NanoAODv5-00331_1_cfg.py


    
    
    
    

LHE gridpacks
====

The configuration should be similar to the one defined here:

    args = cms.vstring('/cvmfs/cms.cern.ch/phys_generator/gridpacks/2017/13TeV/powheg/V2/gg_H_quark-mass-effects_gghWW2l2nu125/v1/gg_H_quark-mass-effects_slc6_amd64_gcc630_CMSSW_9_3_6_patch2_gghWW2l2nu125.tgz'),
    