#!/bin/bash                                                                                                                                                                                       
set -e
BASE=$PWD
RELEASE_BASE=$CMSSW_BASE

source /cvmfs/cms.cern.ch/cmsset_default.sh

cd $RELEASE_BASE
eval `scram runtime -sh`
cd $BASE

echo "cmsRun -e -j FrameworkJobReport.xml EWK_LLJJ_MLL-50_MJJ-120_TuneCP5_13TeV-madgraph-pythia8_dipole_cfg.py jobNum="$1" "$2" "$3" outputName=lheGenStep_"$1".root"
#cmsRun -e -j FrameworkJobReport.xml EWK_LLJJ_MLL-50_MJJ-120_TuneCP5_13TeV-madgraph-pythia8_dipole_cfg.py jobNum=$1 $2 $3 outputName=lheGenStep"_"$1.root

echo "cmsRun -e -j FrameworkJobReport.xml SIM_step_cfg.py "$3" inputName=lheGenStep_"$1".root outputName=simStep_"$1".root"
#cmsRun -e -j FrameworkJobReport.xml SIM_step_cfg.py $3 inputName=lheGenStep_$1.root outputName=simStep_$1.root
#rm lheGenStep"_"$1.root

echo "cmsRun -e -j FrameworkJobReport.xml DIGI_RAW_premix_step_cfg.py "$3" inputName=simStep_"$1".root outputName=digiRawStep_"$1".root"
#cmsRun -e -j FrameworkJobReport.xml DIGI_RAW_premix_step_cfg.py $3 inputName=simStep_$1.root outputName=digiRawStep_$1.root
#rm simStep"_"$1.root

scram p CMSSW CMSSW_10_2_16_UL
cd CMSSW_10_2_16_UL/src
eval `scram runtime -sh`
cd ../../

echo "cmsRun -e -j FrameworkJobReport.xml HLT_step_cfg.py "$3" inputName=digiRawStep_"$1".root outputName=hltStep_"$1".root"
#cmsRun -e -j FrameworkJobReport.xml HLT_step_cfg.py $3 inputName=digiRawStep_$1.root outputName=hltStep_$1.root
#rm digiRawStep"_"$1.root

cd $RELEASE_BASE
eval `scram runtime -sh`
cd $BASE

echo "cmsRun -e -j FrameworkJobReport.xml RECO_step_cfg.py "$3" inputName=hltStep_"$1".root outputName=recoStep_"$1".root"
#cmsRun -e -j FrameworkJobReport.xml RECO_step_cfg.py $3 inputName=hltStep_$1.root outputName=recoStep_$1.root
#rm hltStep"_"$1.root

echo "cmsRun -e -j FrameworkJobReport.xml MINIAOD_step_cfg.py "$3" inputName=recoStep_"$1".root outputName=miniAODStep_"$1".root"
#cmsRun -e -j FrameworkJobReport.xml MINIAOD_step_cfg.py $3 inputName=recoStep_$1.root outputName=miniAODStep_$1.root
#rm recoStep"_"$1.root

echo "cmsRun -e -j FrameworkJobReport.xml NANOAODv9_step_cfg.py "$3" inputName=miniAODStep_"$1".root "$4
#cmsRun -e -j FrameworkJobReport.xml NANOAODv9_step_cfg.py $3 inputName=miniAODStep_$1.root $4
