# Auto generated configuration file
# using: 
# Revision: 1.19 
# Source: /local/reps/CMSSW/CMSSW/Configuration/Applications/python/ConfigBuilder.py,v 
# with command line options: --python_filename SMP-RunIIFall17NanoAODv7-00030_1_cfg.py --eventcontent NANOEDMAODSIM --customise Configuration/DataProcessing/Utils.addMonitoring --datatier NANOAODSIM --fileout file:SMP-RunIIFall17NanoAODv7-00030.root --conditions 102X_mc2017_realistic_v8 --step NANO --filein dbs:/WLLJJ_WToLNu_EWK_TuneCP5_13TeV_madgraph-madspin-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM --era Run2_2017,run2_nanoAOD_94XMiniAODv2 --no_exec --mc -n 10000
import FWCore.ParameterSet.Config as cms

from Configuration.StandardSequences.Eras import eras

process = cms.Process('NANO',eras.Run2_2017,eras.run2_nanoAOD_94XMiniAODv2)

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
        '/store/mc/RunIIFall17MiniAODv2/WLLJJ_WToLNu_EWK_TuneCP5_13TeV_madgraph-madspin-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/00000/BA64B6FA-B04E-E811-B940-00000086FE80.root', 
        '/store/mc/RunIIFall17MiniAODv2/WLLJJ_WToLNu_EWK_TuneCP5_13TeV_madgraph-madspin-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/00000/E864C55F-C74F-E811-9217-0242AC130002.root', 
        '/store/mc/RunIIFall17MiniAODv2/WLLJJ_WToLNu_EWK_TuneCP5_13TeV_madgraph-madspin-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/00000/727AFBB6-9450-E811-BEE5-003048FF273A.root', 
        '/store/mc/RunIIFall17MiniAODv2/WLLJJ_WToLNu_EWK_TuneCP5_13TeV_madgraph-madspin-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/00000/B2C057B5-6350-E811-A96C-0CC47A7C340E.root', 
        '/store/mc/RunIIFall17MiniAODv2/WLLJJ_WToLNu_EWK_TuneCP5_13TeV_madgraph-madspin-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/00000/7660D561-B052-E811-A8DB-F01FAFD69174.root', 
        '/store/mc/RunIIFall17MiniAODv2/WLLJJ_WToLNu_EWK_TuneCP5_13TeV_madgraph-madspin-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/00000/60297902-1551-E811-88FD-008CFAC93B20.root', 
        '/store/mc/RunIIFall17MiniAODv2/WLLJJ_WToLNu_EWK_TuneCP5_13TeV_madgraph-madspin-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/00000/F82F3940-9C50-E811-A98E-FA163EA34E4C.root', 
        '/store/mc/RunIIFall17MiniAODv2/WLLJJ_WToLNu_EWK_TuneCP5_13TeV_madgraph-madspin-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/00000/A68E1882-1950-E811-9F29-FA163ECABC5E.root', 
        '/store/mc/RunIIFall17MiniAODv2/WLLJJ_WToLNu_EWK_TuneCP5_13TeV_madgraph-madspin-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/00000/D4BB668D-3C50-E811-87C8-FA163EE28AFD.root', 
        '/store/mc/RunIIFall17MiniAODv2/WLLJJ_WToLNu_EWK_TuneCP5_13TeV_madgraph-madspin-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/00000/1CC74014-5150-E811-9321-FA163E6E7962.root', 
        '/store/mc/RunIIFall17MiniAODv2/WLLJJ_WToLNu_EWK_TuneCP5_13TeV_madgraph-madspin-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/00000/7E89A662-7751-E811-A580-FA163EF75B2B.root', 
        '/store/mc/RunIIFall17MiniAODv2/WLLJJ_WToLNu_EWK_TuneCP5_13TeV_madgraph-madspin-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/00000/3C6BB476-3450-E811-876A-E0071B7A8570.root', 
        '/store/mc/RunIIFall17MiniAODv2/WLLJJ_WToLNu_EWK_TuneCP5_13TeV_madgraph-madspin-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/00000/DA97AC81-764F-E811-BA47-0025905A607E.root', 
        '/store/mc/RunIIFall17MiniAODv2/WLLJJ_WToLNu_EWK_TuneCP5_13TeV_madgraph-madspin-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/00000/E42AF3F8-C04F-E811-8C77-0025905A60CE.root', 
        '/store/mc/RunIIFall17MiniAODv2/WLLJJ_WToLNu_EWK_TuneCP5_13TeV_madgraph-madspin-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/00000/4095EC31-FA4F-E811-9333-0CC47A4D7606.root', 
        '/store/mc/RunIIFall17MiniAODv2/WLLJJ_WToLNu_EWK_TuneCP5_13TeV_madgraph-madspin-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/00000/36E8520C-7A50-E811-A8CF-0CC47A7C35D2.root', 
        '/store/mc/RunIIFall17MiniAODv2/WLLJJ_WToLNu_EWK_TuneCP5_13TeV_madgraph-madspin-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/00000/58FE69C8-CD50-E811-A39D-0CC47A7C3420.root', 
        '/store/mc/RunIIFall17MiniAODv2/WLLJJ_WToLNu_EWK_TuneCP5_13TeV_madgraph-madspin-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/00000/7ACE9AA5-3151-E811-836F-0CC47A4C8E26.root', 
        '/store/mc/RunIIFall17MiniAODv2/WLLJJ_WToLNu_EWK_TuneCP5_13TeV_madgraph-madspin-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/00000/F88822FF-9451-E811-8A17-00248C55CC9D.root', 
        '/store/mc/RunIIFall17MiniAODv2/WLLJJ_WToLNu_EWK_TuneCP5_13TeV_madgraph-madspin-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/00000/843FC8A2-D958-E811-9102-7845C4FBB764.root', 
        '/store/mc/RunIIFall17MiniAODv2/WLLJJ_WToLNu_EWK_TuneCP5_13TeV_madgraph-madspin-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/00000/02A0739C-D155-E811-AF6D-00000086FE80.root', 
        '/store/mc/RunIIFall17MiniAODv2/WLLJJ_WToLNu_EWK_TuneCP5_13TeV_madgraph-madspin-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/00000/28B75FB8-D958-E811-BE87-D4AE526A0C89.root', 
        '/store/mc/RunIIFall17MiniAODv2/WLLJJ_WToLNu_EWK_TuneCP5_13TeV_madgraph-madspin-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/00000/EE13111D-D858-E811-8DC6-008CFAF21F34.root', 
        '/store/mc/RunIIFall17MiniAODv2/WLLJJ_WToLNu_EWK_TuneCP5_13TeV_madgraph-madspin-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/00000/4EA37BF7-D558-E811-ACAA-001E67792702.root', 
        '/store/mc/RunIIFall17MiniAODv2/WLLJJ_WToLNu_EWK_TuneCP5_13TeV_madgraph-madspin-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/00000/54713F74-0C59-E811-A889-0CC47AF9B1AA.root', 
        '/store/mc/RunIIFall17MiniAODv2/WLLJJ_WToLNu_EWK_TuneCP5_13TeV_madgraph-madspin-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/00000/44AED2B6-DC58-E811-809C-509A4C7489E2.root', 
        '/store/mc/RunIIFall17MiniAODv2/WLLJJ_WToLNu_EWK_TuneCP5_13TeV_madgraph-madspin-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/00000/38FEB8EB-8659-E811-AFB3-1CB72C1B2D88.root', 
        '/store/mc/RunIIFall17MiniAODv2/WLLJJ_WToLNu_EWK_TuneCP5_13TeV_madgraph-madspin-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/00000/A20B1AAD-1059-E811-B83F-008CFA56D794.root', 
        '/store/mc/RunIIFall17MiniAODv2/WLLJJ_WToLNu_EWK_TuneCP5_13TeV_madgraph-madspin-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/00000/B24C5194-BE4F-E811-B714-0CC47AD98BCC.root', 
        '/store/mc/RunIIFall17MiniAODv2/WLLJJ_WToLNu_EWK_TuneCP5_13TeV_madgraph-madspin-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/00000/A0E163D5-7959-E811-99E8-FA163E4DAB5E.root', 
        '/store/mc/RunIIFall17MiniAODv2/WLLJJ_WToLNu_EWK_TuneCP5_13TeV_madgraph-madspin-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/00000/EAD63AEE-E158-E811-9CBB-001E675051BD.root', 
        '/store/mc/RunIIFall17MiniAODv2/WLLJJ_WToLNu_EWK_TuneCP5_13TeV_madgraph-madspin-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/00000/6C6110BB-D858-E811-A93F-A0369FE2C0E2.root', 
        '/store/mc/RunIIFall17MiniAODv2/WLLJJ_WToLNu_EWK_TuneCP5_13TeV_madgraph-madspin-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/00000/5A7A1622-D858-E811-AC19-C4346BC08440.root', 
        '/store/mc/RunIIFall17MiniAODv2/WLLJJ_WToLNu_EWK_TuneCP5_13TeV_madgraph-madspin-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/00000/F496E4E8-8659-E811-B38D-00269E95B014.root', 
        '/store/mc/RunIIFall17MiniAODv2/WLLJJ_WToLNu_EWK_TuneCP5_13TeV_madgraph-madspin-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/00000/80E6CE9D-DF58-E811-B5C2-1C6A7A21A33B.root', 
        '/store/mc/RunIIFall17MiniAODv2/WLLJJ_WToLNu_EWK_TuneCP5_13TeV_madgraph-madspin-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/00000/48D12E46-2E59-E811-902E-44A842CF05B2.root', 
        '/store/mc/RunIIFall17MiniAODv2/WLLJJ_WToLNu_EWK_TuneCP5_13TeV_madgraph-madspin-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/00000/1C660D52-E058-E811-8C47-B083FECFD4F0.root'
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
    fileName = cms.untracked.string('file:SMP-RunIIFall17NanoAODv7-00030.root'),
    outputCommands = process.NANOAODSIMEventContent.outputCommands
)

# Additional output definition

# Other statements
from Configuration.AlCa.GlobalTag import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, '102X_mc2017_realistic_v8', '')

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
