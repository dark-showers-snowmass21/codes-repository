# Authors and contacts:
# Guillaume Albouy: guillaume.albouy@etu.univ-grenoble-alpes.fr
# Akanksha Singh: akki153209@gmail.com
# Harikrishnan Nair: hunair1996@gmail.com

# Following cuts on events are assumed
# jet1.PT > 500 and np.abs(jet1.Eta) < 2.5 and jet2.PT > 500 and np.abs(jet2.Eta) < 2.5
# We assume that different branches corresponding to different jet radii are defined in root files
# In this code jet clustering radius is fixed to 1.4, can be changed at line 77
# This code will analyse input sample and create following reconstructed level normalized distributions:
# 1) pt of leading/subleading jet
# 2) dijet invarint mass
# 3) missing energy
# 4) transverse mass of dijet and met system
# 5) transverse ratio
# 6) delta phi between missin energy and leading/subleading jet
# 7) 2D histo of track pT of leading jet
# 8) delta eta between leading and subleading jet
#
# command: python /path_of_code/transverse_mass.py /path_of_rootfile/name_of_rootfile.root
# Takes the rootfile as input and computes the defined variables and fills the respective histograms.

import sys
import numpy as np
import ROOT
from array import array

M_PI = 3.14
# Define all common procedures here

def GetJetVector(jetpt, jeteta, jetphi, jetmass):
    # Given the jet pt, eta, phi and mass, this will return a TLorentzVector
    px = jetpt*np.cos(jetphi)
    py = jetpt*np.sin(jetphi)
    pz = jetpt*np.sinh(jeteta)
    energy = np.sqrt((jetmass * jetmass) + (jetpt*np.cosh(jeteta) * jetpt*np.cosh(jeteta)))
    JetVector = ROOT.TLorentzVector()
    JetVector.SetPxPyPzE(px, py, pz, energy)
    return JetVector

def GetdPhi(phi1, phi2):
    # Given two phi angles, this returns the difference between them
    dPhi = phi1 - phi2
    if (dPhi  >  M_PI): dPhi -= 2*M_PI
    if (dPhi <= - M_PI): dPhi += 2*M_PI
    return dPhi

def GetdEta(eta1,eta2):
    #Given two eta values, this will return the difference between them
    dEta = eta1 - eta2
    return dEta

def Getinvmass(obj1, obj2):
    # Given 2 four-momenta, this will return the invariant mass
    invmass = (obj1 + obj2).M()
    return invmass
