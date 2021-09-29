# Authors and contacts:
# Guillaume Albouy: guillaume.albouy@etu.univ-grenoble-alpes.fr
# Akanksha Singh: akki153209@gmail.com
# Harikrishnan Nair: hunair1996@gmail.com

# This code needs helpers.py and histo_defs.py which are stored in the same folder as this file
# Following cuts on events are assumed
# jet1.PT > 500 and np.abs(jet1.Eta) < 2.5 and jet2.PT > 500 and np.abs(jet2.Eta) < 2.5
# We assume that different branches corresponding to different jet radii are defined in root files
# In this code jet clustering radius is fixed to 1.4, can be changed at line 52
# This code will analyse input sample and create following reconstructed level normalized distributions:
# 1) pt of leading/subleading jet
# 2) dijet invarint mass
# 3) missing energy
# 4) transverse mass of dijet and met system
# 5) transverse ratio
# 6) delta phi between missin energy and leading/subleading jet
# 7) 2D histo of track pT of leading jet
# 8) delta eta between leading and subleading jet
# 9) pt and invariant mass for trimmed and SoftDropped leading/subleading jets
#
# command: python /path_of_code/transverse_mass.py /path_of_rootfile/name_of_rootfile.root /path_of_rootfile/output_name.root
# Takes the rootfile as input and computes the defined variables and fills the respective histograms.

import sys
import numpy as np
import ROOT
from array import array
from helpers import *


try:
  input = raw_input
except:
  pass

if len(sys.argv) < 3:
  print(" Usage: Analysis_code/Jet_analysis.py /path/delphes_file.root /path/output.root")
  sys.exit(1)

ROOT.gSystem.Load("libDelphes")

try:
        ROOT.gInterpreter.Declare('#include "classes/DelphesClasses.h"')
        ROOT.gInterpreter.Declare('#include "external/ExRootAnalysis/ExRootTreeReader.h"')
except:
        pass

# Parameters
############################################
# Radius of jets (0.4, 1.0, 1.4) :
R = 1.4
# Events selection (pT in GeV)
pT_min_jet1 = 500
pT_min_jet2 = 500
eta_max = 2.5
M_PI = 3.14
############################################

inputFile = sys.argv[1]
print("Input file :")
print(inputFile)

outputFile = sys.argv[2]
print("output file :")
print(outputFile)

# Create chain of root trees
chain = ROOT.TChain("Delphes")
chain.Add(inputFile)

# Create object of class ExRootTreeReader
treeReader = ROOT.ExRootTreeReader(chain)
numberOfEntries = treeReader.GetEntries()

# Get pointer to branches used in this analysis
# R-jet branches : 04, 08, 10, 12, 14
R_jet = str(int(R*10))
if R<1.0: R_jet = '0' + R_jet

# Getting the required branches from Delphes ROOT file.
branchJet = treeReader.UseBranch("ParticleFlowJet%s"%R_jet)
branchMET = treeReader.UseBranch("MissingET")
branchtrack = treeReader.UseBranch("Track")

# Book histograms

Nbins = 150
hist1Jet1PT = ROOT.TH1F("jet1_pt", "Lead jet p_{T} with R=%.1f;p_{T} GeV;A.U."%(R), Nbins, 0.0, 2000.0)
hist1Jet2PT = ROOT.TH1F("jet2_pt", "Sub jet p_{T} with R=%.1f;p_{T} GeV;A.U."%(R), Nbins, 0.0, 2000.0)
histMET = ROOT.TH1F("jet_met", "Missing transverse energy;MET GeV;A.U.", Nbins, .0, 3000.0)
hist1JetmJJ = ROOT.TH1F("jet_mJJ", " Invariant mass m_{JJ} with R=%.1f;m_{JJ} GeV;A.U."%(R), Nbins, 0.0, 3500.0)

Nbins = 40
hist1Jet1Ntrk = ROOT.TH1F("jet1_ntrk", "Lead jet N_{trk} with R=%.1f;N_{trk};A.U."%(R), Nbins, .0, 170.0)
hist1Jet2Ntrk = ROOT.TH1F("jet2_ntrk", "Sub jet N_{trk} with R=%.1f;N_{trk};A.U."%(R), Nbins, .0, 170.0)

Nbins = 150
hmt = ROOT.TH1F("jet_met_mt" , "Transverse mass of jet + MET" , Nbins, 0.0 , 3000.0)

Nbins = 50
hdphi1 = ROOT.TH1F("dPhi1", "dPhi_jet1_met", Nbins, 0.0, 10.0)
hdphi2 = ROOT.TH1F("dPhi2", "dPhi_jet2_met", Nbins, 0.0, 10.0)

Nbins = 100
hrt = ROOT.TH1F("jet_met_rt" , "Transverse ratio of jet + MET" , Nbins, 0.0 , 1.0)

Nbins = 150
hist2Jet1PT = ROOT.TH1F("jet1_pt_softdrop", "Lead jet p_{T} with R=%.1f;p_{T} GeV;A.U."%(R), Nbins, 0.0, 2000.0)
hist2Jet2PT = ROOT.TH1F("jet2_pt_softdrop", "Sub jet p_{T} with R=%.1f;p_{T} GeV;A.U."%(R), Nbins, 0.0, 2000.0)
hist2JetmJJ = ROOT.TH1F("jet_mJJ_softdrop", " Invariant mass m_{JJ} with R=%.1f;m_{JJ} GeV;A.U."%(R), Nbins, 0.0, 3500.0)

hist3Jet1PT = ROOT.TH1F("jet1_pt_trimmed", "Lead jet p_{T} with R=%.1f;p_{T} GeV;A.U."%(R), Nbins, 0.0, 2000.0)
hist3Jet2PT = ROOT.TH1F("jet2_pt_trimmed", "Sub jet p_{T} with R=%.1f;p_{T} GeV;A.U."%(R), Nbins, 0.0, 2000.0)
hist3JetmJJ = ROOT.TH1F("jet_mJJ_trimmed", " Invariant mass m_{JJ} with R=%.1f;m_{JJ} GeV;A.U."%(R), Nbins, 0.0, 3500.0)

histtrackpt = ROOT.TH2F("track_pt", "track PT vs Ntrk1", 20,0.0,100.0 , 40,0.0,160.0)

Nbins = 50
histdelEta = ROOT.TH1F("delta_eta", "delta_eta_jet1_and_jet2", 50,0.0,10.0)


# Loop over all events
for entry in range(0, numberOfEntries):
    # Load selected branches with data from specified event
    treeReader.ReadEntry(entry)

    # If event contains at least 2 jets
    if branchJet.GetEntries() > 1:
        # Take the two leading jets
        jet1 = branchJet.At(0)
        jet2 = branchJet.At(1)

        #Selecting events
        if jet1.PT > pT_min_jet1 and np.abs(jet1.Eta) < eta_max and jet2.PT > pT_min_jet2 and np.abs(jet2.Eta) < eta_max :

            # Defining the TLorentz vector for leading jet
            vec1 = GetJetVector(jet1.PT , jet1.Eta , jet1.Phi , jet1.Mass)

            # Defining TLorentz vector for sub - leading jet
            vec2 = GetJetVector(jet2.PT , jet2.Eta , jet2.Phi , jet2.Mass)

            # Defining TLorentz vector for missing energy branch
            #{
            met = branchMET.At(0)
            m = met.MET
            METPhi = met.Phi
            METx = m* np.cos(METPhi)
            METy = m* np.sin(METPhi)
            vecmet = ROOT.TLorentzVector()
            vecmet.SetPxPyPzE(METx , METy , 0 , m)
            #}

            # Computing transverse mass for jet1+jet2+met
            mt = (vec1 + vec2 + vecmet).Mt()

            # Computing dPhi between jet1 and met
            dPhi1 = GetdPhi(jet1.Phi, met.Phi)

            # Computing dphi between jet2 and met
            dPhi2 = GetdPhi(jet2.Phi , met.Phi)

            # Computing transverse ratio
            if (mt!=0): rt = m/mt

            # SoftDropped jets
            #{
            # Getting the Soft dropped jet1 four momenta
            jet1_softdrop = jet1.SoftDroppedP4[0]
            jet1_pt_softdrop = jet1_softdrop.Pt()

            # Getting the Soft dropped Jet2 four momenta
            jet2_softdrop = jet2.SoftDroppedP4[0]
            jet2_pt_softdrop = jet2_softdrop.Pt()

            # Computing invariant mass using Soft dropped leading and sub-leading jets
            invmass_softdrop = Getinvmass(jet1_softdrop , jet2_softdrop)
            #}

            # Trimmed jets
            #{
            # Getting the Trimmed jet1 four momenta
            jet1_trimmed = jet1.TrimmedP4[0]
            jet1_pt_trimmed = jet1_trimmed.Pt()

            # Getting the Trimmed jet2 four momenta
            jet2_trimmed = jet2.TrimmedP4[0]
            jet2_pt_trimmed = jet2_trimmed.Pt()

            # Computing invariant mass using Trimmed leading and sub-leading jets
            invmass_trimmed = Getinvmass(jet1_trimmed , jet2_trimmed)
            #}

            #Calculating average track transverse momentum
            #{
            delEta = GetdEta(jet1.Eta , jet2.Eta)
            track = []
            selectedtrack = []
            trackpt = []
            #Store the tracks to array called "track"
            for i in range(0 , branchtrack.GetEntries()):
                 track.append(branchtrack.At(i))

            #Loop over array "track" and calculate delta phi and delta R
            for j in range(0 , len(track)):
                dPhi = GetdPhi(track[j].Phi , jet1.Phi)

                dEta = GetdEta(track[j].Eta , jet1.Eta)

                DeltaR = np.sqrt(dEta*dEta + dPhi*dPhi)

                #Store the tracks which satisfy the condition on delta R to array "selectedtrack"
                if DeltaR < 1.4 :
                    selectedtrack.append(track[j])

            #Loop over selected tracks to calculate average momentum of the tracks
            for k in range(0 , len(selectedtrack)):
                trackpt.append(selectedtrack[k].PT)

            averagept = np.average(trackpt)
            #}

            #Fill histograms
            hist1Jet1PT.Fill(jet1.PT)
            hist1Jet2PT.Fill(jet2.PT)
            hist1JetmJJ.Fill((jet1.P4() + jet2.P4()).M())
            hist1Jet1Ntrk.Fill(jet1.NCharged)
            hist1Jet2Ntrk.Fill(jet2.NCharged)
            histMET.Fill(branchMET.At(0).MET)
            hmt.Fill(mt)
            hdphi1.Fill(dPhi1)
            hdphi2.Fill(dPhi2)
            hrt.Fill(rt)
            hist2Jet1PT.Fill(jet1_pt_softdrop)
            hist2Jet2PT.Fill(jet2_pt_softdrop)
            hist2JetmJJ.Fill(invmass_softdrop)
            hist3Jet1PT.Fill(jet1_pt_trimmed)
            hist3Jet2PT.Fill(jet2_pt_trimmed)
            hist3JetmJJ.Fill(invmass_trimmed)
            histdelEta.Fill(delEta)
            histtrackpt.Fill(averagept,jet1.NCharged)

#Printing number of accepted events
integral=hmt.Integral(0,-1)
print("integral=",integral)

#Normalizing the histogram
if hist1Jet1PT.GetSumw2N()==0: hist1Jet1PT.Sumw2(True)
if hist1Jet2PT.GetSumw2N()==0: hist1Jet2PT.Sumw2(True)
if hist1JetmJJ.GetSumw2N()==0: hist1JetmJJ.Sumw2(True)
if hist1Jet1Ntrk.GetSumw2N()==0: hist1Jet1Ntrk.Sumw2(True)
if hist1Jet2Ntrk.GetSumw2N()==0: hist1Jet2Ntrk.Sumw2(True)
if histMET.GetSumw2N()==0: histMET.Sumw2(True)
if hmt.GetSumw2N()==0: hmt.Sumw2(True)
if hdphi1.GetSumw2N()==0: hdphi1.Sumw2(True)
if hdphi2.GetSumw2N()==0: hdphi2.Sumw2(True)
if hrt.GetSumw2N()==0: hrt.Sumw2(True)
if hist2Jet1PT.GetSumw2N()==0: hist2Jet1PT.Sumw2(True)
if hist2Jet2PT.GetSumw2N()==0: hist2Jet2PT.Sumw2(True)
if hist2JetmJJ.GetSumw2N()==0: hist2JetmJJ.Sumw2(True)
if hist3Jet1PT.GetSumw2N()==0: hist3Jet1PT.Sumw2(True)
if hist3Jet2PT.GetSumw2N()==0: hist3Jet2PT.Sumw2(True)
if hist3JetmJJ.GetSumw2N()==0: hist3JetmJJ.Sumw2(True)
if histdelEta.GetSumw2N()==0: histdelEta.Sumw2(True)

hist1Jet1PT.Scale(1./hist1Jet1PT.Integral())
hist1Jet2PT.Scale(1./hist1Jet2PT.Integral())
hist1JetmJJ.Scale(1./hist1JetmJJ.Integral())
hist1Jet1Ntrk.Scale(1./hist1Jet1Ntrk.Integral())
hist1Jet2Ntrk.Scale(1./hist1Jet2Ntrk.Integral())
histMET.Scale(1./histMET.Integral())
hmt.Scale(1./hmt.Integral())
hdphi1.Scale(1./hdphi1.Integral())
hdphi2.Scale(1./hdphi2.Integral())
hrt.Scale(1./hrt.Integral())
hist2Jet1PT.Scale(1./hist2Jet1PT.Integral())
hist2Jet2PT.Scale(1./hist2Jet2PT.Integral())
hist2JetmJJ.Scale(1./hist2JetmJJ.Integral())
hist3Jet1PT.Scale(1./hist3Jet1PT.Integral())
hist3Jet2PT.Scale(1./hist3Jet2PT.Integral())
hist3JetmJJ.Scale(1./hist3JetmJJ.Integral())
histdelEta.Scale(1./histdelEta.Integral())

#Creating a list and saving the histograms to the list.

histlist = ROOT.TList()

histlist.Add(hist1Jet1PT)
histlist.Add(hist1Jet2PT)
histlist.Add(hist1JetmJJ)
histlist.Add(hist1Jet1Ntrk)
histlist.Add(hist1Jet2Ntrk)
histlist.Add(histMET)
histlist.Add(hmt)
histlist.Add(hdphi1)
histlist.Add(hdphi2)
histlist.Add(hrt)
histlist.Add(hist2Jet1PT)
histlist.Add(hist2Jet2PT)
histlist.Add(hist2JetmJJ)
histlist.Add(hist3Jet1PT)
histlist.Add(hist3Jet2PT)
histlist.Add(hist3JetmJJ)
histlist.Add(histtrackpt)
histlist.Add(histdelEta)

#outputFile = inputFile[:-5] + "_combined_R14.root"
rootFile = ROOT.TFile(outputFile, "RECREATE")
histlist.Write()
rootFile.Close()
