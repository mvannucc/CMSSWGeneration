from CRABClient.UserUtilities import config, getUsernameFromSiteDB
config = config()

config.General.requestName = 'VBS_SSWW_TT_NANOAODSIM'
config.General.workArea = 'crab_projects'
config.General.transferOutputs = True
config.General.transferLogs = False

config.JobType.pluginName = 'Analysis'
config.JobType.psetName = 'SMP-RunIIFall17NanoAODv5-00023_1_cfg.py'
config.JobType.numCores = 2
#config.JobType.maxMemoryMB = 6000

config.Data.inputDataset = '/Bulk/jixiao-VBS_SSWW_LT_MINIAODSIM-5f646ecd4e1c7a39ab0ed099ff55ceb9/USER'
config.Data.inputDBS = 'phys03'
config.Data.splitting = 'FileBased'
config.Data.unitsPerJob = 1
config.Data.outLFNDirBase = '/store/user/%s/polarization_2017' % (getUsernameFromSiteDB())
config.Data.publication = True
config.Data.outputDatasetTag = 'VBS_SSWW_TT_NANOAODSIM'

config.Site.storageSite = 'T2_CN_Beijing'
