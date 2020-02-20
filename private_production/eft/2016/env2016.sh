#!/bin/bash

# refer to: https://cms-pdmv.cern.ch/mcm/chained_requests?contains=SMP-RunIISummer16NanoAODv5-00095&page=0&shown=15
echo '>>>>>>>>>>>>> set environment for GENSIM'
export SCRAM_ARCH=slc6_amd64_gcc481
source /cvmfs/cms.cern.ch/cmsset_default.sh
if [ -r CMSSW_7_1_21_patch2/src ] ; then 
 echo release CMSSW_7_1_21_patch2 already exists
else
scram p CMSSW CMSSW_7_1_21_patch2
fi
cd CMSSW_7_1_21_patch2/src
eval `scram runtime -sh`

curl -s --insecure https://cms-pdmv.cern.ch/mcm/public/restapi/requests/get_fragment/SMP-RunIISummer15wmLHEGS-00006 --retry 2 --create-dirs -o Configuration/GenProduction/python/SMP-RunIISummer15wmLHEGS-00006-fragment.py 
[ -s Configuration/GenProduction/python/SMP-RunIISummer15wmLHEGS-00006-fragment.py ] || exit $?;

scram b
cd ../../
seed=$(($(date +%s) % 100 + 1))
cmsDriver.py Configuration/GenProduction/python/SMP-RunIISummer15wmLHEGS-00006-fragment.py --fileout file:SMP-RunIISummer15wmLHEGS-00006.root --mc --eventcontent RAWSIM,LHE --datatier GEN-SIM,LHE --customise SLHCUpgradeSimulations/Configuration/postLS1Customs.customisePostLS1,Configuration/DataProcessing/Utils.addMonitoring --conditions MCRUN2_71_V1::All --beamspot Realistic50ns13TeVCollision --step LHE,GEN,SIM,VALIDATION:genvalid_all --magField 38T_PostLS1 --python_filename SMP-RunIISummer15wmLHEGS-00006_1_cfg.py --no_exec --customise_commands process.RandomNumberGeneratorService.externalLHEProducer.initialSeed="int(${seed})" -n 49 || exit $? ; 

cp SMP-RunIISummer15wmLHEGS-00006_1_cfg.py SMP-RunIISummer15wmLHEGS-00006_1_cfg_SM.py
cp SMP-RunIISummer15wmLHEGS-00006_1_cfg.py SMP-RunIISummer15wmLHEGS-00006_1_cfg_INT.py
cp SMP-RunIISummer15wmLHEGS-00006_1_cfg.py SMP-RunIISummer15wmLHEGS-00006_1_cfg_BSM.py

sed "s/^.*args = cms.vstring(.*$/    args = cms.vstring('..\/SSWW_SMlimit_slc6_amd64_gcc630_CMSSW_9_3_16_tarball.tar.xz'),/" -i SMP-RunIISummer15wmLHEGS-00006_1_cfg_SM.py
sed "s/^.*args = cms.vstring(.*$/    args = cms.vstring('..\/SSWW_RcW_int_slc6_amd64_gcc630_CMSSW_9_3_16_tarball.tar.xz'),/" -i SMP-RunIISummer15wmLHEGS-00006_1_cfg_INT.py
sed "s/^.*args = cms.vstring(.*$/    args = cms.vstring('..\/SSWW_RcW_bsm_slc6_amd64_gcc630_CMSSW_9_3_16_tarball.tar.xz'),/" -i SMP-RunIISummer15wmLHEGS-00006_1_cfg_BSM.py

echo '>>>>>>>>>>>>> set environment for Premix'
export SCRAM_ARCH=slc6_amd64_gcc530
source /cvmfs/cms.cern.ch/cmsset_default.sh
if [ -r CMSSW_8_0_21/src ] ; then 
 echo release CMSSW_8_0_21 already exists
else
scram p CMSSW CMSSW_8_0_21
fi
cd CMSSW_8_0_21/src
eval `scram runtime -sh`


scram b
cd ../../
cmsDriver.py step1 --filein "dbs:/WpWpJJ_EWK_TuneCUETP8M1_13TeV-madgraph-pythia8/RunIISummer15wmLHEGS-MCRUN2_71_V1-v1/GEN-SIM" --fileout file:SMP-RunIISummer16DR80Premix-00098_step1.root  --pileup_input "dbs:/Neutrino_E-10_gun/RunIISpring15PrePremix-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v2-v2/GEN-SIM-DIGI-RAW" --mc --eventcontent PREMIXRAW --datatier GEN-SIM-RAW --conditions 80X_mcRun2_asymptotic_2016_TrancheIV_v6 --step DIGIPREMIX_S2,DATAMIX,L1,DIGI2RAW,HLT:@frozen2016 --nThreads 4 --datamix PreMix --era Run2_2016 --python_filename SMP-RunIISummer16DR80Premix-00098_1_cfg.py --no_exec --customise Configuration/DataProcessing/Utils.addMonitoring -n 169 || exit $? ; 

cmsDriver.py step2 --filein file:SMP-RunIISummer16DR80Premix-00098_step1.root --fileout file:SMP-RunIISummer16DR80Premix-00098.root --mc --eventcontent AODSIM --runUnscheduled --datatier AODSIM --conditions 80X_mcRun2_asymptotic_2016_TrancheIV_v6 --step RAW2DIGI,RECO,EI --nThreads 4 --era Run2_2016 --python_filename SMP-RunIISummer16DR80Premix-00098_2_cfg.py --no_exec --customise Configuration/DataProcessing/Utils.addMonitoring -n 169 || exit $? ; 

echo '>>>>>>>>>>>>> set environment for MINIAODSIM'
export SCRAM_ARCH=slc6_amd64_gcc630
source /cvmfs/cms.cern.ch/cmsset_default.sh
if [ -r CMSSW_9_4_9/src ] ; then 
 echo release CMSSW_9_4_9 already exists
else
scram p CMSSW CMSSW_9_4_9
fi
cd CMSSW_9_4_9/src
eval `scram runtime -sh`


scram b
cd ../../
cmsDriver.py step1 --filein "dbs:/WpWpJJ_EWK_TuneCUETP8M1_13TeV-madgraph-pythia8/RunIISummer16DR80Premix-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/AODSIM" --fileout file:SMP-RunIISummer16MiniAODv3-00004.root --mc --eventcontent MINIAODSIM --runUnscheduled --datatier MINIAODSIM --conditions 94X_mcRun2_asymptotic_v3 --step PAT --nThreads 8 --era Run2_2016,run2_miniAOD_80XLegacy --python_filename SMP-RunIISummer16MiniAODv3-00004_1_cfg.py --no_exec --customise Configuration/DataProcessing/Utils.addMonitoring -n 10000 || exit $? ; 

echo '>>>>>>>>>>>>> set environment for NANOAODSIM'
export SCRAM_ARCH=slc6_amd64_gcc700
source /cvmfs/cms.cern.ch/cmsset_default.sh
if [ -r CMSSW_10_2_15/src ] ; then 
 echo release CMSSW_10_2_15 already exists
else
scram p CMSSW CMSSW_10_2_15
fi
cd CMSSW_10_2_15/src
eval `scram runtime -sh`


scram b
cd ../../
cmsDriver.py step1 --filein "dbs:/WpWpJJ_EWK_TuneCUETP8M1_13TeV-madgraph-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM" --fileout file:SMP-RunIISummer16NanoAODv5-00095.root --mc --eventcontent NANOAODSIM --datatier NANOAODSIM --conditions 102X_mcRun2_asymptotic_v7 --step NANO --nThreads 2 --era Run2_2016,run2_nanoAOD_94X2016 --python_filename SMP-RunIISummer16NanoAODv5-00095_1_cfg.py --no_exec --customise Configuration/DataProcessing/Utils.addMonitoring -n 3840 || exit $? ; 
sed '/process.NANOAODSIMoutput = cms.OutputModule("NanoAODOutputModule",/a\    fakeNameForCrab =cms.untracked.bool(True),' -i SMP-RunIISummer16NanoAODv5-00095_1_cfg.py