# CMSSWGeneration

Instructions on how to generate a private sample using crab in CMSSW 

Assumptions:

- LHE are available
- premixed library is available




Prepare to get premix library:

    voms-proxy-init -voms cms -rfc

LHE:

    example: /afs/cern.ch/user/g/govoni/myeos/samples/2019_EFT/SSeu/SM_limit/SSeu_SMlimit_results/1441466/SSeu_SMlimit_3/unweighted_events.lhe
    
    

Produce (from RunTheMatrix):

    # in: /afs/cern.ch/work/a/amassiro/ECAL/SIM/ToRebase/CMSSW_11_0_X_2019-10-06-2300/src dryRun for 'cd 250202.172_TTbar_13UP17+TTbar_13UP17+DIGIPRMXUP17_PU25_RD+RECOPRMXUP17_PU25+HARVESTUP17_PU25
    cmsDriver.py TTbar_13TeV_TuneCUETP8M1_cfi  --conditions auto:phase1_2017_realistic -n 10 --era Run2_2017 --eventcontent FEVTDEBUG --relval 9000,50 -s GEN,SIM --datatier GEN-SIM --beamspot Realistic25ns13TeVEarly2017Collision --io TTbar_13UP17.io --python TTbar_13UP17.py --fileout file:step1.root  --nThreads 8 > step1_TTbar_13UP17+TTbar_13UP17+DIGIPRMXUP17_PU25_RD+RECOPRMXUP17_PU25+HARVESTUP17_PU25.log  2>&1
    
    
    #    in: /afs/cern.ch/work/a/amassiro/ECAL/SIM/ToRebase/CMSSW_11_0_X_2019-10-06-2300/src dryRun for 'cd 250202.172_TTbar_13UP17+TTbar_13UP17+DIGIPRMXUP17_PU25_RD+RECOPRMXUP17_PU25+HARVESTUP17_PU25
    cmsDriver.py step2  --datamix PreMix --conditions auto:phase1_2017_realistic --pileup_input das:/RelValPREMIXUP17_PU25/CMSSW_10_6_0-PU25ns_106X_mc2017_realistic_v3-v1/PREMIX --era Run2_2017 --procModifiers premix_stage2 -s DIGI:pdigi_valid,DATAMIX,L1,DIGI2RAW,HLT:@relval2017 --datatier GEN-SIM-DIGI-RAW-HLTDEBUG --eventcontent FEVTDEBUGHLT --io DIGIPRMXUP17_PU25_RD.io --python DIGIPRMXUP17_PU25_RD.py -n 100  --filein  file:step1.root  --fileout file:step2.root  --nThreads 8 > step2_TTbar_13UP17+TTbar_13UP17+DIGIPRMXUP17_PU25_RD+RECOPRMXUP17_PU25+HARVESTUP17_PU25.log  2>&1
    
    
    #    in: /afs/cern.ch/work/a/amassiro/ECAL/SIM/ToRebase/CMSSW_11_0_X_2019-10-06-2300/src dryRun for 'cd 250202.172_TTbar_13UP17+TTbar_13UP17+DIGIPRMXUP17_PU25_RD+RECOPRMXUP17_PU25+HARVESTUP17_PU25
    cmsDriver.py step3  --conditions auto:phase1_2017_realistic -n 10 --era Run2_2017 --eventcontent RECOSIM,MINIAODSIM,DQM --runUnscheduled  --procModifiers premix_stage2 -s RAW2DIGI,L1Reco,RECO,RECOSIM,EI,PAT,VALIDATION:@standardValidationNoHLT+@miniAODValidation,DQM:@standardDQMFakeHLT+@miniAODDQM --datatier GEN-SIM-RECO,MINIAODSIM,DQMIO --io RECOPRMXUP17_PU25.io --python RECOPRMXUP17_PU25.py --filein  file:step2.root  --fileout file:step3.root  --nThreads 8 > step3_TTbar_13UP17+TTbar_13UP17+DIGIPRMXUP17_PU25_RD+RECOPRMXUP17_PU25+HARVESTUP17_PU25.log  2>&1
    
    
    #    in: /afs/cern.ch/work/a/amassiro/ECAL/SIM/ToRebase/CMSSW_11_0_X_2019-10-06-2300/src dryRun for 'cd 250202.172_TTbar_13UP17+TTbar_13UP17+DIGIPRMXUP17_PU25_RD+RECOPRMXUP17_PU25+HARVESTUP17_PU25
    cmsDriver.py step4  --conditions auto:phase1_2017_realistic -s HARVESTING:@standardValidationNoHLT+@standardDQMFakeHLT+@miniAODValidation+@miniAODDQM --filetype DQM --geometry DB:Extended --era Run2_2017 --mc  --io HARVESTUP17_PU25.io --python HARVESTUP17_PU25.py -n 100  --filein file:step3_inDQM.root --fileout file:step4.root  > step4_TTbar_13UP17+TTbar_13UP17+DIGIPRMXUP17_PU25_RD+RECOPRMXUP17_PU25+HARVESTUP17_PU25.log  2>&1

    


    
