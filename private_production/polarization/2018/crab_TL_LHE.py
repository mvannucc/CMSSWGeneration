from CRABClient.UserUtilities import config, getUsernameFromSiteDB
config = config()

config.General.requestName = 'VBS_SSWW_TL_LHE'
config.General.workArea = 'crab_projects'
config.General.transferOutputs = True
config.General.transferLogs = False

config.JobType.pluginName = 'PrivateMC'
config.JobType.psetName = 'SMP-RunIIFall18wmLHEGS-00059_1_cfg_TL.py'
config.JobType.inputFiles = ['/eos/user/j/jixiao/polar/VBS_SSWW_TL_slc6_amd64_gcc630_CMSSW_9_3_16_tarball.tar.xz']
config.Data.outputPrimaryDataset = 'Bulk'
config.Data.splitting = 'EventBased'
config.Data.unitsPerJob = 500
NJOBS = 200  # This is not a configuration parameter, but an auxiliary variable that we use in the next line.
config.Data.totalUnits = config.Data.unitsPerJob * NJOBS
config.Data.outLFNDirBase = '/store/user/%s/polarization_2018' % (getUsernameFromSiteDB())
config.Data.publication = True
config.Data.outputDatasetTag = 'VBS_SSWW_TL_LHE'

config.Site.storageSite = 'T2_CN_Beijing'