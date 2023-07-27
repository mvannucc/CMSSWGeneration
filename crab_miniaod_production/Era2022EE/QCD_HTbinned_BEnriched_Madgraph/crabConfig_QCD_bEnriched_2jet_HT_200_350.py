from CRABClient.UserUtilities import config

config = config()

## General settings
config.General.requestName = 'rgerosa_QCD_bEnriched_2jet_HT_200_350'
config.General.transferOutputs = True
config.General.transferLogs = False
## PrivateMC type with a fake miniAOD step to circunvent crab requests (official data-tier for PrivateMC)
config.JobType.pluginName  = 'PrivateMC'
config.JobType.psetName    = 'miniaod_step_fake.py'
config.JobType.pyCfgParams = ['nThreads=4','outputName=miniaodStep.root']
## To be executed on node with Arguments
config.JobType.scriptExe   = 'scriptExe.sh'
config.JobType.scriptArgs  = ['nEvents=1500','nThreads=4','outputName=miniaodStep.root','gridpack=./QCD_bEnriched_2jet_HT_200_350_slc7_amd64_gcc10_CMSSW_12_4_8_tarball.tar.xz']
config.JobType.inputFiles  = ['scriptExe.sh','gen_sim_step.py','digi_raw_step_hlt.py','reco_step.py','miniaod_step.py','../pileup.py','/eos/cms/store/user/rgerosa/QCD_HTbinned_BEnriched_gridpacks/QCD_bEnriched_2jet_HT_200_350_slc7_amd64_gcc10_CMSSW_12_4_8_tarball.tar.xz']
## Output file to be collected
config.JobType.outputFiles = ["miniaodStep.root"]
config.JobType.disableAutomaticOutputCollection = True
## Memory, cores, cmssw
config.JobType.allowUndistributedCMSSW = True
config.JobType.maxMemoryMB = 5500
config.JobType.numCores    = 4
## Data
config.Data.splitting   = 'EventBased'
config.Data.unitsPerJob = 1500
config.Data.totalUnits  = 500000
config.Data.outLFNDirBase = '/store/user/rgerosa/PrivateMC/Run3Summer22EEMiniAODv3/'
config.Data.publication   = True
config.Data.outputPrimaryDataset = 'QCD_bEnriched_2jet_HT_200_350_TuneCP5_madgraph-pythia8_13p6TeV'
config.Data.outputDatasetTag = 'Run3Summer22EEMiniAODv3_124X_mcRun3_2022_realistic_postEE_v1-MINIAODSIM'
## Site
config.Site.storageSite = 'T2_US_UCSD' 
