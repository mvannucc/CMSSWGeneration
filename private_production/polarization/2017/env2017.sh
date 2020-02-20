#!/bin/bash

# refer to: https://cms-pdmv.cern.ch/mcm/chained_requests?contains=SMP-RunIIFall17NanoAODv5-00023&page=0&shown=15
echo '>>>>>>>>>>>>> set environment for GENSIM'
export SCRAM_ARCH=slc6_amd64_gcc630
source /cvmfs/cms.cern.ch/cmsset_default.sh
if [ -r CMSSW_9_3_9_patch1/src ] ; then 
 echo release CMSSW_9_3_9_patch1 already exists
else
scram p CMSSW CMSSW_9_3_9_patch1
fi
cd CMSSW_9_3_9_patch1/src
eval `scram runtime -sh`

curl -s --insecure https://cms-pdmv.cern.ch/mcm/public/restapi/requests/get_fragment/SMP-RunIIFall17wmLHEGS-00046 --retry 2 --create-dirs -o Configuration/GenProduction/python/SMP-RunIIFall17wmLHEGS-00046-fragment.py 
[ -s Configuration/GenProduction/python/SMP-RunIIFall17wmLHEGS-00046-fragment.py ] || exit $?;

scram b
cd ../../
seed=$(($(date +%s) % 100 + 1))
cmsDriver.py Configuration/GenProduction/python/SMP-RunIIFall17wmLHEGS-00046-fragment.py --fileout file:SMP-RunIIFall17wmLHEGS-00046.root --mc --eventcontent RAWSIM,LHE --datatier GEN-SIM,LHE --conditions 93X_mc2017_realistic_v3 --beamspot Realistic25ns13TeVEarly2017Collision --step LHE,GEN,SIM --geometry DB:Extended --era Run2_2017 --python_filename SMP-RunIIFall17wmLHEGS-00046_1_cfg.py --no_exec --customise Configuration/DataProcessing/Utils.addMonitoring --customise_commands process.RandomNumberGeneratorService.externalLHEProducer.initialSeed="int(${seed})" -n 130 || exit $? ; 

cp SMP-RunIIFall17wmLHEGS-00046_1_cfg.py SMP-RunIIFall17wmLHEGS-00046_1_cfg_LL.py
cp SMP-RunIIFall17wmLHEGS-00046_1_cfg.py SMP-RunIIFall17wmLHEGS-00046_1_cfg_LT.py
cp SMP-RunIIFall17wmLHEGS-00046_1_cfg.py SMP-RunIIFall17wmLHEGS-00046_1_cfg_TT.py
cp SMP-RunIIFall17wmLHEGS-00046_1_cfg.py SMP-RunIIFall17wmLHEGS-00046_1_cfg_TL.py

sed "s/^.*args = cms.vstring(.*$/    args = cms.vstring('..\/VBS_SSWW_LL_slc6_amd64_gcc630_CMSSW_9_3_16_tarball.tar.xz'),/" -i SMP-RunIIFall17wmLHEGS-00046_1_cfg_LL.py
sed "s/^.*args = cms.vstring(.*$/    args = cms.vstring('..\/VBS_SSWW_LT_slc6_amd64_gcc630_CMSSW_9_3_16_tarball.tar.xz'),/" -i SMP-RunIIFall17wmLHEGS-00046_1_cfg_LT.py
sed "s/^.*args = cms.vstring(.*$/    args = cms.vstring('..\/VBS_SSWW_TT_slc6_amd64_gcc630_CMSSW_9_3_16_tarball.tar.xz'),/" -i SMP-RunIIFall17wmLHEGS-00046_1_cfg_TT.py
sed "s/^.*args = cms.vstring(.*$/    args = cms.vstring('..\/VBS_SSWW_TL_slc6_amd64_gcc630_CMSSW_9_3_16_tarball.tar.xz'),/" -i SMP-RunIIFall17wmLHEGS-00046_1_cfg_TL.py

echo '>>>>>>>>>>>>> set environment for Premix'
export SCRAM_ARCH=slc6_amd64_gcc630
source /cvmfs/cms.cern.ch/cmsset_default.sh
if [ -r CMSSW_9_4_7/src ] ; then 
 echo release CMSSW_9_4_7 already exists
else
scram p CMSSW CMSSW_9_4_7
fi
cd CMSSW_9_4_7/src
eval `scram runtime -sh`


scram b
cd ../../
cmsDriver.py step1 --fileout file:SMP-RunIIFall17DRPremix-00068_step1.root  --pileup_input "dbs:/Neutrino_E-10_gun/RunIISummer17PrePremix-MCv2_correctPU_94X_mc2017_realistic_v9-v1/GEN-SIM-DIGI-RAW" --mc --eventcontent PREMIXRAW --datatier GEN-SIM-RAW --conditions 94X_mc2017_realistic_v11 --step DIGIPREMIX_S2,DATAMIX,L1,DIGI2RAW,HLT:2e34v40 --nThreads 8 --datamix PreMix --era Run2_2017 --python_filename SMP-RunIIFall17DRPremix-00068_1_cfg.py --no_exec --customise Configuration/DataProcessing/Utils.addMonitoring -n 1751 || exit $? ; 

cmsDriver.py step2 --filein file:SMP-RunIIFall17DRPremix-00068_step1.root --fileout file:SMP-RunIIFall17DRPremix-00068.root --mc --eventcontent AODSIM --runUnscheduled --datatier AODSIM --conditions 94X_mc2017_realistic_v11 --step RAW2DIGI,RECO,RECOSIM,EI --nThreads 8 --era Run2_2017 --python_filename SMP-RunIIFall17DRPremix-00068_2_cfg.py --no_exec --customise Configuration/DataProcessing/Utils.addMonitoring -n 1751 || exit $? ; 

echo '>>>>>>>>>>>>> set environment for MINIAODSIM'
export SCRAM_ARCH=slc6_amd64_gcc630
source /cvmfs/cms.cern.ch/cmsset_default.sh
if [ -r CMSSW_9_4_7/src ] ; then 
 echo release CMSSW_9_4_7 already exists
else
scram p CMSSW CMSSW_9_4_7
fi
cd CMSSW_9_4_7/src
eval `scram runtime -sh`


scram b
cd ../../
cmsDriver.py step1 --filein "dbs:/WpWpJJ_EWK_TuneCP5_13TeV-madgraph-pythia8/RunIIFall17DRPremix-PU2017_94X_mc2017_realistic_v11-v2/AODSIM" --fileout file:SMP-RunIIFall17MiniAODv2-00055.root --mc --eventcontent MINIAODSIM --runUnscheduled --datatier MINIAODSIM --conditions 94X_mc2017_realistic_v14 --step PAT --nThreads 4 --scenario pp --era Run2_2017,run2_miniAOD_94XFall17 --python_filename SMP-RunIIFall17MiniAODv2-00055_1_cfg.py --no_exec --customise Configuration/DataProcessing/Utils.addMonitoring -n 4800 || exit $? ; 

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
cmsDriver.py step1 --filein "dbs:/WpWpJJ_EWK_TuneCP5_13TeV-madgraph-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM" --fileout file:SMP-RunIIFall17NanoAODv5-00023.root --mc --eventcontent NANOAODSIM --datatier NANOAODSIM --conditions 102X_mc2017_realistic_v7 --step NANO --nThreads 2 --era Run2_2017,run2_nanoAOD_94XMiniAODv2 --python_filename SMP-RunIIFall17NanoAODv5-00023_1_cfg.py --no_exec --customise Configuration/DataProcessing/Utils.addMonitoring -n 10000 || exit $? ; 
sed '/process.NANOAODSIMoutput = cms.OutputModule("NanoAODOutputModule",/a\    fakeNameForCrab =cms.untracked.bool(True),' -i SMP-RunIIFall17NanoAODv5-00023_1_cfg.py