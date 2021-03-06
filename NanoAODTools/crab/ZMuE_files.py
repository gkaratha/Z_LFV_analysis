
Run2018B={"Name":"Run2018B","Path":"/SingleMuon/Run2018B-UL2018_MiniAODv2_NanoAODv9-v2/NANOAOD","Units":"1","Data":True}
Run2018C={"Name":"Run2018C","Path":"/SingleMuon/Run2018C-UL2018_MiniAODv2_NanoAODv9-v2/NANOAOD","Units":"1","Data":True}
Run2018D={"Name":"Run2018D","Path":"/SingleMuon/Run2018D-UL2018_MiniAODv2_NanoAODv9-v1/NANOAOD","Units":"1","Data":True}


SgnZMuE={"Name":"SgnZMuE","Path":"/LFVAnalysis_ZEMu_2018_10218V1/pellicci-LFVAnalysis_NANOAOD_10218V1-a7880b551d3b12f0ed185e04212304eb/USER","Units":"5","Data":False,"GenZMuE":True,"Phys3":True}


samples_in=[Run2018B,Run2018C,Run2018D,SgnZMuE]


optional_keys=["GenZMuE","GenZMuTau","GenZETau","Phys3","Lumibased"]
samples_out=[]
for sample in samples_in:
  for key in optional_keys:
     if key not in sample.keys():
        sample[key]=False
  samples_out.append(sample)



'''
SgnZMuE2:/LFVAnalysis_ZEMu_2017_934V2/pellicci-LFVAnalysis_NANOAOD_10218V2-df769e3b6a68f1e897c86e71b2345849/USER
SgnZMuE3:/LFVAnalysis_ZEMu_2017_934V1/pellicci-LFVAnalysis_NANOAOD_10218V1-df769e3b6a68f1e897c86e71b2345849/USER
SgnZMuE4:/ZEMuAnalysis_10218V2/pellicci-ZEMuAnalysis_NANOAOD_10218V1-a7880b551d3b12f0ed185e04212304eb/USER
SgnZMuE5:/ZEMuAnalysis_2017_934V1/pellicci-ZEMuAnalysis_NANOAOD_2017_10218V1-df769e3b6a68f1e897c86e71b2345849/USER
SgnZMuE6:/ZEMuAnalysis_2017_934V1/pellicci-ZEMuAnalysis_NANOAOD_2017_10218V2-df769e3b6a68f1e897c86e71b2345849/USER
SgnCentral:/LFV_ZToLL_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v2/NANOAODSIM
SgnCentral2:/LFV_ZToLL_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL18NanoAODv2-106X_upgrade2018_realistic_v15_L1v1-v1/NANOAODSIM
SgnCentral3:/LFV_ZToLL_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v2/NANOAODSIM
SgnCentral4:/LFV_ZToLL_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL17NanoAODv2-106X_mc2017_realistic_v8-v1/NANOAODSIM


SgnZMuTau:/LFVAnalysis_ZMuTau_2018_10218V1/pellicci-LFVAnalysis_NANOAOD_10218V1-a7880b551d3b12f0ed185e04212304eb/USER
SgnZETau:/LFVAnalysis_ZETau_2018_10218V1/pellicci-LFVAnalysis_NANOAOD_10218V1-a7880b551d3b12f0ed185e04212304eb/USER


#:TT:Background
BkgTT2l:/TTTo2L2Nu_TuneCP5_13TeV-powheg-pythia8/RunIIAutumn18NanoAODv7-Nano02Apr2020_102X_upgrade2018_realistic_v21-v1/NANOAODSIM
BkgTTsemiLep:/TTToSemiLeptonic_TuneCP5_13TeV-powheg-pythia8/RunIIAutumn18NanoAODv7-Nano02Apr2020_102X_upgrade2018_realistic_v21_ext3-v1/NANOAODSIM
BkgTThadronic:/TTToHadronic_TuneCP5_13TeV-powheg-pythia8/RunIIAutumn18NanoAODv7-Nano02Apr2020_102X_upgrade2018_realistic_v21_ext2-v1/NANOAODSIM

#:TW:Background
BkgTW:/ST_tW_top_5f_inclusiveDecays_TuneCP5_13TeV-powheg-pythia8/RunIIAutumn18NanoAODv7-Nano02Apr2020_102X_upgrade2018_realistic_v21_ext1-v1/NANOAODSIM
BkgAntiTW:/ST_tW_antitop_5f_inclusiveDecays_TuneCP5_13TeV-powheg-pythia8/RunIIAutumn18NanoAODv7-Nano02Apr2020_102X_upgrade2018_realistic_v21_ext1-v1/NANOAODSIM'

#:W:Background
BkgWJets:/WJetsToLNu_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIAutumn18NanoAODv7-Nano02Apr2020_102X_upgrade2018_realistic_v21-v1/NANOAODSIM
BkgWW2l:/WWTo2L2Nu_NNPDF31_TuneCP5_13TeV-powheg-pythia8/RunIIAutumn18NanoAODv7-Nano02Apr2020_102X_upgrade2018_realistic_v21-v1/NANOAODSIM
BkgWW2q:/WWToLNuQQ_NNPDF31_TuneCP5_13TeV-powheg-pythia8/RunIIAutumn18NanoAODv7-Nano02Apr2020_102X_upgrade2018_realistic_v21-v1/NANOAODSIM
BkgWWW:/WWW_4F_TuneCP5_13TeV-amcatnlo-pythia8/RunIIAutumn18NanoAODv7-Nano02Apr2020_102X_upgrade2018_realistic_v21_ext1-v1/NANOAODSIM

#Z:Background
BkgDYJets:/DYJetsToLL_M-50_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIIAutumn18NanoAODv7-Nano02Apr2020_102X_upgrade2018_realistic_v21-v1/NANOAODSIM
BkgDYJets2:/DYJetsToLL_M-50_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIIAutumn18NanoAODv7-Nano02Apr2020_102X_upgrade2018_realistic_v21_ext2-v1/NANOAODSIM
BkgDYMuEJets:/DYJetsToTauTau_ForcedMuEleDecay_M-50_TuneCP5_PSweights_13TeV-amcatnloFXFX-pythia8/RunIIAutumn18NanoAODv7-Nano02Apr2020_EXT_102X_upgrade2018_realistic_v21-v1/NANOAODSIM
BkgDYMuEJets2:/DYJetsToTauTau_ForcedMuEleDecay_M-50_TuneCP5_PSweights_13TeV-amcatnloFXFX-pythia8/RunIIAutumn18NanoAODv7-Nano02Apr2020_102X_upgrade2018_realistic_v21_ext1-v1/NANOAODSIM
BkgWZ:/WZ_TuneCP5_13TeV-pythia8/RunIIAutumn18NanoAODv7-Nano02Apr2020_102X_upgrade2018_realistic_v21-v1/NANOAODSIM
BkgZZ:/ZZ_TuneCP5_13TeV-pythia8/RunIIAutumn18NanoAODv7-Nano02Apr2020_102X_upgrade2018_realistic_v21-v1/NANOAODSIM

#:QCD:Background
BkgQCD30to40:/QCD_Pt-30toInf_DoubleEMEnriched_MGG-40to80_TuneCP5_13TeV_Pythia8/RunIIAutumn18NanoAODv7-Nano02Apr2020_102X_upgrade2018_realistic_v21-v1/NANOAODSIM
BkgQCD40toInf:/QCD_Pt-40toInf_DoubleEMEnriched_MGG-80toInf_TuneCP5_13TeV_Pythia8/RunIIAutumn18NanoAODv7-Nano02Apr2020_102X_upgrade2018_realistic_v21-v1/NANOAODSIM
BkgQCDMu15:/QCD_Pt-20toInf_MuEnrichedPt15_TuneCUETP8M1_13TeV_pythia8/RunIISummer16NanoAODv7-PUMoriond17_Nano02Apr2020_102X_mcRun2_asymptotic_v8-v1/NANOAODSIM
'''
