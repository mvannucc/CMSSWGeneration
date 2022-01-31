# Auto generated configuration file
# using: 
# Revision: 1.19 
# Source: /local/reps/CMSSW/CMSSW/Configuration/Applications/python/ConfigBuilder.py,v 
# with command line options: --python_filename SMP-RunIISummer16NanoAODv7-00241_1_cfg.py --eventcontent NANOEDMAODSIM --customise Configuration/DataProcessing/Utils.addMonitoring --datatier NANOAODSIM --fileout file:SMP-RunIISummer16NanoAODv7-00241.root --conditions 102X_mcRun2_asymptotic_v8 --step NANO --filein dbs:/WLLJJ_WToLNu_EWK_TuneCUETP8M1_13TeV_madgraph-madspin-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM --era Run2_2016,run2_nanoAOD_94X2016 --no_exec --mc -n 10000
import FWCore.ParameterSet.Config as cms

from Configuration.StandardSequences.Eras import eras

process = cms.Process('NANO',eras.Run2_2016,eras.run2_nanoAOD_94X2016)

# import of standard configurations
process.load('Configuration.StandardSequences.Services_cff')
process.load('SimGeneral.HepPDTESSource.pythiapdt_cfi')
process.load('FWCore.MessageService.MessageLogger_cfi')
process.load('Configuration.EventContent.EventContent_cff')
process.load('SimGeneral.MixingModule.mixNoPU_cfi')
process.load('Configuration.StandardSequences.GeometryRecoDB_cff')
process.load('Configuration.StandardSequences.MagneticField_cff')
process.load('PhysicsTools.NanoAOD.nano_cff')
process.load('Configuration.StandardSequences.EndOfProcess_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(10000)
)

# Input source
process.source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring(
        '/store/mc/RunIISummer16MiniAODv3/WLLJJ_WToLNu_EWK_TuneCUETP8M1_13TeV_madgraph-madspin-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/00000/C23D1F4F-2AD2-E811-B55C-5065F38142E1.root', 
        '/store/mc/RunIISummer16MiniAODv3/WLLJJ_WToLNu_EWK_TuneCUETP8M1_13TeV_madgraph-madspin-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/00000/BE5726D2-1BD2-E811-ACF4-0242AC130002.root', 
        '/store/mc/RunIISummer16MiniAODv3/WLLJJ_WToLNu_EWK_TuneCUETP8M1_13TeV_madgraph-madspin-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/110000/EE85A7CE-4ED2-E811-B659-5065F38102F1.root', 
        '/store/mc/RunIISummer16MiniAODv3/WLLJJ_WToLNu_EWK_TuneCUETP8M1_13TeV_madgraph-madspin-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/110000/40113805-5FD2-E811-9C51-EC0D9A8221FE.root', 
        '/store/mc/RunIISummer16MiniAODv3/WLLJJ_WToLNu_EWK_TuneCUETP8M1_13TeV_madgraph-madspin-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/110000/BE7EF452-64D2-E811-A919-E0071B6C9DD0.root', 
        '/store/mc/RunIISummer16MiniAODv3/WLLJJ_WToLNu_EWK_TuneCUETP8M1_13TeV_madgraph-madspin-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/110000/B606967B-65D2-E811-84EB-24BE05C616E1.root', 
        '/store/mc/RunIISummer16MiniAODv3/WLLJJ_WToLNu_EWK_TuneCUETP8M1_13TeV_madgraph-madspin-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/110000/74161721-49D2-E811-950C-0242AC130002.root', 
        '/store/mc/RunIISummer16MiniAODv3/WLLJJ_WToLNu_EWK_TuneCUETP8M1_13TeV_madgraph-madspin-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/110000/42BE07F0-4AD2-E811-BE05-0242AC130002.root', 
        '/store/mc/RunIISummer16MiniAODv3/WLLJJ_WToLNu_EWK_TuneCUETP8M1_13TeV_madgraph-madspin-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/110000/96B4AC2D-4BD2-E811-9687-0242AC130002.root', 
        '/store/mc/RunIISummer16MiniAODv3/WLLJJ_WToLNu_EWK_TuneCUETP8M1_13TeV_madgraph-madspin-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/110000/1C583A17-4BD2-E811-8507-0242AC130002.root', 
        '/store/mc/RunIISummer16MiniAODv3/WLLJJ_WToLNu_EWK_TuneCUETP8M1_13TeV_madgraph-madspin-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/110000/0A676E98-4DD2-E811-9466-0242AC130002.root', 
        '/store/mc/RunIISummer16MiniAODv3/WLLJJ_WToLNu_EWK_TuneCUETP8M1_13TeV_madgraph-madspin-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/110000/AE6CBC57-AFD2-E811-A569-E0071B740D80.root'
    ),
    secondaryFileNames = cms.untracked.vstring()
)

process.options = cms.untracked.PSet(

)

# Production Info
process.configurationMetadata = cms.untracked.PSet(
    annotation = cms.untracked.string('--python_filename nevts:10000'),
    name = cms.untracked.string('Applications'),
    version = cms.untracked.string('$Revision: 1.19 $')
)

# Output definition

process.NANOEDMAODSIMoutput = cms.OutputModule("PoolOutputModule",
    compressionAlgorithm = cms.untracked.string('LZMA'),
    compressionLevel = cms.untracked.int32(9),
    dataset = cms.untracked.PSet(
        dataTier = cms.untracked.string('NANOAODSIM'),
        filterName = cms.untracked.string('')
    ),
    fileName = cms.untracked.string('file:SMP-RunIISummer16NanoAODv7-00241.root'),
    outputCommands = process.NANOAODSIMEventContent.outputCommands
)

# Additional output definition

# Other statements
from Configuration.AlCa.GlobalTag import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, '102X_mcRun2_asymptotic_v8', '')

# Path and EndPath definitions
process.nanoAOD_step = cms.Path(process.nanoSequenceMC)
process.endjob_step = cms.EndPath(process.endOfProcess)
process.NANOEDMAODSIMoutput_step = cms.EndPath(process.NANOEDMAODSIMoutput)

# Schedule definition
process.schedule = cms.Schedule(process.nanoAOD_step,process.endjob_step,process.NANOEDMAODSIMoutput_step)
from PhysicsTools.PatAlgos.tools.helpers import associatePatAlgosToolsTask
associatePatAlgosToolsTask(process)

# customisation of the process.

# Automatic addition of the customisation function from PhysicsTools.NanoAOD.nano_cff
from PhysicsTools.NanoAOD.nano_cff import nanoAOD_customizeMC 

#call to customisation function nanoAOD_customizeMC imported from PhysicsTools.NanoAOD.nano_cff
process = nanoAOD_customizeMC(process)

# Automatic addition of the customisation function from Configuration.DataProcessing.Utils
from Configuration.DataProcessing.Utils import addMonitoring 

#call to customisation function addMonitoring imported from Configuration.DataProcessing.Utils
process = addMonitoring(process)

# End of customisation functions

# Customisation from command line

# Add early deletion of temporary data products to reduce peak memory need
from Configuration.StandardSequences.earlyDeleteSettings_cff import customiseEarlyDelete
process = customiseEarlyDelete(process)
# End adding early deletion
