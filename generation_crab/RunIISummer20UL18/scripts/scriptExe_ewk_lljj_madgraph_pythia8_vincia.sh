#!/bin/bash                                                                                                                                                                                       
set -e
BASE=$PWD
RELEASE_BASE=$CMSSW_BASE
source /cvmfs/cms.cern.ch/cmsset_default.sh
cd $RELEASE_BASE/src
eval `scram runtime -sh`

## installation pythia8 last version
curl -s --insecure https://pythia.org/download/pythia83/pythia8306.tgz -retry 2 --create-dirs -o  pythia8306.tgz 
tar xfz pythia8306.tgz 
rm pythia8306.tgz
cd pythia8306/    
hepmc=$(scram tool info hepmc | grep HEPMC_BASE | sed -e "s/HEPMC_BASE=//g")
lhapdf=$(scram tool info lhapdf | grep LHAPDF_BASE | sed -e "s/LHAPDF_BASE=//g")
./configure --enable-shared  --with-hepmc2=$hepmc --with-lhapdf6=$lhapdf 
make -j 4
export PYTHIA_BASE=$PWD 
cd ..
path_to_replace=$(scram tool info pythia8 | grep PYTHIA8_BASE | sed -e "s/PYTHIA8_BASE=//g")
scp $RELEASE_BASE/config/toolbox/$SCRAM_ARCH/tools/selected/pythia8.xml ./
sed -i "s|$path_to_replace|$PYTHIA_BASE|g"  pythia8.xml
mv pythia8.xml $RELEASE_BASE/config/toolbox/$SCRAM_ARCH/tools/selected/
scram setup pythia8
## update pythia8 interface for vincia
scp -r $BASE/GeneratorInterface.tar.gz ./ 
tar xfz GeneratorInterface.tar.gz
scram b -j 4
cd $BASE

echo "cmsRun -e -j FrameworkJobReport.xml EWK_LLJJ_MLL_50_MJJ_120_TuneCP5_13TeV_madgraph_pythia8_vincia_cfg.py jobNum="$1" "$2" "$3" outputName=lheGenStep_"$1".root"
cmsRun -e -j FrameworkJobReport.xml EWK_LLJJ_MLL_50_MJJ_120_TuneCP5_13TeV_madgraph_pythia8_vincia_cfg.py jobNum=$1 $2 $3 outputName=lheGenStep"_"$1.root

echo "cmsRun -e -j FrameworkJobReport.xml SIM_step_cfg.py "$3" inputName=lheGenStep_"$1".root outputName=simStep_"$1".root"
cmsRun -e -j FrameworkJobReport.xml SIM_step_cfg.py $3 inputName=lheGenStep_$1.root outputName=simStep_$1.root
rm lheGenStep"_"$1.root

echo "cmsRun -e -j FrameworkJobReport.xml DIGI_RAW_premix_step_cfg.py "$3" inputName=simStep_"$1".root outputName=digiRawStep_"$1".root"
cmsRun -e -j FrameworkJobReport.xml DIGI_RAW_premix_step_cfg.py $3 inputName=simStep_$1.root outputName=digiRawStep_$1.root
rm simStep"_"$1.root

scram p CMSSW CMSSW_10_2_16_UL
cd CMSSW_10_2_16_UL/src
eval `scram runtime -sh`
cd ../../

echo "cmsRun -e -j FrameworkJobReport.xml HLT_step_cfg.py "$3" inputName=digiRawStep_"$1".root outputName=hltStep_"$1".root"
cmsRun -e -j FrameworkJobReport.xml HLT_step_cfg.py $3 inputName=digiRawStep_$1.root outputName=hltStep_$1.root
rm digiRawStep"_"$1.root

cd $RELEASE_BASE
eval `scram runtime -sh`
cd $BASE

echo "cmsRun -e -j FrameworkJobReport.xml RECO_step_cfg.py "$3" inputName=hltStep_"$1".root outputName=recoStep_"$1".root"
cmsRun -e -j FrameworkJobReport.xml RECO_step_cfg.py $3 inputName=hltStep_$1.root outputName=recoStep_$1.root
rm hltStep"_"$1.root

echo "cmsRun -e -j FrameworkJobReport.xml MINIAOD_step_cfg.py "$3" inputName=recoStep_"$1".root outputName=miniAODStep_"$1".root"
cmsRun -e -j FrameworkJobReport.xml MINIAOD_step_cfg.py $3 inputName=recoStep_$1.root outputName=miniAODStep_$1.root
rm recoStep"_"$1.root

echo "cmsRun -e -j FrameworkJobReport.xml NANOAODv9_step_cfg.py "$3" inputName=miniAODStep_"$1".root "$4
cmsRun -e -j FrameworkJobReport.xml NANOAODv9_step_cfg.py $3 inputName=miniAODStep_$1.root $4
