#### Environment settings
Log on `lxplus6` firstly, then clone this repository:
~~~
git clone git@github.com:UniMiBAnalyses/CMSSWGeneration.git
cd CMSSWGeneration/private_production/polarization
~~~
But before setting environment, do:
~~~
voms-proxy-init --voms cms -rfc
~~~
Choose one year, e.g. 2018. You will find environment setting file `env2018.sh`, just run:
~~~
source env2018.sh
~~~
Then you will have related cfg files for each step and related CMSSW.

#### Submit crab jobs
Now you are able to submit crab jobs for each step. In order to get NANOAODSIM, we need 5 steps.

1. GEN-SIM
    - Put correct gridpack behind `config.JobType.inputFiles` in crab config files.
    - How to generate gridpack? Please find [here](https://twiki.cern.ch/twiki/bin/view/Main/Dim6VBSproduction).
    - Also remember to change `config.Site.storageSite`.
    ~~~
    crab submit -c crab_LL_LHE.py
    crab submit -c crab_LT_LHE.py
    crab submit -c crab_TT_LHE.py
    crab submit -c crab_TL_LHE.py
    ~~~
2. GEN-SIM-RAW
    - Use `crab status` to get the outputs of step1,then put behind `config.Data.inputDataset` in crab config files.
    - Remember to change `config.Site.storageSite`.
    ~~~
    crab submit -c crab_LL_Premix_1.py
    crab submit -c crab_LT_Premix_1.py
    crab submit -c crab_TT_Premix_1.py
    crab submit -c crab_TL_Premix_1.py
    ~~~
3. AODSIM
    - Use `crab status` to get the outputs of step2,then put behind `config.Data.inputDataset` in crab config files.
    - Remember to change `config.Site.storageSite`.
    ~~~
    crab submit -c crab_LL_Premix_2.py
    crab submit -c crab_LT_Premix_2.py
    crab submit -c crab_TT_Premix_2.py
    crab submit -c crab_TL_Premix_2.py
    ~~~
4. MINIAODSIM
    - Use `crab status` to get the outputs of step3,then put behind `config.Data.inputDataset` in crab config files.
    - Remember to change `config.Site.storageSite`.
    ~~~
    crab submit -c crab_LL_MINIAODSIM.py
    crab submit -c crab_LT_MINIAODSIM.py
    crab submit -c crab_TT_MINIAODSIM.py
    crab submit -c crab_TL_MINIAODSIM.py
    ~~~
5. NANOAODSIM
    - Use `crab status` to get the outputs of step4,then put behind `config.Data.inputDataset` in crab config files.
    - Remember to change `config.Site.storageSite`.
    ~~~
    crab submit -c crab_LL_NANOAODSIM.py
    crab submit -c crab_LT_NANOAODSIM.py
    crab submit -c crab_TT_NANOAODSIM.py
    crab submit -c crab_TL_NANOAODSIM.py
    ~~~
Be aware that each step need specific version of CMSSW, which could be found in env2018.sh 