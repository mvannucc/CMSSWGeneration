from CRABClient.UserUtilities import config

## parameters 
nThreads = 4
datasetname = 'EWK_LLJJ_MLL_50_MJJ_120_TuneCP5_13TeV_madgraph_herwig7_dipole'
configlhe = '../LHEGEN/'+datasetname+'_cfg.py'
outputName = 'nanoAOD.root'
scriptExe = '../scripts/scriptExe_ewk_lljj_madgraph_herwig7_dipole.sh'
nEvents = 1500
nEventsTotal = 1500000

## config file
config = config()
## General settings
config.General.requestName = 'rgerosa_ewk_lljj_madgraph_herwig7_dipole'
config.General.transferOutputs = True
config.General.transferLogs = False
## PrivateMC type with a fake miniAOD step to circunvent crab requests (official data-tier for PrivateMC)
config.JobType.pluginName  = 'PrivateMC'
config.JobType.psetName    = configlhe
config.JobType.pyCfgParams = ['nThreads='+str(nThreads),'outputName='+outputName]
## To be executed on node with Arguments
config.JobType.scriptExe   = scriptExe
config.JobType.scriptArgs  = ['nEvents='+str(nEvents),'nThreads='+str(nThreads),'outputName='+outputName]
config.JobType.inputFiles  = ['../DIGI_RAW_premix_step_cfg.py','../HLT_step_cfg.py','../MINIAOD_step_cfg.py','../NANOAODv9_step_cfg.py','../RECO_step_cfg.py','../SIM_step_cfg.py','../pileup.py',configlhe]
## Output file to be collected
config.JobType.outputFiles = [outputName]
config.JobType.disableAutomaticOutputCollection = True
## Memory, cores, cmssw
config.JobType.allowUndistributedCMSSW = True
config.JobType.maxMemoryMB = 5500
config.JobType.numCores    = 4
## Data
config.Data.splitting   = 'EventBased'
config.Data.unitsPerJob = nEvents
config.Data.totalUnits  = nEventsTotal
config.Data.outLFNDirBase = '/store/user/rgerosa/PrivateMC/RunIISummer20UL18NanoAODv9/'
config.Data.publication   = True
config.Data.outputPrimaryDataset = datasetname
config.Data.outputDatasetTag = 'RunIISummer20UL18NanoAODv9_106X_upgrade2018_realistic_v11_NANOAODSIM'
## Site
config.Site.storageSite = 'T2_US_UCSD' 
