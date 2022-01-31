# Auto generated configuration file
# using: 
# Revision: 1.19 
# Source: /local/reps/CMSSW/CMSSW/Configuration/Applications/python/ConfigBuilder.py,v 
# with command line options: --python_filename SMP-RunIIFall17MiniAODv2-00029_1_cfg.py --eventcontent MINIAODSIM --customise Configuration/DataProcessing/Utils.addMonitoring --datatier MINIAODSIM --fileout file:SMP-RunIIFall17MiniAODv2-00029.root --conditions 94X_mc2017_realistic_v14 --step PAT --scenario pp --filein dbs:/WLLJJ_WToLNu_EWK_TuneCP5_13TeV_madgraph-madspin-pythia8/RunIIFall17DRPremix-PU2017_94X_mc2017_realistic_v11-v2/AODSIM --era Run2_2017,run2_miniAOD_94XFall17 --runUnscheduled --no_exec --mc -n 4200
import FWCore.ParameterSet.Config as cms

from Configuration.StandardSequences.Eras import eras

process = cms.Process('PAT',eras.Run2_2017,eras.run2_miniAOD_94XFall17)

# import of standard configurations
process.load('Configuration.StandardSequences.Services_cff')
process.load('SimGeneral.HepPDTESSource.pythiapdt_cfi')
process.load('FWCore.MessageService.MessageLogger_cfi')
process.load('Configuration.EventContent.EventContent_cff')
process.load('SimGeneral.MixingModule.mixNoPU_cfi')
process.load('Configuration.StandardSequences.GeometryRecoDB_cff')
process.load('Configuration.StandardSequences.MagneticField_cff')
process.load('PhysicsTools.PatAlgos.slimming.metFilterPaths_cff')
process.load('Configuration.StandardSequences.PATMC_cff')
process.load('Configuration.StandardSequences.EndOfProcess_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(4200)
)

# Input source
process.source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring('/store/mc/RunIIFall17DRPremix/WLLJJ_WToLNu_EWK_TuneCP5_13TeV_madgraph-madspin-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v2/00000/4C0921B9-204D-E811-ADAE-E0071B7A6890.root', 
        '/store/mc/RunIIFall17DRPremix/WLLJJ_WToLNu_EWK_TuneCP5_13TeV_madgraph-madspin-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v2/00000/96B6D4D9-AE4D-E811-84C8-5065F381A2E1.root', 
        '/store/mc/RunIIFall17DRPremix/WLLJJ_WToLNu_EWK_TuneCP5_13TeV_madgraph-madspin-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v2/00000/56E9CB8E-B04D-E811-98CD-E0071B7A8550.root', 
        '/store/mc/RunIIFall17DRPremix/WLLJJ_WToLNu_EWK_TuneCP5_13TeV_madgraph-madspin-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v2/00000/02FD74A2-DE4D-E811-B7D5-24BE05CECB51.root', 
        '/store/mc/RunIIFall17DRPremix/WLLJJ_WToLNu_EWK_TuneCP5_13TeV_madgraph-madspin-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v2/00000/90AF2FA1-2A4E-E811-954D-24BE05C33C81.root', 
        '/store/mc/RunIIFall17DRPremix/WLLJJ_WToLNu_EWK_TuneCP5_13TeV_madgraph-madspin-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v2/00000/9298CEA2-FD4E-E811-877C-24BE05C44BC1.root', 
        '/store/mc/RunIIFall17DRPremix/WLLJJ_WToLNu_EWK_TuneCP5_13TeV_madgraph-madspin-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v2/00000/06D19AB3-4C4E-E811-8C05-FA163E016D86.root', 
        '/store/mc/RunIIFall17DRPremix/WLLJJ_WToLNu_EWK_TuneCP5_13TeV_madgraph-madspin-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v2/00000/5EBE3D5C-A14F-E811-BC8C-FA163E6FBE85.root', 
        '/store/mc/RunIIFall17DRPremix/WLLJJ_WToLNu_EWK_TuneCP5_13TeV_madgraph-madspin-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v2/00000/D6272203-A84F-E811-9A20-FA163EDA9606.root', 
        '/store/mc/RunIIFall17DRPremix/WLLJJ_WToLNu_EWK_TuneCP5_13TeV_madgraph-madspin-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v2/00000/46F95817-A84F-E811-A23B-FA163E4FDC41.root', 
        '/store/mc/RunIIFall17DRPremix/WLLJJ_WToLNu_EWK_TuneCP5_13TeV_madgraph-madspin-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v2/00000/E0BE6D54-A14F-E811-A7A4-FA163EB2409E.root', 
        '/store/mc/RunIIFall17DRPremix/WLLJJ_WToLNu_EWK_TuneCP5_13TeV_madgraph-madspin-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v2/00000/366D48BC-DD4E-E811-A003-0CC47A4D7668.root', 
        '/store/mc/RunIIFall17DRPremix/WLLJJ_WToLNu_EWK_TuneCP5_13TeV_madgraph-madspin-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v2/00000/E640EE62-214F-E811-A6A7-0025905B856C.root', 
        '/store/mc/RunIIFall17DRPremix/WLLJJ_WToLNu_EWK_TuneCP5_13TeV_madgraph-madspin-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v2/00000/E416AC97-744E-E811-B140-0CC47A7C3636.root', 
        '/store/mc/RunIIFall17DRPremix/WLLJJ_WToLNu_EWK_TuneCP5_13TeV_madgraph-madspin-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v2/00000/2A87627E-DA4E-E811-8E52-0025905A60D6.root', 
        '/store/mc/RunIIFall17DRPremix/WLLJJ_WToLNu_EWK_TuneCP5_13TeV_madgraph-madspin-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v2/00000/8EAB06DC-454F-E811-A61B-0025905A60DE.root', 
        '/store/mc/RunIIFall17DRPremix/WLLJJ_WToLNu_EWK_TuneCP5_13TeV_madgraph-madspin-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v2/00000/869571C0-004F-E811-9ADF-0025905A60AA.root', 
        '/store/mc/RunIIFall17DRPremix/WLLJJ_WToLNu_EWK_TuneCP5_13TeV_madgraph-madspin-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v2/00000/58B47549-0A4F-E811-B31A-0025905A60D2.root', 
        '/store/mc/RunIIFall17DRPremix/WLLJJ_WToLNu_EWK_TuneCP5_13TeV_madgraph-madspin-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v2/00000/802F2F4E-214F-E811-880D-0CC47A4D767C.root', 
        '/store/mc/RunIIFall17DRPremix/WLLJJ_WToLNu_EWK_TuneCP5_13TeV_madgraph-madspin-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v2/00000/9AFBB22A-304F-E811-88CC-0025905B8604.root', 
        '/store/mc/RunIIFall17DRPremix/WLLJJ_WToLNu_EWK_TuneCP5_13TeV_madgraph-madspin-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v2/00000/C455014C-0A4F-E811-A0C7-0025905B85D8.root', 
        '/store/mc/RunIIFall17DRPremix/WLLJJ_WToLNu_EWK_TuneCP5_13TeV_madgraph-madspin-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v2/00000/5E078A4A-0A4F-E811-92FF-0025905A60B0.root', 
        '/store/mc/RunIIFall17DRPremix/WLLJJ_WToLNu_EWK_TuneCP5_13TeV_madgraph-madspin-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v2/00000/7AD991F5-C24F-E811-8B25-0CC47A4D762E.root', 
        '/store/mc/RunIIFall17DRPremix/WLLJJ_WToLNu_EWK_TuneCP5_13TeV_madgraph-madspin-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v2/00000/72FDEA1B-C34F-E811-8D99-0CC47A4D7638.root', 
        '/store/mc/RunIIFall17DRPremix/WLLJJ_WToLNu_EWK_TuneCP5_13TeV_madgraph-madspin-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v2/00000/8CE5362A-C14F-E811-9B11-0025905A48BA.root', 
        '/store/mc/RunIIFall17DRPremix/WLLJJ_WToLNu_EWK_TuneCP5_13TeV_madgraph-madspin-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v2/00000/A23484CA-FF4F-E811-B18B-0025905B8572.root', 
        '/store/mc/RunIIFall17DRPremix/WLLJJ_WToLNu_EWK_TuneCP5_13TeV_madgraph-madspin-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v2/00000/A62E48A4-FA4F-E811-811A-0CC47A4D7692.root', 
        '/store/mc/RunIIFall17DRPremix/WLLJJ_WToLNu_EWK_TuneCP5_13TeV_madgraph-madspin-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v2/00000/84EAE4A3-F14F-E811-A4AC-0CC47A4C8E3C.root', 
        '/store/mc/RunIIFall17DRPremix/WLLJJ_WToLNu_EWK_TuneCP5_13TeV_madgraph-madspin-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v2/00000/EEA7BBAB-FA4F-E811-AAB4-0025905B85F6.root', 
        '/store/mc/RunIIFall17DRPremix/WLLJJ_WToLNu_EWK_TuneCP5_13TeV_madgraph-madspin-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v2/00000/B27EE8CA-FF4F-E811-8F44-0025905A612A.root', 
        '/store/mc/RunIIFall17DRPremix/WLLJJ_WToLNu_EWK_TuneCP5_13TeV_madgraph-madspin-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v2/00000/3CA14E13-F04F-E811-9746-0CC47A4C8EE8.root', 
        '/store/mc/RunIIFall17DRPremix/WLLJJ_WToLNu_EWK_TuneCP5_13TeV_madgraph-madspin-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v2/00000/90EB9591-F04F-E811-9FA5-0CC47A78A3B4.root', 
        '/store/mc/RunIIFall17DRPremix/WLLJJ_WToLNu_EWK_TuneCP5_13TeV_madgraph-madspin-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v2/00000/B6C0D85B-5650-E811-A8E0-0CC47A78A4BA.root', 
        '/store/mc/RunIIFall17DRPremix/WLLJJ_WToLNu_EWK_TuneCP5_13TeV_madgraph-madspin-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v2/00000/6A61D422-4A4F-E811-85C5-0CC47AA99438.root', 
        '/store/mc/RunIIFall17DRPremix/WLLJJ_WToLNu_EWK_TuneCP5_13TeV_madgraph-madspin-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v2/00000/A0E60D94-4D4F-E811-AFB0-0CC47A2B06DE.root', 
        '/store/mc/RunIIFall17DRPremix/WLLJJ_WToLNu_EWK_TuneCP5_13TeV_madgraph-madspin-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v2/00000/CABEAEB3-6D4E-E811-AF4F-0CC47A6C1864.root', 
        '/store/mc/RunIIFall17DRPremix/WLLJJ_WToLNu_EWK_TuneCP5_13TeV_madgraph-madspin-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v2/00000/407835BC-494F-E811-A6F5-4C79BA180B67.root', 
        '/store/mc/RunIIFall17DRPremix/WLLJJ_WToLNu_EWK_TuneCP5_13TeV_madgraph-madspin-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v2/00000/8EE66D86-494F-E811-B8E4-5065F381F252.root', 
        '/store/mc/RunIIFall17DRPremix/WLLJJ_WToLNu_EWK_TuneCP5_13TeV_madgraph-madspin-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v2/00000/3200ABE0-DF4F-E811-A258-E0071B691B81.root', 
        '/store/mc/RunIIFall17DRPremix/WLLJJ_WToLNu_EWK_TuneCP5_13TeV_madgraph-madspin-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v2/00000/C2FD7569-4A4F-E811-971B-0CC47A6C1806.root', 
        '/store/mc/RunIIFall17DRPremix/WLLJJ_WToLNu_EWK_TuneCP5_13TeV_madgraph-madspin-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v2/00000/2A0AE871-514F-E811-BD70-0CC47A6C1866.root', 
        '/store/mc/RunIIFall17DRPremix/WLLJJ_WToLNu_EWK_TuneCP5_13TeV_madgraph-madspin-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v2/00000/3A3DCBFA-7F4E-E811-A011-0242AC130002.root', 
        '/store/mc/RunIIFall17DRPremix/WLLJJ_WToLNu_EWK_TuneCP5_13TeV_madgraph-madspin-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v2/00000/2CB74F76-B94E-E811-AED5-0242AC130002.root', 
        '/store/mc/RunIIFall17DRPremix/WLLJJ_WToLNu_EWK_TuneCP5_13TeV_madgraph-madspin-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v2/00000/0CCFE871-4A4F-E811-B25E-0242AC130002.root', 
        '/store/mc/RunIIFall17DRPremix/WLLJJ_WToLNu_EWK_TuneCP5_13TeV_madgraph-madspin-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v2/00000/C874A924-574F-E811-8BE8-0242AC130002.root', 
        '/store/mc/RunIIFall17DRPremix/WLLJJ_WToLNu_EWK_TuneCP5_13TeV_madgraph-madspin-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v2/00000/0817649B-4D4F-E811-B64D-0242AC130004.root', 
        '/store/mc/RunIIFall17DRPremix/WLLJJ_WToLNu_EWK_TuneCP5_13TeV_madgraph-madspin-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v2/00000/603FA696-684E-E811-B2B9-008CFAC93DD8.root', 
        '/store/mc/RunIIFall17DRPremix/WLLJJ_WToLNu_EWK_TuneCP5_13TeV_madgraph-madspin-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v2/00000/C473F259-EC4F-E811-AF9A-FA163E9AFDB6.root', 
        '/store/mc/RunIIFall17DRPremix/WLLJJ_WToLNu_EWK_TuneCP5_13TeV_madgraph-madspin-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v2/00000/1E4531FD-ED4F-E811-9083-FA163E644D61.root', 
        '/store/mc/RunIIFall17DRPremix/WLLJJ_WToLNu_EWK_TuneCP5_13TeV_madgraph-madspin-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v2/00000/48CFE035-DE4F-E811-85E0-FA163EF75B2B.root', 
        '/store/mc/RunIIFall17DRPremix/WLLJJ_WToLNu_EWK_TuneCP5_13TeV_madgraph-madspin-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v2/00000/E2F65846-F34F-E811-B4F6-FA163EF9D9FE.root', 
        '/store/mc/RunIIFall17DRPremix/WLLJJ_WToLNu_EWK_TuneCP5_13TeV_madgraph-madspin-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v2/00000/EE373E96-EE4F-E811-B5A8-FA163EAD8059.root', 
        '/store/mc/RunIIFall17DRPremix/WLLJJ_WToLNu_EWK_TuneCP5_13TeV_madgraph-madspin-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v2/00000/30E3DAA3-F74F-E811-B17B-FA163E2BBDCE.root', 
        '/store/mc/RunIIFall17DRPremix/WLLJJ_WToLNu_EWK_TuneCP5_13TeV_madgraph-madspin-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v2/00000/74C6C4DF-EB4F-E811-9082-FA163E80C3B9.root', 
        '/store/mc/RunIIFall17DRPremix/WLLJJ_WToLNu_EWK_TuneCP5_13TeV_madgraph-madspin-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v2/00000/AA318051-F04F-E811-B9F9-FA163E520CE8.root', 
        '/store/mc/RunIIFall17DRPremix/WLLJJ_WToLNu_EWK_TuneCP5_13TeV_madgraph-madspin-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v2/00000/8A1B6DCD-1750-E811-BE2A-FA163EB59EE1.root', 
        '/store/mc/RunIIFall17DRPremix/WLLJJ_WToLNu_EWK_TuneCP5_13TeV_madgraph-madspin-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v2/00000/5256B9DD-0D50-E811-9DF6-FA163EDA9606.root', 
        '/store/mc/RunIIFall17DRPremix/WLLJJ_WToLNu_EWK_TuneCP5_13TeV_madgraph-madspin-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v2/00000/C4B7D47C-1650-E811-BA91-FA163E9AFDB6.root', 
        '/store/mc/RunIIFall17DRPremix/WLLJJ_WToLNu_EWK_TuneCP5_13TeV_madgraph-madspin-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v2/00000/52F7BE7D-1C50-E811-8C6B-FA163E631703.root', 
        '/store/mc/RunIIFall17DRPremix/WLLJJ_WToLNu_EWK_TuneCP5_13TeV_madgraph-madspin-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v2/00000/7E7D6126-5150-E811-8977-FA163EF75B2B.root', 
        '/store/mc/RunIIFall17DRPremix/WLLJJ_WToLNu_EWK_TuneCP5_13TeV_madgraph-madspin-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v2/00000/3EBC5A8D-5150-E811-A113-FA163E10084A.root', 
        '/store/mc/RunIIFall17DRPremix/WLLJJ_WToLNu_EWK_TuneCP5_13TeV_madgraph-madspin-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v2/00000/26B5F4B3-6450-E811-A56C-FA163EF069BE.root', 
        '/store/mc/RunIIFall17DRPremix/WLLJJ_WToLNu_EWK_TuneCP5_13TeV_madgraph-madspin-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v2/00000/F2C3E077-6650-E811-879E-FA163EEB9AB3.root', 
        '/store/mc/RunIIFall17DRPremix/WLLJJ_WToLNu_EWK_TuneCP5_13TeV_madgraph-madspin-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v2/00000/4CB89989-E44F-E811-967E-0CC47AD9914A.root', 
        '/store/mc/RunIIFall17DRPremix/WLLJJ_WToLNu_EWK_TuneCP5_13TeV_madgraph-madspin-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v2/00000/4E0B5433-7F51-E811-9ED2-1866DA85DFA8.root', 
        '/store/mc/RunIIFall17DRPremix/WLLJJ_WToLNu_EWK_TuneCP5_13TeV_madgraph-madspin-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v2/00000/C2D24B40-E14F-E811-B5D9-008CFAE451C4.root', 
        '/store/mc/RunIIFall17DRPremix/WLLJJ_WToLNu_EWK_TuneCP5_13TeV_madgraph-madspin-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v2/00000/2CC309F4-C94F-E811-9E70-1866DA85E0DC.root', 
        '/store/mc/RunIIFall17DRPremix/WLLJJ_WToLNu_EWK_TuneCP5_13TeV_madgraph-madspin-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v2/00000/4C5B0528-7D50-E811-B30B-0CC47A4D7662.root', 
        '/store/mc/RunIIFall17DRPremix/WLLJJ_WToLNu_EWK_TuneCP5_13TeV_madgraph-madspin-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v2/00000/64AD0274-9750-E811-AFD6-0025905A605E.root', 
        '/store/mc/RunIIFall17DRPremix/WLLJJ_WToLNu_EWK_TuneCP5_13TeV_madgraph-madspin-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v2/00000/B0B7E34B-7950-E811-9E6F-0025905A48BC.root', 
        '/store/mc/RunIIFall17DRPremix/WLLJJ_WToLNu_EWK_TuneCP5_13TeV_madgraph-madspin-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v2/00000/E46DC994-5650-E811-964A-0025905B85F6.root', 
        '/store/mc/RunIIFall17DRPremix/WLLJJ_WToLNu_EWK_TuneCP5_13TeV_madgraph-madspin-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v2/00000/9A1C3ADE-9650-E811-9FC9-0CC47A4C8F10.root', 
        '/store/mc/RunIIFall17DRPremix/WLLJJ_WToLNu_EWK_TuneCP5_13TeV_madgraph-madspin-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v2/00000/F032560B-7850-E811-A149-0025905B85BA.root', 
        '/store/mc/RunIIFall17DRPremix/WLLJJ_WToLNu_EWK_TuneCP5_13TeV_madgraph-madspin-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v2/00000/0C7E6A69-C150-E811-8F82-0CC47A74527A.root', 
        '/store/mc/RunIIFall17DRPremix/WLLJJ_WToLNu_EWK_TuneCP5_13TeV_madgraph-madspin-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v2/00000/68C6E431-DA50-E811-A518-0CC47A4C8EB0.root', 
        '/store/mc/RunIIFall17DRPremix/WLLJJ_WToLNu_EWK_TuneCP5_13TeV_madgraph-madspin-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v2/00000/681815BB-D850-E811-A1F2-0025905B85BA.root', 
        '/store/mc/RunIIFall17DRPremix/WLLJJ_WToLNu_EWK_TuneCP5_13TeV_madgraph-madspin-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v2/00000/D0C16AE9-3851-E811-89AA-0025905A612A.root', 
        '/store/mc/RunIIFall17DRPremix/WLLJJ_WToLNu_EWK_TuneCP5_13TeV_madgraph-madspin-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v2/00000/50B50956-1A55-E811-9AE0-0CC47A4DEEBA.root', 
        '/store/mc/RunIIFall17DRPremix/WLLJJ_WToLNu_EWK_TuneCP5_13TeV_madgraph-madspin-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v2/00000/78D42D3A-0255-E811-89CC-0242AC1C0503.root', 
        '/store/mc/RunIIFall17DRPremix/WLLJJ_WToLNu_EWK_TuneCP5_13TeV_madgraph-madspin-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v2/00000/EEBABF23-4454-E811-BEC6-509A4C74D09C.root', 
        '/store/mc/RunIIFall17DRPremix/WLLJJ_WToLNu_EWK_TuneCP5_13TeV_madgraph-madspin-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v2/00000/923F10FE-1255-E811-871B-7CD30AD0A1F8.root', 
        '/store/mc/RunIIFall17DRPremix/WLLJJ_WToLNu_EWK_TuneCP5_13TeV_madgraph-madspin-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v2/00000/DECCDFBE-A355-E811-9E20-1866DA87B0FE.root', 
        '/store/mc/RunIIFall17DRPremix/WLLJJ_WToLNu_EWK_TuneCP5_13TeV_madgraph-madspin-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v2/00000/8E00EE71-DC54-E811-AD98-002590A83192.root', 
        '/store/mc/RunIIFall17DRPremix/WLLJJ_WToLNu_EWK_TuneCP5_13TeV_madgraph-madspin-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v2/00000/B22D7AFC-E254-E811-9AB1-A0369F83627A.root', 
        '/store/mc/RunIIFall17DRPremix/WLLJJ_WToLNu_EWK_TuneCP5_13TeV_madgraph-madspin-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v2/00000/023708E7-1654-E811-942F-44A842CFC9F3.root', 
        '/store/mc/RunIIFall17DRPremix/WLLJJ_WToLNu_EWK_TuneCP5_13TeV_madgraph-madspin-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v2/00000/C4375B91-0A55-E811-9DDF-001E67504FFD.root', 
        '/store/mc/RunIIFall17DRPremix/WLLJJ_WToLNu_EWK_TuneCP5_13TeV_madgraph-madspin-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v2/00000/80B4A1A4-B855-E811-879B-34E6D7BEAF28.root', 
        '/store/mc/RunIIFall17DRPremix/WLLJJ_WToLNu_EWK_TuneCP5_13TeV_madgraph-madspin-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v2/00000/5AE33EAC-DE54-E811-89A7-3417EBE51E38.root', 
        '/store/mc/RunIIFall17DRPremix/WLLJJ_WToLNu_EWK_TuneCP5_13TeV_madgraph-madspin-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v2/00000/BE5025B1-9757-E811-8527-141877640173.root', 
        '/store/mc/RunIIFall17DRPremix/WLLJJ_WToLNu_EWK_TuneCP5_13TeV_madgraph-madspin-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v2/00000/AEAC8EBE-0658-E811-B8C8-ECB1D79E5C40.root', 
        '/store/mc/RunIIFall17DRPremix/WLLJJ_WToLNu_EWK_TuneCP5_13TeV_madgraph-madspin-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v2/00000/444C0C85-1C55-E811-9F58-B496910A0430.root', 
        '/store/mc/RunIIFall17DRPremix/WLLJJ_WToLNu_EWK_TuneCP5_13TeV_madgraph-madspin-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v2/00000/9ECEF242-1A54-E811-94F3-0025904C66E6.root'),
    secondaryFileNames = cms.untracked.vstring()
)

process.options = cms.untracked.PSet(

)

# Production Info
process.configurationMetadata = cms.untracked.PSet(
    annotation = cms.untracked.string('--python_filename nevts:4200'),
    name = cms.untracked.string('Applications'),
    version = cms.untracked.string('$Revision: 1.19 $')
)

# Output definition

process.MINIAODSIMoutput = cms.OutputModule("PoolOutputModule",
    compressionAlgorithm = cms.untracked.string('LZMA'),
    compressionLevel = cms.untracked.int32(4),
    dataset = cms.untracked.PSet(
        dataTier = cms.untracked.string('MINIAODSIM'),
        filterName = cms.untracked.string('')
    ),
    dropMetaData = cms.untracked.string('ALL'),
    eventAutoFlushCompressedSize = cms.untracked.int32(-900),
    fastCloning = cms.untracked.bool(False),
    fileName = cms.untracked.string('file:SMP-RunIIFall17MiniAODv2-00029.root'),
    outputCommands = process.MINIAODSIMEventContent.outputCommands,
    overrideBranchesSplitLevel = cms.untracked.VPSet(cms.untracked.PSet(
        branch = cms.untracked.string('patPackedCandidates_packedPFCandidates__*'),
        splitLevel = cms.untracked.int32(99)
    ), 
        cms.untracked.PSet(
            branch = cms.untracked.string('recoGenParticles_prunedGenParticles__*'),
            splitLevel = cms.untracked.int32(99)
        ), 
        cms.untracked.PSet(
            branch = cms.untracked.string('patTriggerObjectStandAlones_slimmedPatTrigger__*'),
            splitLevel = cms.untracked.int32(99)
        ), 
        cms.untracked.PSet(
            branch = cms.untracked.string('patPackedGenParticles_packedGenParticles__*'),
            splitLevel = cms.untracked.int32(99)
        ), 
        cms.untracked.PSet(
            branch = cms.untracked.string('patJets_slimmedJets__*'),
            splitLevel = cms.untracked.int32(99)
        ), 
        cms.untracked.PSet(
            branch = cms.untracked.string('recoVertexs_offlineSlimmedPrimaryVertices__*'),
            splitLevel = cms.untracked.int32(99)
        ), 
        cms.untracked.PSet(
            branch = cms.untracked.string('recoCaloClusters_reducedEgamma_reducedESClusters_*'),
            splitLevel = cms.untracked.int32(99)
        ), 
        cms.untracked.PSet(
            branch = cms.untracked.string('EcalRecHitsSorted_reducedEgamma_reducedEBRecHits_*'),
            splitLevel = cms.untracked.int32(99)
        ), 
        cms.untracked.PSet(
            branch = cms.untracked.string('EcalRecHitsSorted_reducedEgamma_reducedEERecHits_*'),
            splitLevel = cms.untracked.int32(99)
        ), 
        cms.untracked.PSet(
            branch = cms.untracked.string('recoGenJets_slimmedGenJets__*'),
            splitLevel = cms.untracked.int32(99)
        ), 
        cms.untracked.PSet(
            branch = cms.untracked.string('patJets_slimmedJetsPuppi__*'),
            splitLevel = cms.untracked.int32(99)
        ), 
        cms.untracked.PSet(
            branch = cms.untracked.string('EcalRecHitsSorted_reducedEgamma_reducedESRecHits_*'),
            splitLevel = cms.untracked.int32(99)
        )),
    overrideInputFileSplitLevels = cms.untracked.bool(True),
    splitLevel = cms.untracked.int32(0)
)

# Additional output definition

# Other statements
from Configuration.AlCa.GlobalTag import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, '94X_mc2017_realistic_v14', '')

# Path and EndPath definitions
process.Flag_trackingFailureFilter = cms.Path(process.goodVertices+process.trackingFailureFilter)
process.Flag_goodVertices = cms.Path(process.primaryVertexFilter)
process.Flag_CSCTightHaloFilter = cms.Path(process.CSCTightHaloFilter)
process.Flag_trkPOGFilters = cms.Path(process.trkPOGFilters)
process.Flag_HcalStripHaloFilter = cms.Path(process.HcalStripHaloFilter)
process.Flag_trkPOG_logErrorTooManyClusters = cms.Path(~process.logErrorTooManyClusters)
process.Flag_EcalDeadCellTriggerPrimitiveFilter = cms.Path(process.EcalDeadCellTriggerPrimitiveFilter)
process.Flag_ecalLaserCorrFilter = cms.Path(process.ecalLaserCorrFilter)
process.Flag_globalSuperTightHalo2016Filter = cms.Path(process.globalSuperTightHalo2016Filter)
process.Flag_eeBadScFilter = cms.Path(process.eeBadScFilter)
process.Flag_METFilters = cms.Path(process.metFilters)
process.Flag_chargedHadronTrackResolutionFilter = cms.Path(process.chargedHadronTrackResolutionFilter)
process.Flag_globalTightHalo2016Filter = cms.Path(process.globalTightHalo2016Filter)
process.Flag_CSCTightHaloTrkMuUnvetoFilter = cms.Path(process.CSCTightHaloTrkMuUnvetoFilter)
process.Flag_HBHENoiseIsoFilter = cms.Path(process.HBHENoiseFilterResultProducer+process.HBHENoiseIsoFilter)
process.Flag_BadChargedCandidateSummer16Filter = cms.Path(process.BadChargedCandidateSummer16Filter)
process.Flag_hcalLaserEventFilter = cms.Path(process.hcalLaserEventFilter)
process.Flag_BadPFMuonFilter = cms.Path(process.BadPFMuonFilter)
process.Flag_ecalBadCalibFilter = cms.Path(process.ecalBadCalibFilter)
process.Flag_HBHENoiseFilter = cms.Path(process.HBHENoiseFilterResultProducer+process.HBHENoiseFilter)
process.Flag_trkPOG_toomanystripclus53X = cms.Path(~process.toomanystripclus53X)
process.Flag_EcalDeadCellBoundaryEnergyFilter = cms.Path(process.EcalDeadCellBoundaryEnergyFilter)
process.Flag_BadChargedCandidateFilter = cms.Path(process.BadChargedCandidateFilter)
process.Flag_trkPOG_manystripclus53X = cms.Path(~process.manystripclus53X)
process.Flag_BadPFMuonSummer16Filter = cms.Path(process.BadPFMuonSummer16Filter)
process.Flag_muonBadTrackFilter = cms.Path(process.muonBadTrackFilter)
process.Flag_CSCTightHalo2015Filter = cms.Path(process.CSCTightHalo2015Filter)
process.endjob_step = cms.EndPath(process.endOfProcess)
process.MINIAODSIMoutput_step = cms.EndPath(process.MINIAODSIMoutput)

# Schedule definition
process.schedule = cms.Schedule(process.Flag_HBHENoiseFilter,process.Flag_HBHENoiseIsoFilter,process.Flag_CSCTightHaloFilter,process.Flag_CSCTightHaloTrkMuUnvetoFilter,process.Flag_CSCTightHalo2015Filter,process.Flag_globalTightHalo2016Filter,process.Flag_globalSuperTightHalo2016Filter,process.Flag_HcalStripHaloFilter,process.Flag_hcalLaserEventFilter,process.Flag_EcalDeadCellTriggerPrimitiveFilter,process.Flag_EcalDeadCellBoundaryEnergyFilter,process.Flag_ecalBadCalibFilter,process.Flag_goodVertices,process.Flag_eeBadScFilter,process.Flag_ecalLaserCorrFilter,process.Flag_trkPOGFilters,process.Flag_chargedHadronTrackResolutionFilter,process.Flag_muonBadTrackFilter,process.Flag_BadChargedCandidateFilter,process.Flag_BadPFMuonFilter,process.Flag_BadChargedCandidateSummer16Filter,process.Flag_BadPFMuonSummer16Filter,process.Flag_trkPOG_manystripclus53X,process.Flag_trkPOG_toomanystripclus53X,process.Flag_trkPOG_logErrorTooManyClusters,process.Flag_METFilters,process.endjob_step,process.MINIAODSIMoutput_step)
process.schedule.associate(process.patTask)
from PhysicsTools.PatAlgos.tools.helpers import associatePatAlgosToolsTask
associatePatAlgosToolsTask(process)

# customisation of the process.

# Automatic addition of the customisation function from Configuration.DataProcessing.Utils
from Configuration.DataProcessing.Utils import addMonitoring 

#call to customisation function addMonitoring imported from Configuration.DataProcessing.Utils
process = addMonitoring(process)

# End of customisation functions
#do not add changes to your config after this point (unless you know what you are doing)
from FWCore.ParameterSet.Utilities import convertToUnscheduled
process=convertToUnscheduled(process)

# customisation of the process.

# Automatic addition of the customisation function from PhysicsTools.PatAlgos.slimming.miniAOD_tools
from PhysicsTools.PatAlgos.slimming.miniAOD_tools import miniAOD_customizeAllMC 

#call to customisation function miniAOD_customizeAllMC imported from PhysicsTools.PatAlgos.slimming.miniAOD_tools
process = miniAOD_customizeAllMC(process)

# End of customisation functions

# Customisation from command line

# Add early deletion of temporary data products to reduce peak memory need
from Configuration.StandardSequences.earlyDeleteSettings_cff import customiseEarlyDelete
process = customiseEarlyDelete(process)
# End adding early deletion
