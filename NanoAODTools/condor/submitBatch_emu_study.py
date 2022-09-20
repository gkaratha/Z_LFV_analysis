#! /usr/bin/env python
import PhysicsTools.NanoAODTools.condor.BatchMaster as bm

import os, sys

dryRun = False

# -----------------------------
# Specify parameters
# -----------------------------

executable = 'execBatch_emu_study.sh'
analyzer   = 'EmbeddingEMuAnalyzer'
stage_dir  = 'batch'
output_dir = '/store/user/mimacken/emu_study'
location   = 'lpc'



# -----------------------------
# Set job configurations.  
# -----------------------------
samplesDict = {}



nEvtPerJob = 8 # faster jobs, # in unit of 1e6 , 5-10 are good settings. 


#################################################
#                                               #
#---------- Running Embedded Samples -----------#
#                                               #
#################################################

### redefine N(events/job) for embedding ###
nEvtPerJob = 0.5 #~25k events per file, ~50-100 files per dataset --> ~5-10 jobs/dataset

# 2016 Embedded samples
samplesDict['2016_embed_emu'] = [
    bm.JobConfig(
        dataset='/EmbeddingRun2016B/pellicci-EmbeddedElMu_NANOAOD_10222V2-eb4bd41e0cecc0e67477f0cf9aac775c/USER',
        nEvtPerJobIn1e6=nEvtPerJob, year="2016", isData=False, suffix='EMuStudy_Embed-EMu-B_2016', inputDBS="phys03"),
    bm.JobConfig(
        dataset='/EmbeddingRun2016C/pellicci-EmbeddedElMu_NANOAOD_10222V2-eb4bd41e0cecc0e67477f0cf9aac775c/USER',
        nEvtPerJobIn1e6=nEvtPerJob, year="2016", isData=False, suffix='EMuStudy_Embed-EMu-C_2016', inputDBS="phys03"),
    bm.JobConfig(
        dataset='/EmbeddingRun2016D/pellicci-EmbeddedElMu_NANOAOD_10222V2-eb4bd41e0cecc0e67477f0cf9aac775c/USER',
        nEvtPerJobIn1e6=nEvtPerJob, year="2016", isData=False, suffix='EMuStudy_Embed-EMu-D_2016', inputDBS="phys03"),
    bm.JobConfig(
        dataset='/EmbeddingRun2016E/pellicci-EmbeddedElMu_NANOAOD_10222V2-eb4bd41e0cecc0e67477f0cf9aac775c/USER',
        nEvtPerJobIn1e6=nEvtPerJob, year="2016", isData=False, suffix='EMuStudy_Embed-EMu-E_2016', inputDBS="phys03"),
    bm.JobConfig(
        dataset='/EmbeddingRun2016F/pellicci-EmbeddedElMu_NANOAOD_10222V2-eb4bd41e0cecc0e67477f0cf9aac775c/USER',
        nEvtPerJobIn1e6=nEvtPerJob, year="2016", isData=False, suffix='EMuStudy_Embed-EMu-F_2016', inputDBS="phys03"),
    bm.JobConfig(
        dataset='/EmbeddingRun2016G/pellicci-EmbeddedElMu_NANOAOD_10222V2-eb4bd41e0cecc0e67477f0cf9aac775c/USER',
        nEvtPerJobIn1e6=nEvtPerJob, year="2016", isData=False, suffix='EMuStudy_Embed-EMu-G_2016', inputDBS="phys03"),
    bm.JobConfig(
        dataset='/EmbeddingRun2016H/pellicci-EmbeddedElMu_NANOAOD_10222V2-eb4bd41e0cecc0e67477f0cf9aac775c/USER',
        nEvtPerJobIn1e6=nEvtPerJob, year="2016", isData=False, suffix='EMuStudy_Embed-EMu-H_2016', inputDBS="phys03"),

]

# 2017 Embedded samples
samplesDict['2017_embed_emu'] = [
    bm.JobConfig(
        dataset='/EmbeddingRun2017B/pellicci-EmbeddedElMu_NANOAOD_10222V1-6e995938c955340423734eed12836829/USER',
        nEvtPerJobIn1e6=nEvtPerJob, year="2017", isData=False, suffix='EMuStudy_Embed-EMu-B_2017', inputDBS="phys03"),
    bm.JobConfig(
        dataset='/EmbeddingRun2017C/pellicci-EmbeddedElMu_NANOAOD_10222V1-6e995938c955340423734eed12836829/USER',
        nEvtPerJobIn1e6=nEvtPerJob, year="2017", isData=False, suffix='EMuStudy_Embed-EMu-C_2017', inputDBS="phys03"),
    bm.JobConfig(
        dataset='/EmbeddingRun2017D/pellicci-EmbeddedElMu_NANOAOD_10222V1-6e995938c955340423734eed12836829/USER',
        nEvtPerJobIn1e6=nEvtPerJob, year="2017", isData=False, suffix='EMuStudy_Embed-EMu-D_2017', inputDBS="phys03"),
    bm.JobConfig(
        dataset='/EmbeddingRun2017E/pellicci-EmbeddedElMu_NANOAOD_10222V1-6e995938c955340423734eed12836829/USER',
        nEvtPerJobIn1e6=nEvtPerJob, year="2017", isData=False, suffix='EMuStudy_Embed-EMu-E_2017', inputDBS="phys03"),
    bm.JobConfig(
        dataset='/EmbeddingRun2017F/pellicci-EmbeddedElMu_NANOAOD_10222V1-6e995938c955340423734eed12836829/USER',
        nEvtPerJobIn1e6=nEvtPerJob, year="2017", isData=False, suffix='EMuStudy_Embed-EMu-F_2017', inputDBS="phys03"),
]

# 2018 Embedded samples
samplesDict['2018_embed_emu'] = [
    bm.JobConfig(
        dataset='/EmbeddingRun2018A/pellicci-EmbeddedElMu_NANOAOD_2018_10222V1-9b11f648cb233dc346c2d0860bbea8f9/USER',
        nEvtPerJobIn1e6=nEvtPerJob, year="2018", isData=False, suffix='EMuStudy_Embed-EMu-A_2018', inputDBS="phys03"),
    bm.JobConfig(
        dataset='/EmbeddingRun2018B/pellicci-EmbeddedElMu_NANOAOD_2018_10222V1-9b11f648cb233dc346c2d0860bbea8f9/USER',
        nEvtPerJobIn1e6=nEvtPerJob, year="2018", isData=False, suffix='EMuStudy_Embed-EMu-B_2018', inputDBS="phys03"),
    bm.JobConfig(
        dataset='/EmbeddingRun2018C/pellicci-EmbeddedElMu_NANOAOD_2018_10222V1-9b11f648cb233dc346c2d0860bbea8f9/USER',
        nEvtPerJobIn1e6=nEvtPerJob, year="2018", isData=False, suffix='EMuStudy_Embed-EMu-C_2018', inputDBS="phys03"),
    bm.JobConfig(
        dataset='/EmbeddingRun2018D/pellicci-EmbeddedElMu_NANOAOD_2018_10222V1-e181eeebc101019f884cba30e429f851/USER',
        nEvtPerJobIn1e6=nEvtPerJob, year="2018", isData=False, suffix='EMuStudy_Embed-EMu-D_2018', inputDBS="phys03"),
]

#################################################
#                                               #
#------------- Running MC Samples --------------#
#                                               #
#################################################

### redefine N(events/job) for MC ###
nEvtPerJob = 5

samplesDict['2016_z'] = [
    bm.JobConfig(
        dataset='/DYJetsToLL_M-50_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/RunIISummer16NanoAODv7-PUMoriond17_Nano02Apr2020_102X_mcRun2_asymptotic_v8_ext2-v1/NANOAODSIM',
        nEvtPerJobIn1e6=nEvtPerJob, year="2016", isData=False, suffix='EMuStudy_DY50_2016'),
]
samplesDict['2017_z'] = [
    bm.JobConfig(
        dataset='/DYJetsToLL_M-50_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIIFall17NanoAODv7-PU2017_12Apr2018_Nano02Apr2020_102X_mc2017_realistic_v8_ext3-v1/NANOAODSIM',
        nEvtPerJobIn1e6=nEvtPerJob, year="2017", isData=False, suffix='EMuStudy_DY50_2017'),    
]
samplesDict['2018_z'] = [
    bm.JobConfig(
        dataset='/DYJetsToLL_M-50_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIIAutumn18NanoAODv7-Nano02Apr2020_102X_upgrade2018_realistic_v21_ext2-v1/NANOAODSIM',
        nEvtPerJobIn1e6=nEvtPerJob, year="2018", isData=False, suffix='EMuStudy_DY50_2018'),
]

# -----------------------------
# submit to batch
# -----------------------------

samplesToSubmit = samplesDict.keys()
samplesToSubmit.sort()
# samplesToSubmit = ["2018_embed_emu"]

# doYears = ["2016", "2017", "2018"]
doYears = ["2018"]
configs = []

for s in samplesToSubmit:
    if s[:4] in doYears:
        configs += samplesDict[s]

batchMaster = bm.BatchMaster(
    analyzer    = analyzer,
    config_list = configs, 
    stage_dir   = stage_dir,
    output_dir  = output_dir,
    executable  = executable,
    location    = location
)

#ensure there's a symbolic link 'batch' to put the tarball in
if not os.path.exists("batch") :
    if not os.path.exists("~/nobackup/batch") :
        os.makedirs("~/nobackup/batch")
    os.symlink("~/nobackup/batch", "batch")
    print "Created symbolic link to ~/nobackup/batch"

if configs == []:
    print "No jobs to submit!\n"
else :
    batchMaster.submit_to_batch(doSubmit=(not dryRun))
