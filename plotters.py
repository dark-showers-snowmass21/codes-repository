# bash command: python /location/of/code/histograms.py -a /path/rootfile1.root -b /path/rootfile2.root -c /path/rootfile3.root -d /path/rootfile4.root -e /path/rootfile5.root -f/path/rootfile6.root -m Mq -p Nf -q Nc1 -r Nc2 -s Nc3 -t Nc4
# Takes rootfiles as input and prints different histograms on separate canvas.
# Per plot, four different histograms for foud different colors and one given flavour are plotted

import os, sys
import numpy as np
from numpy import *
from pylab import *
from scipy.interpolate import interp1d
import ROOT
from array import array
import argparse
parser = argparse.ArgumentParser()
parser.add_argument('-a' , help = "rootfile1")
parser.add_argument('-b' , help = "rootfile2")
parser.add_argument('-c' , help = "rootfile3")
parser.add_argument('-d' , help = "rootfile4")
parser.add_argument('-e' , help = "rootfile5")
parser.add_argument('-f' , help = "rootfile6")
parser.add_argument('-m' , help = "Mq" , type = float)
parser.add_argument('-p' , help = "Nf")
parser.add_argument('-q' , help = "Nc1")
parser.add_argument('-r' , help = "Nc2")
parser.add_argument('-s' , help = "Nc3")
parser.add_argument('-t' , help = "Nc4")
args = parser.parse_args()

rootfile1 = args.a
rootfile2 = args.b
rootfile3 = args.c
rootfile4 = args.d
rootfile5 = args.e
rootfile6 = args.f
Mq = args.m
Nf = args.p
Nc1 = args.q
Nc2 = args.r
Nc3 = args.s
Nc4 = args.t

print("Input files :")
print("rootfile1: ",rootfile1)
print("rootfile2: ",rootfile2)
print("rootfile3: ",rootfile3)
print("rootfile4: ",rootfile4)
print("rootfile5: ",rootfile5)
print("rootfile6: ",rootfile6)
print(Mq)
print(Nf,Nc1)
print(Nf,Nc2)
print(Nf,Nc3)
print(Nf,Nc4)

m_pion = (Mq)*2.
m_rho = (m_pion)*2.1

print("m_pion=", m_pion, "GeV")
print("m_rho=", m_rho, "GeV")
# Reading the first rootfile

f1 = ROOT.TFile(rootfile1)

# Getting histograms from the first root file.

hist1jet1PT = f1.Get('jet1_pt')#.Rebin(5)
hist1jet2PT = f1.Get('jet2_pt')#.Rebin(5)
hist1mjj = f1.Get('jet_mJJ')#.Rebin(5)
hist1met = f1.Get('jet_met')#.Rebin(5)
hist1ntrk1 = f1.Get('jet1_ntrk')#.Rebin(3)
hist1ntrk2 = f1.Get('jet2_ntrk')
hist1mt = f1.Get('jet_met_mt')#.Rebin(3)
hist1dphi1 = f1.Get('dPhi1')
hist1dphi2 = f1.Get('dPhi2')
hist1rt = f1.Get('jet_met_rt')
hist1jet1PT_softdrop = f1.Get('jet1_pt_softdrop')
hist1jet2PT_softdrop = f1.Get('jet2_pt_softdrop')
hist1mjj_softdrop = f1.Get('jet_mJJ_softdrop')
hist1jet1PT_trimmed = f1.Get('jet1_pt_trimmed')
hist1jet2PT_trimmed = f1.Get('jet2_pt_trimmed')
hist1mjj_trimmed = f1.Get('jet_mJJ_trimmed')
hist1track_pt = f1.Get('track_pt')

# Read second root file

f2 = ROOT.TFile(rootfile2)

# Getting histograms from second root file

hist2jet1PT = f2.Get('jet1_pt')#.Rebin(5)
hist2jet2PT = f2.Get('jet2_pt')#.Rebin(5)
hist2mjj = f2.Get('jet_mJJ')#.Rebin(5)
hist2met = f2.Get('jet_met')#.Rebin(5)
hist2ntrk1 = f2.Get('jet1_ntrk')
hist2ntrk2 = f2.Get('jet2_ntrk')
hist2mt = f2.Get('jet_met_mt')#.Rebin(3)
hist2dphi1 = f2.Get('dPhi1')
hist2dphi2 = f2.Get('dPhi2')
hist2rt = f2.Get('jet_met_rt')
hist2jet1PT_softdrop = f2.Get('jet1_pt_softdrop')
hist2jet2PT_softdrop = f2.Get('jet2_pt_softdrop')
hist2mjj_softdrop = f2.Get('jet_mJJ_softdrop')
hist2jet1PT_trimmed = f2.Get('jet1_pt_trimmed')
hist2jet2PT_trimmed = f2.Get('jet2_pt_trimmed')
hist2mjj_trimmed = f2.Get('jet_mJJ_trimmed')
hist2track_pt = f2.Get('track_pt')

#Read third root file

f3 = ROOT.TFile(rootfile3)

# Getting histograms from third root file.

hist3jet1PT = f3.Get('jet1_pt')#.Rebin(5)
hist3jet2PT = f3.Get('jet2_pt')#.Rebin(5)
hist3mjj = f3.Get('jet_mJJ')#.Rebin(5)
hist3met = f3.Get('jet_met')#.Rebin(5)
hist3ntrk1 = f3.Get('jet1_ntrk')
hist3ntrk2 = f3.Get('jet2_ntrk')
hist3mt = f3.Get('jet_met_mt')#.Rebin(3)
hist3dphi1 = f3.Get('dPhi1')
hist3dphi2 = f3.Get('dPhi2')
hist3rt = f3.Get('jet_met_rt')
hist3jet1PT_softdrop = f3.Get('jet1_pt_softdrop')
hist3jet2PT_softdrop = f3.Get('jet2_pt_softdrop')
hist3mjj_softdrop = f3.Get('jet_mJJ_softdrop')
hist3jet1PT_trimmed = f3.Get('jet1_pt_trimmed')
hist3jet2PT_trimmed = f3.Get('jet2_pt_trimmed')
hist3mjj_trimmed = f3.Get('jet_mJJ_trimmed')
hist3track_pt = f3.Get('track_pt')

#Read fourth root file

f4 = ROOT.TFile(rootfile4)

# Getting histograms from fourth root file.

hist4jet1PT = f4.Get('jet1_pt')#.Rebin(5)
hist4jet2PT = f4.Get('jet2_pt')#.Rebin(5)
hist4mjj = f4.Get('jet_mJJ')#.Rebin(5)
hist4met = f4.Get('jet_met')#.Rebin(5)
hist4ntrk1 = f4.Get('jet1_ntrk')
hist4ntrk2 = f4.Get('jet2_ntrk')
hist4mt = f4.Get('jet_met_mt')#.Rebin(3)
hist4dphi1 = f4.Get('dPhi1')
hist4dphi2 = f4.Get('dPhi2')
hist4rt = f4.Get('jet_met_rt')
hist4jet1PT_softdrop = f4.Get('jet1_pt_softdrop')
hist4jet2PT_softdrop = f4.Get('jet2_pt_softdrop')
hist4mjj_softdrop = f4.Get('jet_mJJ_softdrop')
hist4jet1PT_trimmed = f4.Get('jet1_pt_trimmed')
hist4jet2PT_trimmed = f4.Get('jet2_pt_trimmed')
hist4mjj_trimmed = f4.Get('jet_mJJ_trimmed')
hist4track_pt = f4.Get('track_pt')

# Read fifth root file

f5 = ROOT.TFile(rootfile5)

# Getting histograms from fifth root file
hist5jet1PT = f5.Get('jet1_pt')#.Rebin(5)
hist5jet2PT = f5.Get('jet2_pt')#.Rebin(5)
hist5mjj = f5.Get('jet_mJJ')#.Rebin(5)
hist5met = f5.Get('jet_met')#.Rebin(5)
hist5ntrk1 = f5.Get('jet1_ntrk')
hist5ntrk2 = f5.Get('jet2_ntrk')
hist5mt = f5.Get('jet_met_mt')#.Rebin(3)
hist5dphi1 = f5.Get('dPhi1')
hist5dphi2 = f5.Get('dPhi2')
hist5rt = f5.Get('jet_met_rt')
hist5jet1PT_softdrop = f5.Get('jet1_pt_softdrop')
hist5jet2PT_softdrop = f5.Get('jet2_pt_softdrop')
hist5mjj_softdrop = f5.Get('jet_mJJ_softdrop')
hist5jet1PT_trimmed = f5.Get('jet1_pt_trimmed')
hist5jet2PT_trimmed = f5.Get('jet2_pt_trimmed')
hist5mjj_trimmed = f5.Get('jet_mJJ_trimmed')
hist5track_pt = f5.Get('track_pt')

# Read sixth root file

f6 = ROOT.TFile(rootfile6)

# Getting histograms from sixth root file
hist6jet1PT = f6.Get('jet1_pt')#.Rebin(5)
hist6jet2PT = f6.Get('jet2_pt')#.Rebin(5)
hist6mjj = f6.Get('jet_mJJ')#.Rebin(5)
hist6met = f6.Get('jet_met')#.Rebin(5)
hist6ntrk1 = f6.Get('jet1_ntrk')
hist6ntrk2 = f6.Get('jet2_ntrk')
hist6mt = f6.Get('jet_met_mt')#.Rebin(3)
hist6dphi1 = f6.Get('dPhi1')
hist6dphi2 = f6.Get('dPhi2')
hist6rt = f6.Get('jet_met_rt')
hist6jet1PT_softdrop = f6.Get('jet1_pt_softdrop')
hist6jet2PT_softdrop = f6.Get('jet2_pt_softdrop')
hist6mjj_softdrop = f6.Get('jet_mJJ_softdrop')
hist6jet1PT_trimmed = f6.Get('jet1_pt_trimmed')
hist6jet2PT_trimmed = f6.Get('jet2_pt_trimmed')
hist6mjj_trimmed = f6.Get('jet_mJJ_trimmed')
hist6track_pt = f6.Get('track_pt')

# Creating and using first canvas; i.e. pTj1.

canvas1 = ROOT.TCanvas("canvas1")
canvas1.cd()

#Plotting histograms on first canvas.

hist1jet1PT.SetTitle("Transverse momentum of leading jet")
hist1jet1PT.GetXaxis().SetTitle("p_{T} (leading jet) [GeV]")
hist1jet1PT.GetYaxis().SetTitle("A.U.")
hist1jet1PT.GetXaxis().SetLabelSize(0.04)
hist1jet1PT.GetYaxis().SetLabelSize(0.04)
hist1jet1PT.GetXaxis().SetTitleSize(0.04)
hist1jet1PT.GetYaxis().SetTitleSize(0.04)
hist1jet1PT.SetStats(0)
hist1jet1PT.SetLineColor(ROOT.kRed)
hist1jet1PT.SetLineWidth(2)
hist1jet1PT.Draw("hist1")

hist2jet1PT.SetLineColor(ROOT.kBlue)
hist2jet1PT.SetLineWidth(2)
hist2jet1PT.SetStats(0)
hist2jet1PT.Draw("hist1 same")
hist1jet1PT.GetXaxis().SetRangeUser(0,1600)
hist1jet1PT.GetYaxis().SetRangeUser(0,0.24)
hist1jet1PT.GetXaxis().SetTitleOffset(1.4)
hist1jet1PT.GetYaxis().SetTitleOffset(1.4)

hist3jet1PT.SetLineColor(ROOT.kBlack)
hist3jet1PT.SetLineWidth(2)
hist3jet1PT.SetStats(0)
hist3jet1PT.Draw("hist1 same")

hist4jet1PT.SetLineColor(ROOT.kGreen)
hist4jet1PT.SetLineWidth(2)
hist4jet1PT.SetStats(0)
hist4jet1PT.Draw("hist1 same")

hist5jet1PT.SetLineColor(7)
hist5jet1PT.SetLineStyle(2)
hist5jet1PT.SetLineWidth(2)
hist5jet1PT.SetStats(0)
hist5jet1PT.Draw("hist1 same")

hist6jet1PT.SetLineColor(6)
hist6jet1PT.SetLineStyle(2)
hist6jet1PT.SetLineWidth(2)
hist6jet1PT.SetStats(0)
hist6jet1PT.Draw("hist1 same")

#setting margins on first canvas

canvas1.SetRightMargin(0.09)
canvas1.SetLeftMargin(0.15)
canvas1.SetBottomMargin(0.15)

#adding text on first canvas
t1 = ROOT.TLatex()
t1.SetNDC(ROOT.kTRUE)
t1.SetTextSize(0.03)
t1.DrawLatex(0.18 ,0.86 ,"M_{h'} = 2 TeV , M_{q} = %.1f GeV , R = 1.4"%(Mq))
t1.SetTextSize(0.03)
t1.DrawLatex(0.18 ,0.82 ,"M_{\pi} = %.1f GeV , M_{#rho} = %.1f GeV , \Lambda = %.1f GeV"%(m_pion, m_rho, Mq))

#Adding legend on first canvas

legend1 = ROOT.TLegend(0.55,0.65,0.9,0.9)
legend1.SetTextSize(0.03)
legend1.AddEntry(hist1jet1PT,"N_{f}=%s , N_{c}=%s , Mean = %.1f"%(Nf,Nc1,hist1jet1PT.GetMean()),"l")
legend1.AddEntry(hist2jet1PT,"N_{f}=%s , N_{c}=%s , Mean = %.1f"%(Nf,Nc2,hist2jet1PT.GetMean()),"l")
legend1.AddEntry(hist3jet1PT,"N_{f}=%s , N_{c}=%s , Mean = %.1f"%(Nf,Nc3,hist3jet1PT.GetMean()),"l")
legend1.AddEntry(hist4jet1PT,"N_{f}=%s , N_{c}=%s , Mean = %.1f"%(Nf,Nc4,hist4jet1PT.GetMean()),"l")
legend1.AddEntry(hist5jet1PT,"QCD Z' -> qq~ , Mean = %.1f"%(hist5jet1PT.GetMean()),"l")
legend1.AddEntry(hist6jet1PT,"QCD h' -> gg~ , Mean = %.1f"%(hist6jet1PT.GetMean()),"l")
legend1.SetLineWidth(1)
legend1.Draw()

canvas1.Update()
ROOT.gSystem.ProcessEvents()

#saving the canvas
canvas1.Print("ptj1_varyingNc_Nf%s_Mq%.0f.pdf" %(Nf,Mq))
##########################################################################################################################################################################################

# Creating and using second canvas; i.e. pTj2.

canvas2 = ROOT.TCanvas("canvas2")
canvas2.cd()

#Plotting histograms on second canvas.

hist1jet2PT.SetTitle("Transverse momentum of sub-leading jet")
hist1jet2PT.GetXaxis().SetTitle("p_{T} (sub-leading jet) [GeV]")
hist1jet2PT.GetYaxis().SetTitle("A.U.")
hist1jet2PT.GetXaxis().SetLabelSize(0.04)
hist1jet2PT.GetYaxis().SetLabelSize(0.04)
hist1jet2PT.GetXaxis().SetTitleSize(0.04)
hist1jet2PT.GetYaxis().SetTitleSize(0.04)
hist1jet2PT.SetStats(0)
hist1jet2PT.SetLineColor(ROOT.kRed)
hist1jet2PT.SetLineWidth(2)
hist1jet2PT.Draw("hist2")

hist2jet2PT.SetLineColor(ROOT.kBlue)
hist2jet2PT.SetLineWidth(2)
hist2jet2PT.SetStats(0)
hist2jet2PT.Draw("hist2 same")
hist1jet2PT.GetXaxis().SetRangeUser(0,1400)
hist1jet2PT.GetYaxis().SetRangeUser(0,0.4)
hist1jet2PT.GetXaxis().SetTitleOffset(1.4)
hist1jet2PT.GetYaxis().SetTitleOffset(1.4)

hist3jet2PT.SetLineColor(ROOT.kBlack)
hist3jet2PT.SetLineWidth(2)
hist3jet2PT.SetStats(0)
hist3jet2PT.Draw("hist2 same")

hist4jet2PT.SetLineColor(ROOT.kGreen)
hist4jet2PT.SetLineWidth(2)
hist4jet2PT.SetStats(0)
hist4jet2PT.Draw("hist2 same")

hist5jet2PT.SetLineColor(7)
hist5jet2PT.SetLineStyle(2)
hist5jet2PT.SetLineWidth(2)
hist5jet2PT.SetStats(0)
hist5jet2PT.Draw("hist2 same")

hist6jet2PT.SetLineColor(6)
hist6jet2PT.SetLineStyle(2)
hist6jet2PT.SetLineWidth(2)
hist6jet2PT.SetStats(0)
hist6jet2PT.Draw("hist2 same")


#setting margins on second canvas

canvas2.SetRightMargin(0.09)
canvas2.SetLeftMargin(0.15)
canvas2.SetBottomMargin(0.15)

#adding text on second canvas
t2 = ROOT.TLatex()
t2.SetNDC(ROOT.kTRUE)
t2.SetTextSize(0.03)
t2.DrawLatex(0.18 ,0.86 ,"M_{h'} = 2 TeV , M_{q} = %.1f GeV , R = 1.4" %(Mq))
t2.SetTextSize(0.03)
t2.DrawLatex(0.18 ,0.82 ,"M_{\pi} = %.1f GeV , M_{#rho} = %.1f GeV , \Lambda = %.1f GeV"%(m_pion, m_rho, Mq))


#Adding legend on second canvas

legend2 = ROOT.TLegend(0.55,0.65,0.9,0.9)
legend2.SetTextSize(0.03)
legend2.AddEntry(hist1jet2PT,"N_{f}=%s , N_{c}=%s , Mean = %.1f"%(Nf,Nc1,hist1jet2PT.GetMean()),"l")
legend2.AddEntry(hist2jet2PT,"N_{f}=%s , N_{c}=%s , Mean = %.1f"%(Nf,Nc2,hist2jet2PT.GetMean()),"l")
legend2.AddEntry(hist3jet2PT,"N_{f}=%s , N_{c}=%s , Mean = %.1f"%(Nf,Nc3,hist3jet2PT.GetMean()),"l")
legend2.AddEntry(hist4jet2PT,"N_{f}=%s , N_{c}=%s , Mean = %.1f"%(Nf,Nc4,hist4jet2PT.GetMean()),"l")
legend2.AddEntry(hist5jet2PT,"QCD Z' -> qq~ , Mean = %.1f"%(hist5jet2PT.GetMean()),"l")
legend2.AddEntry(hist6jet2PT,"QCD h' -> gg~ , Mean = %.1f"%(hist6jet2PT.GetMean()),"l")
legend2.SetLineWidth(1)
legend2.Draw()

canvas2.Update()
ROOT.gSystem.ProcessEvents()


#Saving the canvas
canvas2.Print("ptj2_varyingNc_Nf%s_Mq%.0f.pdf" %(Nf,Mq))

##################################################################################################################################################################################
# Creating and using third canvas; i.e. mjj.

canvas3 = ROOT.TCanvas("canvas3")
canvas3.cd()


#Plotting histograms on third canvas.

hist1mjj.SetTitle("Invariant Mass")
hist1mjj.GetXaxis().SetTitle("Invariant mass [GeV]")
hist1mjj.GetYaxis().SetTitle("A.U.")
hist1mjj.GetXaxis().SetLabelSize(0.04)
hist1mjj.GetYaxis().SetLabelSize(0.04)
hist1mjj.GetXaxis().SetTitleSize(0.04)
hist1mjj.GetYaxis().SetTitleSize(0.04)
hist1mjj.SetStats(0)
hist1mjj.SetLineColor(ROOT.kRed)
hist1mjj.SetLineWidth(2)
hist1mjj.Draw("hist3")

hist2mjj.SetLineColor(ROOT.kBlue)
hist2mjj.SetLineWidth(2)
hist2mjj.SetStats(0)
hist2mjj.Draw("hist3 same")
hist1mjj.GetXaxis().SetRangeUser(0,3000)
hist1mjj.GetYaxis().SetRangeUser(0,0.28)
hist1mjj.GetXaxis().SetTitleOffset(1.4)
hist1mjj.GetYaxis().SetTitleOffset(1.4)

hist3mjj.SetLineColor(ROOT.kBlack)
hist3mjj.SetLineWidth(2)
hist3mjj.SetStats(0)
hist3mjj.Draw("hist3 same")

hist4mjj.SetLineColor(ROOT.kGreen)
hist4mjj.SetLineWidth(2)
hist4mjj.SetStats(0)
hist4mjj.Draw("hist3 same")

hist5mjj.SetLineColor(7)
hist5mjj.SetLineStyle(2)
hist5mjj.SetLineWidth(2)
hist5mjj.SetStats(0)
hist5mjj.Draw("hist3 same")

hist6mjj.SetLineColor(6)
hist6mjj.SetLineStyle(2)
hist6mjj.SetLineWidth(2)
hist6mjj.SetStats(0)
hist6mjj.Draw("hist3 same")

#setting margins on third canvas

canvas3.SetRightMargin(0.09)
canvas3.SetLeftMargin(0.15)
canvas3.SetBottomMargin(0.15)

#adding text on third canvas
t3 = ROOT.TLatex()
t3.SetNDC(ROOT.kTRUE)
t3.SetTextSize(0.03)
t3.DrawLatex(0.18 ,0.86 ,"M_{h'} = 2 TeV , M_{q} = %.1f GeV , R = 1.4" %(Mq))
t3.SetTextSize(0.03)
t3.DrawLatex(0.18 ,0.82 ,"M_{\pi} = %.1f GeV , M_{#rho} = %.1f GeV , \Lambda = %.1f GeV"%(m_pion, m_rho, Mq))

#Adding legend on third canvas

legend3 = ROOT.TLegend(0.55,0.65,0.9,0.9)
legend3.SetTextSize(0.03)
legend3.AddEntry(hist1mjj,"N_{f}=%s , N_{c}=%s , Mean = %.1f"%(Nf,Nc1,hist1mjj.GetMean()),"l")
legend3.AddEntry(hist2mjj,"N_{f}=%s , N_{c}=%s , Mean = %.1f"%(Nf,Nc2,hist2mjj.GetMean()),"l")
legend3.AddEntry(hist3mjj,"N_{f}=%s , N_{c}=%s , Mean = %.1f"%(Nf,Nc3,hist3mjj.GetMean()),"l")
legend3.AddEntry(hist4mjj,"N_{f}=%s , N_{c}=%s , Mean = %.1f"%(Nf,Nc4,hist4mjj.GetMean()),"l")
legend3.AddEntry(hist5mjj,"QCD Z' -> qq~ , Mean = %.1f"%(hist5mjj.GetMean()),"l")
legend3.AddEntry(hist6mjj,"QCD h' -> gg~ , Mean = %.1f"%(hist6mjj.GetMean()),"l")
legend3.SetLineWidth(1)
legend3.Draw()

canvas3.Update()
ROOT.gSystem.ProcessEvents()


#Saving the canvas
canvas3.Print("mjj_varyingNc_Nf%s_Mq%.0f.pdf" %(Nf,Mq))

##################################################################################################################################################################################
# Creating and using fourth canvas; i.e. met.

canvas4 = ROOT.TCanvas("canvas4")
canvas4.cd()

#Plotting histograms on fourth canvas.

hist1met.SetTitle("Transverse Missing Energy")
hist1met.GetXaxis().SetTitle("Missing energy [GeV]")
hist1met.GetYaxis().SetTitle("A.U.")
hist1met.GetXaxis().SetLabelSize(0.04)
hist1met.GetYaxis().SetLabelSize(0.04)
hist1met.GetXaxis().SetTitleSize(0.04)
hist1met.GetYaxis().SetTitleSize(0.04)
hist1met.SetStats(0)
hist1met.SetLineColor(ROOT.kRed)
hist1met.SetLineWidth(2)
hist1met.Draw("hist4")

hist2met.SetLineColor(ROOT.kBlue)
hist2met.SetLineWidth(2)
hist2met.SetStats(0)
hist2met.Draw("hist4 same")
hist1met.GetXaxis().SetRangeUser(0,1200)
hist1met.GetYaxis().SetRangeUser(0,0.6)
hist1met.GetXaxis().SetTitleOffset(1.4)
hist1met.GetYaxis().SetTitleOffset(1.4)

hist3met.SetLineColor(ROOT.kBlack)
hist3met.SetLineWidth(2)
hist3met.SetStats(0)
hist3met.Draw("hist4 same")

hist4met.SetLineColor(ROOT.kGreen)
hist4met.SetLineWidth(2)
hist4met.SetStats(0)
hist4met.Draw("hist4 same")

hist5met.SetLineColor(7)
hist5met.SetLineStyle(2)
hist5met.SetLineWidth(2)
hist5met.SetStats(0)
hist5met.Draw("hist4 same")

hist6met.SetLineColor(6)
hist6met.SetLineStyle(2)
hist6met.SetLineWidth(2)
hist6met.SetStats(0)
hist6met.Draw("hist4 same")


#setting margins on fourth canvas

canvas4.SetRightMargin(0.09)
canvas4.SetLeftMargin(0.15)
canvas4.SetBottomMargin(0.15)

#adding text on fourth canvas
t4 = ROOT.TLatex()
t4.SetNDC(ROOT.kTRUE)
t4.SetTextSize(0.03)
t4.DrawLatex(0.18 ,0.86 ,"M_{h'} = 2 TeV , M_{q} = %.1f GeV , R = 1.4" %(Mq))
t4.SetTextSize(0.03)
t4.DrawLatex(0.18 ,0.82 ,"M_{\pi} = %.1f GeV , M_{#rho} = %.1f GeV , \Lambda = %.1f GeV"%(m_pion, m_rho, Mq))


#Adding legend on fourth canvas

legend4 = ROOT.TLegend(0.55,0.65,0.9,0.9)
legend4.SetTextSize(0.03)
legend4.AddEntry(hist1met,"N_{f}=%s , N_{c}=%s , Mean = %.1f"%(Nf,Nc1,hist1met.GetMean()),"l")
legend4.AddEntry(hist2met,"N_{f}=%s , N_{c}=%s , Mean = %.1f"%(Nf,Nc2,hist2met.GetMean()),"l")
legend4.AddEntry(hist3met,"N_{f}=%s , N_{c}=%s , Mean = %.1f"%(Nf,Nc3,hist3met.GetMean()),"l")
legend4.AddEntry(hist4met,"N_{f}=%s , N_{c}=%s , Mean = %.1f"%(Nf,Nc4,hist4met.GetMean()),"l")
legend4.AddEntry(hist5met,"QCD Z' -> qq~, Mean = %.1f"%(hist5met.GetMean()),"l")
legend4.AddEntry(hist6met,"QCD h' -> gg~, Mean = %.1f"%(hist6met.GetMean()),"l")
legend4.SetLineWidth(1)
legend4.Draw()

canvas4.Update()
ROOT.gSystem.ProcessEvents()


#Saving the canvas
canvas4.Print("met_varyingNc_Nf%s_Mq%.0f.pdf" %(Nf,Mq))

###################################################################################################################################################################################

# Creating and using fifth canvas; i.e. ntrk1.

canvas5 = ROOT.TCanvas("canvas5")
canvas5.cd()

#Plotting histograms on fifth canvas.

hist1ntrk1.SetTitle("Number of charged particles in leading jet")
hist1ntrk1.GetXaxis().SetTitle("N_{trk} (leading jet)")
hist1ntrk1.GetYaxis().SetTitle("A.U.")
hist1ntrk1.GetXaxis().SetLabelSize(0.04)
hist1ntrk1.GetYaxis().SetLabelSize(0.04)
hist1ntrk1.GetXaxis().SetTitleSize(0.04)
hist1ntrk1.GetYaxis().SetTitleSize(0.04)
hist1ntrk1.SetStats(0)
hist1ntrk1.SetLineColor(ROOT.kRed)
hist1ntrk1.SetLineWidth(2)
hist1ntrk1.Draw("hist5")

hist2ntrk1.SetLineColor(ROOT.kBlue)
hist2ntrk1.SetLineWidth(2)
hist2ntrk1.SetStats(0)
hist2ntrk1.Draw("hist5 same")
hist1ntrk1.GetXaxis().SetRangeUser(0,160)
hist1ntrk1.GetYaxis().SetRangeUser(0,0.45)
hist1ntrk1.GetXaxis().SetTitleOffset(1.4)
hist1ntrk1.GetYaxis().SetTitleOffset(1.4)

hist3ntrk1.SetLineColor(ROOT.kBlack)
hist3ntrk1.SetLineWidth(2)
hist3ntrk1.SetStats(0)
hist3ntrk1.Draw("hist5 same")

hist4ntrk1.SetLineColor(ROOT.kGreen)
hist4ntrk1.SetLineWidth(2)
hist4ntrk1.SetStats(0)
hist4ntrk1.Draw("hist5 same")

hist5ntrk1.SetLineColor(7)
hist5ntrk1.SetLineStyle(2)
hist5ntrk1.SetLineWidth(2)
hist5ntrk1.SetStats(0)
hist5ntrk1.Draw("hist5 same")

hist6ntrk1.SetLineColor(6)
hist6ntrk1.SetLineStyle(2)
hist6ntrk1.SetLineWidth(2)
hist6ntrk1.SetStats(0)
hist6ntrk1.Draw("hist5 same")

#setting margins on fifth canvas

canvas5.SetRightMargin(0.09)
canvas5.SetLeftMargin(0.15)
canvas5.SetBottomMargin(0.15)

#adding text on fifth canvas
t5 = ROOT.TLatex()
t5.SetNDC(ROOT.kTRUE)
t5.SetTextSize(0.03)
t5.DrawLatex(0.18 ,0.86 ,"M_{h'} = 2 TeV , M_{q} = %.1f GeV , R = 1.4" %(Mq))
t5.SetTextSize(0.03)
t5.DrawLatex(0.18 ,0.82 ,"M_{\pi} = %.1f GeV , M_{#rho} = %.1f GeV , \Lambda = %.1f GeV"%(m_pion, m_rho, Mq))

#Adding legend on fifth canvas

legend5 = ROOT.TLegend(0.55,0.65,0.9,0.9)
legend5.SetTextSize(0.03)
legend5.AddEntry(hist1ntrk1,"N_{f}=%s , N_{c}=%s , Mean = %.1f"%(Nf,Nc1,hist1ntrk1.GetMean()),"l")
legend5.AddEntry(hist2ntrk1,"N_{f}=%s , N_{c}=%s , Mean = %.1f"%(Nf,Nc2,hist2ntrk1.GetMean()),"l")
legend5.AddEntry(hist3ntrk1,"N_{f}=%s , N_{c}=%s , Mean = %.1f"%(Nf,Nc3,hist3ntrk1.GetMean()),"l")
legend5.AddEntry(hist4ntrk1,"N_{f}=%s , N_{c}=%s , Mean = %.1f"%(Nf,Nc4,hist4ntrk1.GetMean()),"l")
legend5.AddEntry(hist5ntrk1,"QCD Z' -> qq~ , Mean = %.1f"%(hist5ntrk1.GetMean()),"l")
legend5.AddEntry(hist6ntrk1,"QCD h' -> gg~ , Mean = %.1f"%(hist6ntrk1.GetMean()),"l")
legend5.SetLineWidth(1)
legend5.Draw()

canvas5.Update()
ROOT.gSystem.ProcessEvents()


#Saving the canvas
canvas5.Print("ntrk1_varyingNc_Nf%s_Mq%.0f.pdf" %(Nf,Mq))

###############################################################################################################################################################################


# Creating and using sixth canvas; i.e. ntrk2.

canvas6 = ROOT.TCanvas("canvas6")
canvas6.cd()

#Plotting histograms on sixth canvas.

hist1ntrk2.SetTitle("Number of charged particles in sub-leading jet")
hist1ntrk2.GetXaxis().SetTitle("N_{trk} (sub-leading jet)")
hist1ntrk2.GetYaxis().SetTitle("A.U.")
hist1ntrk2.GetXaxis().SetLabelSize(0.04)
hist1ntrk2.GetYaxis().SetLabelSize(0.04)
hist1ntrk2.GetXaxis().SetTitleSize(0.04)
hist1ntrk2.GetYaxis().SetTitleSize(0.04)
hist1ntrk2.SetStats(0)
hist1ntrk2.SetLineColor(ROOT.kRed)
hist1ntrk2.SetLineWidth(2)
hist1ntrk2.Draw("hist6")

hist2ntrk2.SetLineColor(ROOT.kBlue)
hist2ntrk2.SetLineWidth(2)
hist2ntrk2.SetStats(0)
hist2ntrk2.Draw("hist6 same")
hist1ntrk2.GetXaxis().SetRangeUser(0,160)
hist1ntrk2.GetYaxis().SetRangeUser(0,0.5)
hist1ntrk2.GetXaxis().SetTitleOffset(1.4)
hist1ntrk2.GetYaxis().SetTitleOffset(1.4)

hist3ntrk2.SetLineColor(ROOT.kBlack)
hist3ntrk2.SetLineWidth(2)
hist3ntrk2.SetStats(0)
hist3ntrk2.Draw("hist6 same")

hist4ntrk2.SetLineColor(ROOT.kGreen)
hist4ntrk2.SetLineWidth(2)
hist4ntrk2.SetStats(0)
hist4ntrk2.Draw("hist6 same")

hist5ntrk2.SetLineColor(7)
hist5ntrk2.SetLineStyle(2)
hist5ntrk2.SetLineWidth(2)
hist5ntrk2.SetStats(0)
hist5ntrk2.Draw("hist6 same")

hist6ntrk2.SetLineColor(6)
hist6ntrk2.SetLineStyle(2)
hist6ntrk2.SetLineWidth(2)
hist6ntrk2.SetStats(0)
hist6ntrk2.Draw("hist6 same")


#setting margins on sixth canvas

canvas6.SetRightMargin(0.09)
canvas6.SetLeftMargin(0.15)
canvas6.SetBottomMargin(0.15)

#adding text on sixth canvas
t6 = ROOT.TLatex()
t6.SetNDC(ROOT.kTRUE)
t6.SetTextSize(0.03)
t6.DrawLatex(0.18 ,0.86 ,"M_{h'} = 2 TeV , M_{q} = %.1f GeV , R = 1.4" %(Mq))
t6.SetTextSize(0.03)
t6.DrawLatex(0.18 ,0.82 ,"M_{\pi} = %.1f GeV , M_{#rho} = %.1f GeV , \Lambda = %.1f GeV"%(m_pion, m_rho, Mq))

#Adding legend on sixth canvas

legend6 = ROOT.TLegend(0.55,0.65,0.9,0.9)
legend6.SetTextSize(0.03)
legend6.AddEntry(hist1ntrk2,"N_{f}=%s , N_{c}=%s , Mean = %.1f"%(Nf,Nc1,hist1ntrk2.GetMean()),"l")
legend6.AddEntry(hist2ntrk2,"N_{f}=%s , N_{c}=%s , Mean = %.1f"%(Nf,Nc2,hist2ntrk2.GetMean()),"l")
legend6.AddEntry(hist2ntrk2,"N_{f}=%s , N_{c}=%s , Mean = %.1f"%(Nf,Nc3,hist3ntrk2.GetMean()),"l")
legend6.AddEntry(hist2ntrk2,"N_{f}=%s , N_{c}=%s , Mean = %.1f"%(Nf,Nc4,hist4ntrk2.GetMean()),"l")
legend6.AddEntry(hist3ntrk2,"QCD Z' -> qq~ , Mean = %.1f"%(hist5ntrk2.GetMean()),"l")
legend6.AddEntry(hist4ntrk2,"QCD h' -> gg~ , Mean = %.1f"%(hist6ntrk2.GetMean()),"l")
legend6.SetLineWidth(1)
legend6.Draw()

canvas6.Update()
ROOT.gSystem.ProcessEvents()


#Saving the canvas
canvas6.Print("ntrk2_varyingNc_Nf%s_Mq%.0f.pdf" %(Nf,Mq))

#####################################################################################################################################################
# Creating and using seventh canvas; i.e. mt

canvas7 = ROOT.TCanvas("canvas7")
canvas7.cd()

#Plotting histograms on first canvas.

hist1mt.SetTitle("Transverse Mass")
hist1mt.GetXaxis().SetTitle("m_{T}")
hist1mt.GetYaxis().SetTitle("A.U.")
hist1mt.GetXaxis().SetLabelSize(0.04)
hist1mt.GetYaxis().SetLabelSize(0.04)
hist1mt.GetXaxis().SetTitleSize(0.04)
hist1mt.GetYaxis().SetTitleSize(0.04)
hist1mt.SetStats(0)
hist1mt.SetLineColor(ROOT.kRed)
hist1mt.SetLineWidth(2)
hist1mt.Draw("hist7")

hist2mt.SetLineColor(ROOT.kBlue)
hist2mt.SetLineWidth(2)
hist2mt.SetStats(0)
hist2mt.Draw("same hist7")
hist1mt.GetXaxis().SetRangeUser(0,2500)
hist1mt.GetYaxis().SetRangeUser(0,0.25)
hist1mt.GetXaxis().SetTitleOffset(1.4)
hist1mt.GetYaxis().SetTitleOffset(1.4)

hist3mt.SetLineColor(ROOT.kBlack)
hist3mt.SetLineWidth(2)
hist3mt.SetStats(0)
hist3mt.Draw("same hist7")

hist4mt.SetLineColor(ROOT.kGreen)
hist4mt.SetLineWidth(2)
hist4mt.SetStats(0)
hist4mt.Draw("same hist7")

hist5mt.SetLineColor(7)
hist5mt.SetLineStyle(2)
hist5mt.SetLineWidth(2)
hist5mt.SetStats(0)
hist5mt.Draw("same hist7")

hist6mt.SetLineColor(6)
hist6mt.SetLineStyle(2)
hist6mt.SetLineWidth(2)
hist6mt.SetStats(0)
hist6mt.Draw("same hist7")

#setting margins on canvas

canvas7.SetRightMargin(0.09)
canvas7.SetLeftMargin(0.15)
canvas7.SetBottomMargin(0.15)

#adding text on canvas
t7 = ROOT.TLatex()
t7.SetNDC(ROOT.kTRUE)
t7.SetTextSize(0.03)
t7.DrawLatex(0.18 ,0.86 ,"M_{h'} = 2 TeV , M_{q} = %.1f GeV , R = 1.4"%(Mq))
t7.SetTextSize(0.03)
t7.DrawLatex(0.18 ,0.82 ,"M_{\pi} = %.1f GeV , M_{#rho} = %.1f GeV , \Lambda = %.1f GeV"%(m_pion, m_rho, Mq))

# Adding legend

legend7 = ROOT.TLegend(0.55,0.65,0.9,0.9)
legend7.SetTextSize(0.03)
legend7.AddEntry(hist1mt,"N_{f}=%s , N_{c}=%s , Mean = %.1f"%(Nf,Nc1,hist1mt.GetMean()),"l")
legend7.AddEntry(hist2mt,"N_{f}=%s , N_{c}=%s , Mean = %.1f"%(Nf,Nc2,hist2mt.GetMean()),"l")
legend7.AddEntry(hist3mt,"N_{f}=%s , N_{c}=%s , Mean = %.1f"%(Nf,Nc3,hist3mt.GetMean()),"l")
legend7.AddEntry(hist4mt,"N_{f}=%s , N_{c}=%s , Mean = %.1f"%(Nf,Nc4,hist4mt.GetMean()),"l")
legend7.AddEntry(hist5mt,"QCD Z' -> qq~ , Mean = %.1f"%(hist5mt.GetMean()),"l")
legend7.AddEntry(hist6mt,"QCD h' -> gg~ , Mean = %.1f"%(hist6mt.GetMean()),"l")

legend7.SetLineWidth(1)
legend7.Draw()

canvas7.Update()
ROOT.gSystem.ProcessEvents()

#saving the canvas
canvas7.Print("transverse_mass_Nf%s_Mq%.0f.pdf" %(Nf,Mq))

##########################################################################################################################################

# Creating and using eigth canvas; i.e. delta phi1
canvas8 = ROOT.TCanvas("canvas8")
canvas8.cd()

#Plotting histograms on canvas.

hist1dphi1.SetTitle("Difference in phi between leading jet and MET")
hist1dphi1.GetXaxis().SetTitle("\Delta\phi(leading jet and E_{T})")
hist1dphi1.GetYaxis().SetTitle("A.U.")
hist1dphi1.GetXaxis().SetLabelSize(0.04)
hist1dphi1.GetYaxis().SetLabelSize(0.04)
hist1dphi1.GetXaxis().SetTitleSize(0.04)
hist1dphi1.GetYaxis().SetTitleSize(0.04)
hist1dphi1.SetStats(0)
hist1dphi1.SetLineColor(ROOT.kRed)
hist1dphi1.SetLineWidth(2)
hist1dphi1.Draw("hist8")

hist2dphi1.SetLineColor(ROOT.kBlue)
hist2dphi1.SetLineWidth(2)
hist2dphi1.SetStats(0)
hist2dphi1.Draw("hist8 same")
hist1dphi1.GetXaxis().SetRangeUser(0,3.5)
hist1dphi1.GetYaxis().SetRangeUser(0,0.17)
hist1dphi1.GetXaxis().SetTitleOffset(1.4)
hist1dphi1.GetYaxis().SetTitleOffset(1.4)

hist3dphi1.SetLineColor(ROOT.kBlack)
hist3dphi1.SetLineWidth(2)
hist3dphi1.SetStats(0)
hist3dphi1.Draw("hist8 same")
hist4dphi1.SetLineColor(ROOT.kGreen)
hist4dphi1.SetLineWidth(2)
hist4dphi1.SetStats(0)
hist4dphi1.Draw("hist8 same")

hist5dphi1.SetLineColor(7)
hist5dphi1.SetLineStyle(2)
hist5dphi1.SetLineWidth(2)
hist5dphi1.SetStats(0)
hist5dphi1.Draw("hist8 same")

hist6dphi1.SetLineColor(6)
hist6dphi1.SetLineStyle(2)
hist6dphi1.SetLineWidth(2)
hist6dphi1.SetStats(0)
hist6dphi1.Draw("hist8 same")

#setting margins on canvas

canvas8.SetRightMargin(0.09)
canvas8.SetLeftMargin(0.15)
canvas8.SetBottomMargin(0.15)

#adding text on canvas
t8 = ROOT.TLatex()
t8.SetNDC(ROOT.kTRUE)
t8.SetTextSize(0.03)
t8.DrawLatex(0.18 ,0.86 ,"M_{h'} = 2 TeV , M_{q} = %.1f GeV , R = 1.4"%(Mq))
t8.SetTextSize(0.03)
t8.DrawLatex(0.18 ,0.82 ,"M_{\pi} = %.1f GeV , M_{#rho} = %.1f GeV , \Lambda = %.1f GeV"%(m_pion, m_rho, Mq))

# Adding legend

legend8 = ROOT.TLegend(0.55,0.65,0.9,0.9)
legend8.SetTextSize(0.03)
legend8.AddEntry(hist1dphi1,"N_{f}=%s , N_{c}=%s , Mean = %.1f"%(Nf,Nc1,hist1dphi1.GetMean()),"l")
legend8.AddEntry(hist2dphi1,"N_{f}=%s , N_{c}=%s , Mean = %.1f"%(Nf,Nc2,hist2dphi1.GetMean()),"l")
legend8.AddEntry(hist3dphi1,"N_{f}=%s , N_{c}=%s , Mean = %.1f"%(Nf,Nc3,hist3dphi1.GetMean()),"l")
legend8.AddEntry(hist4dphi1,"N_{f}=%s , N_{c}=%s , Mean = %.1f"%(Nf,Nc4,hist4dphi1.GetMean()),"l")
legend8.AddEntry(hist5dphi1,"QCD Z' -> qq~ , Mean = %.1f"%(hist5dphi1.GetMean()),"l")
legend8.AddEntry(hist6dphi1,"QCD h' -> gg~ , Mean = %.1f"%(hist6dphi1.GetMean()),"l")

legend8.SetLineWidth(1)
legend8.Draw()

canvas8.Update()
ROOT.gSystem.ProcessEvents()

#saving the canvas
canvas8.Print("dphi_varyingNc_Nf%s_Mq%.0f.pdf" %(Nf,Mq))

##########################################################################################################################################

# Creating and using ninth canvas; i.e. delta phi2
canvas9 = ROOT.TCanvas("canvas9")
canvas9.cd()

#Plotting histograms on canvas.

hist1dphi2.SetTitle("Difference in phi between sub-leading jet and MET")
hist1dphi2.GetXaxis().SetTitle("\Delta\phi(sub-leading jet and E_{T})")
hist1dphi2.GetYaxis().SetTitle("A.U.")
hist1dphi2.GetXaxis().SetLabelSize(0.04)
hist1dphi2.GetYaxis().SetLabelSize(0.04)
hist1dphi2.GetXaxis().SetTitleSize(0.04)
hist1dphi2.GetYaxis().SetTitleSize(0.04)
hist1dphi2.SetStats(0)
hist1dphi2.SetLineColor(ROOT.kRed)
hist1dphi2.SetLineWidth(2)
hist1dphi2.Draw("hist9")

hist2dphi2.SetLineColor(ROOT.kBlue)
hist2dphi2.SetLineWidth(2)
hist2dphi2.SetStats(0)
hist2dphi2.Draw("hist9 same")
hist1dphi2.GetXaxis().SetRangeUser(0,3.5)
hist1dphi2.GetYaxis().SetRangeUser(0,0.17)
hist1dphi2.GetXaxis().SetTitleOffset(1.4)
hist1dphi2.GetYaxis().SetTitleOffset(1.4)

hist3dphi2.SetLineColor(ROOT.kBlack)
hist3dphi2.SetLineWidth(2)
hist3dphi2.SetStats(0)
hist3dphi2.Draw("hist9 same")

hist4dphi2.SetLineColor(ROOT.kGreen)
hist4dphi2.SetLineWidth(2)
hist4dphi2.SetStats(0)
hist4dphi2.Draw("hist9 same")

hist5dphi2.SetLineColor(7)
hist5dphi2.SetLineStyle(2)
hist5dphi2.SetLineWidth(2)
hist5dphi2.SetStats(0)
hist5dphi2.Draw("hist9 same")

hist6dphi2.SetLineColor(6)
hist6dphi2.SetLineStyle(2)
hist6dphi2.SetLineWidth(2)
hist6dphi2.SetStats(0)
hist6dphi2.Draw("hist9 same")

#setting margins on canvas

canvas9.SetRightMargin(0.09)
canvas9.SetLeftMargin(0.15)
canvas9.SetBottomMargin(0.15)

#adding text on canvas
t9 = ROOT.TLatex()
t9.SetNDC(ROOT.kTRUE)
t9.SetTextSize(0.03)
t9.DrawLatex(0.18 ,0.86 ,"M_{h'} = 2 TeV , M_{q} = %.1f GeV , R = 1.4"%(Mq))
t9.SetTextSize(0.03)
t9.DrawLatex(0.18 ,0.82 ,"M_{\pi} = %.1f GeV , M_{#rho} = %.1f GeV , \Lambda = %.1f GeV"%(m_pion, m_rho, Mq))

# Adding legend

legend9 = ROOT.TLegend(0.55,0.65,0.9,0.9)
legend9.SetTextSize(0.03)
legend9.AddEntry(hist1dphi2,"N_{f}=%s , N_{c}=%s , Mean = %.1f"%(Nf,Nc1,hist1dphi2.GetMean()),"l")
legend9.AddEntry(hist2dphi2,"N_{f}=%s , N_{c}=%s , Mean = %.1f"%(Nf,Nc2,hist2dphi2.GetMean()),"l")
legend9.AddEntry(hist3dphi2,"N_{f}=%s , N_{c}=%s , Mean = %.1f"%(Nf,Nc3,hist3dphi2.GetMean()),"l")
legend9.AddEntry(hist4dphi2,"N_{f}=%s , N_{c}=%s , Mean = %.1f"%(Nf,Nc4,hist4dphi2.GetMean()),"l")
legend9.AddEntry(hist5dphi2,"QCD Z' -> qq~ , Mean = %.1f"%(hist5dphi2.GetMean()),"l")
legend9.AddEntry(hist6dphi2,"QCD h' -> gg~ , Mean = %.1f"%(hist6dphi2.GetMean()),"l")

legend9.SetLineWidth(1)
legend9.Draw()

canvas9.Update()
ROOT.gSystem.ProcessEvents()

#saving the canvas
canvas9.Print("dphi_varyingNc_Nf%s_Mq%.0f.pdf" %(Nf,Mq))

#######################################################################################################################################################

# Creating and using tenth canvas; i.e rt

canvas10 = ROOT.TCanvas("canvas10")
canvas10.cd()

#Plotting histograms on canvas.

hist1rt.SetTitle("Ratio of missing transverse momentum and transverse mass")
hist1rt.GetXaxis().SetTitle("transverse ratio")
hist1rt.GetYaxis().SetTitle("A.U.")
hist1rt.GetXaxis().SetLabelSize(0.04)
hist1rt.GetYaxis().SetLabelSize(0.04)
hist1rt.GetXaxis().SetTitleSize(0.04)
hist1rt.GetYaxis().SetTitleSize(0.04)
hist1rt.SetStats(0)
hist1rt.SetLineColor(ROOT.kRed)
hist1rt.SetLineWidth(2)
hist1rt.Draw("hist10")

hist2rt.SetLineColor(ROOT.kBlue)
hist2rt.SetLineWidth(2)
hist2rt.SetStats(0)
hist2rt.Draw("hist10 same")
hist1rt.GetXaxis().SetRangeUser(0,0.5)
hist1rt.GetYaxis().SetRangeUser(0.0000001, 100)
hist1rt.GetXaxis().SetTitleOffset(1.4)
hist1rt.GetYaxis().SetTitleOffset(1.4)

hist3rt.SetLineColor(ROOT.kBlack)
hist3rt.SetLineWidth(2)
hist3rt.SetStats(0)
hist3rt.Draw("hist10 same")

hist4rt.SetLineColor(ROOT.kGreen)
hist4rt.SetLineWidth(2)
hist4rt.SetStats(0)
hist4rt.Draw("hist10 same")

hist5rt.SetLineColor(7)
hist5rt.SetLineStyle(2)
hist5rt.SetLineWidth(2)
hist5rt.SetStats(0)
hist5rt.Draw("hist10 same")

hist6rt.SetLineColor(6)
hist6rt.SetLineStyle(2)
hist6rt.SetLineWidth(2)
hist6rt.SetStats(0)
hist6rt.Draw("hist10 same")

#setting margins on canvas
canvas10.SetLogy()
canvas10.SetRightMargin(0.09)
canvas10.SetLeftMargin(0.15)
canvas10.SetBottomMargin(0.15)

#adding text on canvas
t10 = ROOT.TLatex()
t10.SetNDC(ROOT.kTRUE)
t10.SetTextSize(0.03)
t10.DrawLatex(0.18 ,0.86 ,"M_{h'} = 2 TeV , M_{q} = %.1f GeV , R = 1.4"%(Mq))
t10.SetTextSize(0.03)
t10.DrawLatex(0.18 ,0.82 ,"M_{\pi} = %.1f GeV , M_{#rho} = %.1f GeV , \Lambda = %.1f GeV"%(m_pion, m_rho, Mq))

# Adding legend

legend10 = ROOT.TLegend(0.55,0.65,0.9,0.9)
legend10.SetTextSize(0.03)
legend10.AddEntry(hist1rt,"N_{f}=%s , N_{c}=%s , Mean = %.1f"%(Nf,Nc1,hist1rt.GetMean()),"l")
legend10.AddEntry(hist2rt,"N_{f}=%s , N_{c}=%s , Mean = %.1f"%(Nf,Nc2,hist2rt.GetMean()),"l")
legend10.AddEntry(hist3rt,"N_{f}=%s , N_{c}=%s , Mean = %.1f"%(Nf,Nc3,hist3rt.GetMean()),"l")
legend10.AddEntry(hist4rt,"N_{f}=%s , N_{c}=%s , Mean = %.1f"%(Nf,Nc4,hist4rt.GetMean()),"l")
legend10.AddEntry(hist5rt,"QCD Z' -> qq~ , Mean = %.1f"%(hist5rt.GetMean()),"l")
legend10.AddEntry(hist6rt,"QCD h' -> gg~ , Mean = %.1f"%(hist6rt.GetMean()),"l")

legend10.SetLineWidth(1)
legend10.Draw()

canvas10.Update()
ROOT.gSystem.ProcessEvents()

#saving the canvas
canvas10.Print("rt_varyingNc_Nf%s_Mq%.0f.pdf" %(Nf,Mq))

####################################################################################################################################################

# Creating and using eleventh canvas; i.e. jet1 softdrop for Nf,Nc1

canvas11 = ROOT.TCanvas("canvas11")
canvas11.cd()

#Plotting histograms on canvas.

hist1jet1PT_softdrop.SetTitle("Transverse momentum of leading jet")
hist1jet1PT_softdrop.GetXaxis().SetTitle("p_{T} (leading jet) [GeV]")
hist1jet1PT_softdrop.GetYaxis().SetTitle("A.U.")
hist1jet1PT_softdrop.GetXaxis().SetLabelSize(0.04)
hist1jet1PT_softdrop.GetYaxis().SetLabelSize(0.04)
hist1jet1PT_softdrop.GetXaxis().SetTitleSize(0.04)
hist1jet1PT_softdrop.GetYaxis().SetTitleSize(0.04)
hist1jet1PT_softdrop.SetStats(0)
hist1jet1PT_softdrop.SetLineColor(ROOT.kBlue)
hist1jet1PT_softdrop.SetLineWidth(2)
hist1jet1PT_softdrop.Draw("hist11")

hist1jet1PT.SetLineColor(ROOT.kRed)
hist1jet1PT.SetLineWidth(2)
hist1jet1PT.SetStats(0)
hist1jet1PT.Draw("hist11 same")
hist1jet1PT_softdrop.GetXaxis().SetRangeUser(0,1200)
hist1jet1PT_softdrop.GetYaxis().SetRangeUser(0,0.18)
hist1jet1PT_softdrop.GetXaxis().SetTitleOffset(1.4)
hist1jet1PT_softdrop.GetYaxis().SetTitleOffset(1.4)

hist1jet1PT_trimmed.SetLineColor(ROOT.kBlack)
hist1jet1PT_trimmed.SetLineWidth(2)
hist1jet1PT_trimmed.SetStats(0)
hist1jet1PT_trimmed.Draw("hist11 same")

canvas11.SetRightMargin(0.09)
canvas11.SetLeftMargin(0.15)
canvas11.SetBottomMargin(0.15)

#adding text on canvas
t11 = ROOT.TLatex()
t11.SetNDC(ROOT.kTRUE)
t11.SetTextSize(0.03)
t11.DrawLatex(0.18 ,0.86 ,"M_{h'} = 2 TeV , M_{q} = %.1f GeV , \Lambda = %.1f GeV"%(Mq,Mq))
t11.SetTextSize(0.03)
t11.DrawLatex(0.18 ,0.82 ,"M_{\pi} = %.1f GeV , M_{#rho} = %.1f GeV"%(m_pion, m_rho))
t11.SetTextSize(0.03)
t11.DrawLatex(0.18 , 0.78 , "N_{f} = %s , N_{c} = %s " %(Nf,Nc1))

#Adding legend on third canvas

legend11 = ROOT.TLegend(0.55,0.75,0.9,0.9)
legend11.SetTextSize(0.03)
legend11.AddEntry(hist1jet1PT,"Ungroomed , Mean = %.1f"%(hist1jet1PT.GetMean()),"l")
legend11.AddEntry(hist1jet1PT_trimmed,"Trimmed , Mean = %.1f"%(hist1jet1PT_trimmed.GetMean()),"l")
legend11.AddEntry(hist1jet1PT_softdrop,"Softdropped , Mean = %.1f"%(hist1jet1PT_softdrop.GetMean()),"l")
legend11.SetLineWidth(1)
legend11.Draw()

canvas11.Update()
ROOT.gSystem.ProcessEvents()

#Saving the canvas
canvas11.Print("ptj1_groomed_Nf%s_Nc%s_Mq%.0f.pdf"%(Nf,Nc1,Mq))

##############################################################################################################################################################################

# Creating and using twelfth canvas; i.e. mjj softdrop for Nf,Nc1

canvas12 = ROOT.TCanvas("canvas12")
canvas12.cd()

#Plotting histograms on canvas.

hist1mjj_softdrop.SetTitle("Invariant mass")
hist1mjj_softdrop.GetXaxis().SetTitle("Invariant mass [GeV]")
hist1mjj_softdrop.GetYaxis().SetTitle("A.U.")
hist1mjj_softdrop.GetXaxis().SetLabelSize(0.04)
hist1mjj_softdrop.GetYaxis().SetLabelSize(0.04)
hist1mjj_softdrop.GetXaxis().SetTitleSize(0.04)
hist1mjj_softdrop.GetYaxis().SetTitleSize(0.04)
hist1mjj_softdrop.SetStats(0)
hist1mjj_softdrop.SetLineColor(ROOT.kBlue)
hist1mjj_softdrop.SetLineWidth(2)
hist1mjj_softdrop.Draw("hist12")

hist1mjj.SetLineColor(ROOT.kRed)
hist1mjj.SetLineWidth(2)
hist1mjj.SetStats(0)
hist1mjj.Draw("hist12 same")
hist1mjj_softdrop.GetXaxis().SetRangeUser(0,2500)
hist1mjj_softdrop.GetYaxis().SetRangeUser(0,0.14)
hist1mjj_softdrop.GetXaxis().SetTitleOffset(1.4)
hist1mjj_softdrop.GetYaxis().SetTitleOffset(1.4)

hist1mjj_trimmed.SetLineColor(ROOT.kBlack)
hist1mjj_trimmed.SetLineWidth(2)
hist1mjj_trimmed.SetStats(0)
hist1mjj_trimmed.Draw("hist12 same")

canvas12.SetRightMargin(0.09)
canvas12.SetLeftMargin(0.15)
canvas12.SetBottomMargin(0.15)

#adding text on canvas
t12 = ROOT.TLatex()
t12.SetNDC(ROOT.kTRUE)
t12.SetTextSize(0.03)
t12.DrawLatex(0.18 ,0.86 ,"M_{h'} = 2 TeV , M_{q} = %.1f GeV , \Lambda = %.1f GeV"%(Mq,Mq))
t12.SetTextSize(0.03)
t12.DrawLatex(0.18 ,0.82 ,"M_{\pi} = %.1f GeV , M_{#rho} = %.1f GeV"%(m_pion, m_rho))
t12.SetTextSize(0.03)
t12.DrawLatex(0.18 , 0.78 , "N_{f} = %s , N_{c} = %s " %(Nf,Nc1))

#Adding legend on third canvas

legend12 = ROOT.TLegend(0.55,0.75,0.9,0.9)
legend12.SetTextSize(0.03)
legend12.AddEntry(hist1mjj,"Ungroomed , Mean = %.1f"%(hist1mjj.GetMean()),"l")
legend12.AddEntry(hist1mjj_trimmed,"Trimmed , Mean = %.1f"%(hist1mjj_trimmed.GetMean()),"l")
legend12.AddEntry(hist1mjj_softdrop,"Softdropped , Mean = %.1f"%(hist1mjj_softdrop.GetMean()),"l")
legend12.SetLineWidth(1)
legend12.Draw()

canvas12.Update()
ROOT.gSystem.ProcessEvents()

#Saving the canvas
canvas12.Print("mjj_groomed_Nf%s_Nc%s_Mq%.0f.pdf"%(Nf,Nc1,Mq))

##########################################################################################################################################################


# Creating and using thirteenth canvas; i.e. jet1 softdrop for Nf,Nc2

canvas13 = ROOT.TCanvas("canvas13")
canvas13.cd()

#Plotting histograms on canvas.

hist2jet1PT_softdrop.SetTitle("Transverse momentum of leading jet")
hist2jet1PT_softdrop.GetXaxis().SetTitle("p_{T} (leading jet) [GeV]")
hist2jet1PT_softdrop.GetYaxis().SetTitle("A.U.")
hist2jet1PT_softdrop.GetXaxis().SetLabelSize(0.04)
hist2jet1PT_softdrop.GetYaxis().SetLabelSize(0.04)
hist2jet1PT_softdrop.GetXaxis().SetTitleSize(0.04)
hist2jet1PT_softdrop.GetYaxis().SetTitleSize(0.04)
hist2jet1PT_softdrop.SetStats(0)
hist2jet1PT_softdrop.SetLineColor(ROOT.kBlue)
hist2jet1PT_softdrop.SetLineWidth(2)
hist2jet1PT_softdrop.Draw("hist13")

hist2jet1PT.SetLineColor(ROOT.kRed)
hist2jet1PT.SetLineWidth(2)
hist2jet1PT.SetStats(0)
hist2jet1PT.Draw("hist13 same")
hist2jet1PT_softdrop.GetXaxis().SetRangeUser(0,1200)
hist2jet1PT_softdrop.GetYaxis().SetRangeUser(0,0.18)
hist2jet1PT_softdrop.GetXaxis().SetTitleOffset(1.4)
hist2jet1PT_softdrop.GetYaxis().SetTitleOffset(1.4)

hist2jet1PT_trimmed.SetLineColor(ROOT.kBlack)
hist2jet1PT_trimmed.SetLineWidth(2)
hist2jet1PT_trimmed.SetStats(0)
hist2jet1PT_trimmed.Draw("hist13 same")

canvas13.SetRightMargin(0.09)
canvas13.SetLeftMargin(0.15)
canvas13.SetBottomMargin(0.15)

#adding text on canvas
t13 = ROOT.TLatex()
t13.SetNDC(ROOT.kTRUE)
t13.SetTextSize(0.03)
t13.DrawLatex(0.18 ,0.86 ,"M_{h'} = 2 TeV , M_{q} = %.1f GeV , \Lambda = %.1f GeV"%(Mq,Mq))
t13.SetTextSize(0.03)
t13.DrawLatex(0.18 ,0.82 ,"M_{\pi} = %.1f GeV , M_{#rho} = %.1f GeV"%(m_pion, m_rho))
t13.SetTextSize(0.03)
t13.DrawLatex(0.18 , 0.78 , "N_{f} = %s , N_{c} = %s " %(Nf,Nc2))

#Adding legend on canvas

legend13 = ROOT.TLegend(0.55,0.75,0.9,0.9)
legend13.SetTextSize(0.03)
legend13.AddEntry(hist2jet1PT,"Ungroomed , Mean = %.1f"%(hist2jet1PT.GetMean()),"l")
legend13.AddEntry(hist2jet1PT_trimmed,"Trimmed , Mean = %.1f"%(hist2jet1PT_trimmed.GetMean()),"l")
legend13.AddEntry(hist2jet1PT_softdrop,"Softdropped , Mean = %.1f"%(hist2jet1PT_softdrop.GetMean()),"l")
legend13.SetLineWidth(1)
legend13.Draw()

canvas13.Update()
ROOT.gSystem.ProcessEvents()

#Saving the canvas
canvas13.Print("ptj1_groomed_Nf%s_Nc%s_Mq%.0f.pdf"%(Nf,Nc2,Mq))

##############################################################################################################################################################################

# Creating and using fourteenth canvas; i.e. mjj softdrop for Nf,Nc2

canvas14 = ROOT.TCanvas("canvas14")
canvas14.cd()

#Plotting histograms on canvas.

hist2mjj_softdrop.SetTitle("Invariant mass")
hist2mjj_softdrop.GetXaxis().SetTitle("Invariant mass [GeV]")
hist2mjj_softdrop.GetYaxis().SetTitle("A.U.")
hist2mjj_softdrop.GetXaxis().SetLabelSize(0.04)
hist2mjj_softdrop.GetYaxis().SetLabelSize(0.04)
hist2mjj_softdrop.GetXaxis().SetTitleSize(0.04)
hist2mjj_softdrop.GetYaxis().SetTitleSize(0.04)
hist2mjj_softdrop.SetStats(0)
hist2mjj_softdrop.SetLineColor(ROOT.kBlue)
hist2mjj_softdrop.SetLineWidth(2)
hist2mjj_softdrop.Draw("hist14")

hist2mjj.SetLineColor(ROOT.kRed)
hist2mjj.SetLineWidth(2)
hist2mjj.SetStats(0)
hist2mjj.Draw("hist14 same")
hist2mjj_softdrop.GetXaxis().SetRangeUser(0,2500)
hist2mjj_softdrop.GetYaxis().SetRangeUser(0,0.14)
hist2mjj_softdrop.GetXaxis().SetTitleOffset(1.4)
hist2mjj_softdrop.GetYaxis().SetTitleOffset(1.4)

hist2mjj_trimmed.SetLineColor(ROOT.kBlack)
hist2mjj_trimmed.SetLineWidth(2)
hist2mjj_trimmed.SetStats(0)
hist2mjj_trimmed.Draw("hist14 same")

canvas14.SetRightMargin(0.09)
canvas14.SetLeftMargin(0.15)
canvas14.SetBottomMargin(0.15)

#adding text on canvas
t14 = ROOT.TLatex()
t14.SetNDC(ROOT.kTRUE)
t14.SetTextSize(0.03)
t14.DrawLatex(0.18 ,0.86 ,"M_{h'} = 2 TeV , M_{q} = %.1f GeV , \Lambda = %.1f GeV"%(Mq,Mq))
t14.SetTextSize(0.03)
t14.DrawLatex(0.18 ,0.82 ,"M_{\pi} = %.1f GeV , M_{#rho} = %.1f GeV"%(m_pion, m_rho))
t14.SetTextSize(0.03)
t14.DrawLatex(0.18 , 0.78 , "N_{f} = %s , N_{c} = %s " %(Nf,Nc2))

#Adding legend on canvas

legend14 = ROOT.TLegend(0.55,0.75,0.9,0.9)
legend14.SetTextSize(0.03)
legend14.AddEntry(hist2mjj,"Ungroomed , Mean = %.1f"%(hist2mjj.GetMean()),"l")
legend14.AddEntry(hist2mjj_trimmed,"Trimmed , Mean = %.1f"%(hist2mjj_trimmed.GetMean()),"l")
legend14.AddEntry(hist2mjj_softdrop,"Softdropped , Mean = %.1f"%(hist2mjj_softdrop.GetMean()),"l")
legend14.SetLineWidth(1)
legend14.Draw()

canvas14.Update()
ROOT.gSystem.ProcessEvents()

#Saving the canvas
canvas14.Print("mjj_groomed_Nf%s_Nc%s_Mq%.0f.pdf"%(Nf,Nc2,Mq))
########################################################################################################################################
# Creating and using fifteenth canvas; i.e. jet1 softdrop for Nf,Nc3

canvas15 = ROOT.TCanvas("canvas15")
canvas15.cd()

#Plotting histograms on canvas.

hist3jet1PT_softdrop.SetTitle("Transverse momentum of leading jet")
hist3jet1PT_softdrop.GetXaxis().SetTitle("p_{T} (leading jet) [GeV]")
hist3jet1PT_softdrop.GetYaxis().SetTitle("A.U.")
hist3jet1PT_softdrop.GetXaxis().SetLabelSize(0.04)
hist3jet1PT_softdrop.GetYaxis().SetLabelSize(0.04)
hist3jet1PT_softdrop.GetXaxis().SetTitleSize(0.04)
hist3jet1PT_softdrop.GetYaxis().SetTitleSize(0.04)
hist3jet1PT_softdrop.SetStats(0)
hist3jet1PT_softdrop.SetLineColor(ROOT.kBlue)
hist3jet1PT_softdrop.SetLineWidth(2)
hist3jet1PT_softdrop.Draw("hist15")

hist3jet1PT.SetLineColor(ROOT.kRed)
hist3jet1PT.SetLineWidth(2)
hist3jet1PT.SetStats(0)
hist3jet1PT.Draw("hist15 same")
hist3jet1PT_softdrop.GetXaxis().SetRangeUser(0,1200)
hist3jet1PT_softdrop.GetYaxis().SetRangeUser(0,0.18)
hist3jet1PT_softdrop.GetXaxis().SetTitleOffset(1.4)
hist3jet1PT_softdrop.GetYaxis().SetTitleOffset(1.4)

hist3jet1PT_trimmed.SetLineColor(ROOT.kBlack)
hist3jet1PT_trimmed.SetLineWidth(2)
hist3jet1PT_trimmed.SetStats(0)
hist3jet1PT_trimmed.Draw("hist15 same")

canvas15.SetRightMargin(0.09)
canvas15.SetLeftMargin(0.15)
canvas15.SetBottomMargin(0.15)

#adding text on canvas
t15 = ROOT.TLatex()
t15.SetNDC(ROOT.kTRUE)
t15.SetTextSize(0.03)
t15.DrawLatex(0.18 ,0.86 ,"M_{h'} = 2 TeV , M_{q} = %.1f GeV , \Lambda = %.1f GeV"%(Mq,Mq))
t15.SetTextSize(0.03)
t15.DrawLatex(0.18 ,0.82 ,"M_{\pi} = %.1f GeV , M_{#rho} = %.1f GeV"%(m_pion, m_rho))
t15.SetTextSize(0.03)
t15.DrawLatex(0.18 , 0.78 , "N_{f} = %s , N_{c} = %s " %(Nf,Nc3))

#Adding legend on canvas

legend15 = ROOT.TLegend(0.55,0.75,0.9,0.9)
legend15.SetTextSize(0.03)
legend15.AddEntry(hist3jet1PT,"Ungroomed , Mean = %.1f"%(hist3jet1PT.GetMean()),"l")
legend15.AddEntry(hist3jet1PT_trimmed,"Trimmed , Mean = %.1f"%(hist3jet1PT_trimmed.GetMean()),"l")
legend15.AddEntry(hist3jet1PT_softdrop,"Softdropped , Mean = %.1f"%(hist3jet1PT_softdrop.GetMean()),"l")
legend15.SetLineWidth(1)
legend15.Draw()

canvas15.Update()
ROOT.gSystem.ProcessEvents()

#Saving the canvas
canvas15.Print("ptj1_groomed_Nf%s_Nc%s_Mq%.0f.pdf"%(Nf,Nc3,Mq))

##############################################################################################################################################################################

# Creating and using sixteenth canvas; i.e. mjj softdrop for Nf,Nc2

canvas16 = ROOT.TCanvas("canvas16")
canvas16.cd()

#Plotting histograms on canvas.

hist3mjj_softdrop.SetTitle("Invariant mass")
hist3mjj_softdrop.GetXaxis().SetTitle("Invariant mass [GeV]")
hist3mjj_softdrop.GetYaxis().SetTitle("A.U.")
hist3mjj_softdrop.GetXaxis().SetLabelSize(0.04)
hist3mjj_softdrop.GetYaxis().SetLabelSize(0.04)
hist3mjj_softdrop.GetXaxis().SetTitleSize(0.04)
hist3mjj_softdrop.GetYaxis().SetTitleSize(0.04)
hist3mjj_softdrop.SetStats(0)
hist3mjj_softdrop.SetLineColor(ROOT.kBlue)
hist3mjj_softdrop.SetLineWidth(2)
hist3mjj_softdrop.Draw("hist16")

hist3mjj.SetLineColor(ROOT.kRed)
hist3mjj.SetLineWidth(2)
hist3mjj.SetStats(0)
hist3mjj.Draw("hist16 same")
hist3mjj_softdrop.GetXaxis().SetRangeUser(0,2500)
hist3mjj_softdrop.GetYaxis().SetRangeUser(0,0.14)
hist3mjj_softdrop.GetXaxis().SetTitleOffset(1.4)
hist3mjj_softdrop.GetYaxis().SetTitleOffset(1.4)

hist3mjj_trimmed.SetLineColor(ROOT.kBlack)
hist3mjj_trimmed.SetLineWidth(2)
hist3mjj_trimmed.SetStats(0)
hist3mjj_trimmed.Draw("hist16 same")

canvas16.SetRightMargin(0.09)
canvas16.SetLeftMargin(0.15)
canvas16.SetBottomMargin(0.15)

#adding text on canvas
t16 = ROOT.TLatex()
t16.SetNDC(ROOT.kTRUE)
t16.SetTextSize(0.03)
t16.DrawLatex(0.18 ,0.86 ,"M_{h'} = 2 TeV , M_{q} = %.1f GeV , \Lambda = %.1f GeV"%(Mq,Mq))
t16.SetTextSize(0.03)
t16.DrawLatex(0.18 ,0.82 ,"M_{\pi} = %.1f GeV , M_{#rho} = %.1f GeV"%(m_pion, m_rho))
t16.SetTextSize(0.03)
t16.DrawLatex(0.18 , 0.78 , "N_{f} = %s , N_{c} = %s " %(Nf,Nc3))

#Adding legend on canvas

legend16 = ROOT.TLegend(0.55,0.75,0.9,0.9)
legend16.SetTextSize(0.03)
legend16.AddEntry(hist3mjj,"Ungroomed , Mean = %.1f"%(hist3mjj.GetMean()),"l")
legend16.AddEntry(hist3mjj_trimmed,"Trimmed , Mean = %.1f"%(hist3mjj_trimmed.GetMean()),"l")
legend16.AddEntry(hist3mjj_softdrop,"Softdropped , Mean = %.1f"%(hist3mjj_softdrop.GetMean()),"l")
legend16.SetLineWidth(1)
legend16.Draw()

canvas16.Update()
ROOT.gSystem.ProcessEvents()

#Saving the canvas
canvas16.Print("mjj_groomed_Nf%s_Nc%s_Mq%.0f.pdf"%(Nf,Nc3,Mq))
########################################################################################################################################
# Creating and using seventeenth canvas; i.e. jet1 softdrop for Nf,Nc4

canvas17 = ROOT.TCanvas("canvas17")
canvas17.cd()

#Plotting histograms on canvas.

hist4jet1PT_softdrop.SetTitle("Transverse momentum of leading jet")
hist4jet1PT_softdrop.GetXaxis().SetTitle("p_{T} (leading jet) [GeV]")
hist4jet1PT_softdrop.GetYaxis().SetTitle("A.U.")
hist4jet1PT_softdrop.GetXaxis().SetLabelSize(0.04)
hist4jet1PT_softdrop.GetYaxis().SetLabelSize(0.04)
hist4jet1PT_softdrop.GetXaxis().SetTitleSize(0.04)
hist4jet1PT_softdrop.GetYaxis().SetTitleSize(0.04)
hist4jet1PT_softdrop.SetStats(0)
hist4jet1PT_softdrop.SetLineColor(ROOT.kBlue)
hist4jet1PT_softdrop.SetLineWidth(2)
hist4jet1PT_softdrop.Draw("hist17")

hist4jet1PT.SetLineColor(ROOT.kRed)
hist4jet1PT.SetLineWidth(2)
hist4jet1PT.SetStats(0)
hist4jet1PT.Draw("hist17 same")
hist4jet1PT_softdrop.GetXaxis().SetRangeUser(0,1200)
hist4jet1PT_softdrop.GetYaxis().SetRangeUser(0,0.18)
hist4jet1PT_softdrop.GetXaxis().SetTitleOffset(1.4)
hist4jet1PT_softdrop.GetYaxis().SetTitleOffset(1.4)

hist4jet1PT_trimmed.SetLineColor(ROOT.kBlack)
hist4jet1PT_trimmed.SetLineWidth(2)
hist4jet1PT_trimmed.SetStats(0)
hist4jet1PT_trimmed.Draw("hist17 same")

canvas17.SetRightMargin(0.09)
canvas17.SetLeftMargin(0.15)
canvas17.SetBottomMargin(0.15)

#adding text on canvas
t17 = ROOT.TLatex()
t17.SetNDC(ROOT.kTRUE)
t17.SetTextSize(0.03)
t17.DrawLatex(0.18 ,0.86 ,"M_{h'} = 2 TeV , M_{q} = %.1f GeV , \Lambda = %.1f GeV"%(Mq,Mq))
t17.SetTextSize(0.03)
t17.DrawLatex(0.18 ,0.82 ,"M_{\pi} = %.1f GeV , M_{#rho} = %.1f GeV"%(m_pion, m_rho))
t17.SetTextSize(0.03)
t17.DrawLatex(0.18 , 0.78 , "N_{f} = %s , N_{c} = %s " %(Nf,Nc4))

#Adding legend on canvas

legend17 = ROOT.TLegend(0.55,0.75,0.9,0.9)
legend17.SetTextSize(0.03)
legend17.AddEntry(hist4jet1PT,"Ungroomed , Mean = %.1f"%(hist4jet1PT.GetMean()),"l")
legend17.AddEntry(hist4jet1PT_trimmed,"Trimmed , Mean = %.1f"%(hist4jet1PT_trimmed.GetMean()),"l")
legend17.AddEntry(hist4jet1PT_softdrop,"Softdropped , Mean = %.1f"%(hist4jet1PT_softdrop.GetMean()),"l")
legend17.SetLineWidth(1)
legend17.Draw()

canvas17.Update()
ROOT.gSystem.ProcessEvents()

#Saving the canvas
canvas17.Print("ptj1_groomed_Nf%s_Nc%s_Mq%.0f.pdf"%(Nf,Nc4,Mq))

##############################################################################################################################################################################

# Creating and using eighteenth canvas; i.e. mjj softdrop for Nf,Nc4

canvas18 = ROOT.TCanvas("canvas18")
canvas18.cd()

#Plotting histograms on canvas.

hist4mjj_softdrop.SetTitle("Invariant mass")
hist4mjj_softdrop.GetXaxis().SetTitle("Invariant mass [GeV]")
hist4mjj_softdrop.GetYaxis().SetTitle("A.U.")
hist4mjj_softdrop.GetXaxis().SetLabelSize(0.04)
hist4mjj_softdrop.GetYaxis().SetLabelSize(0.04)
hist4mjj_softdrop.GetXaxis().SetTitleSize(0.04)
hist4mjj_softdrop.GetYaxis().SetTitleSize(0.04)
hist4mjj_softdrop.SetStats(0)
hist4mjj_softdrop.SetLineColor(ROOT.kBlue)
hist4mjj_softdrop.SetLineWidth(2)
hist4mjj_softdrop.Draw("hist18")

hist4mjj.SetLineColor(ROOT.kRed)
hist4mjj.SetLineWidth(2)
hist4mjj.SetStats(0)
hist4mjj.Draw("hist18 same")
hist4mjj_softdrop.GetXaxis().SetRangeUser(0,2500)
hist4mjj_softdrop.GetYaxis().SetRangeUser(0,0.14)
hist4mjj_softdrop.GetXaxis().SetTitleOffset(1.4)
hist4mjj_softdrop.GetYaxis().SetTitleOffset(1.4)

hist4mjj_trimmed.SetLineColor(ROOT.kBlack)
hist4mjj_trimmed.SetLineWidth(2)
hist4mjj_trimmed.SetStats(0)
hist4mjj_trimmed.Draw("hist18 same")

canvas18.SetRightMargin(0.09)
canvas18.SetLeftMargin(0.15)
canvas18.SetBottomMargin(0.15)

#adding text on canvas
t18 = ROOT.TLatex()
t18.SetNDC(ROOT.kTRUE)
t18.SetTextSize(0.03)
t18.DrawLatex(0.18 ,0.86 ,"M_{h'} = 2 TeV , M_{q} = %.1f GeV , \Lambda = %.1f GeV"%(Mq,Mq))
t18.SetTextSize(0.03)
t18.DrawLatex(0.18 ,0.82 ,"M_{\pi} = %.1f GeV , M_{#rho} = %.1f GeV"%(m_pion, m_rho))
t18.SetTextSize(0.03)
t18.DrawLatex(0.18 , 0.78 , "N_{f} = %s , N_{c} = %s " %(Nf,Nc4))

#Adding legend on canvas

legend18 = ROOT.TLegend(0.55,0.75,0.9,0.9)
legend18.SetTextSize(0.03)
legend18.AddEntry(hist4mjj,"Ungroomed , Mean = %.1f"%(hist4mjj.GetMean()),"l")
legend18.AddEntry(hist4mjj_trimmed,"Trimmed , Mean = %.1f"%(hist4mjj_trimmed.GetMean()),"l")
legend18.AddEntry(hist4mjj_softdrop,"Softdropped , Mean = %.1f"%(hist4mjj_softdrop.GetMean()),"l")
legend18.SetLineWidth(1)
legend18.Draw()

canvas18.Update()
ROOT.gSystem.ProcessEvents()

#Saving the canvas
canvas18.Print("mjj_groomed_Nf%s_Nc%s_Mq%.0f.pdf"%(Nf,Nc4,Mq))
########################################################################################################################################

# Creating and using nineteenth canvas; i.e. track pt for Nf, Nc1

canvas19 = ROOT.TCanvas("canvas19")
canvas19.cd()

#Plotting histograms on canvas.

hist1track_pt.GetXaxis().SetTitle('p_{T} of tracks in leading jet')
hist1track_pt.GetYaxis().SetTitle('ntrk1')
hist1track_pt.SetStats(0)

hist1track_pt.GetYaxis().SetLabelSize(0.04)
hist1track_pt.GetYaxis().SetTitleSize(0.04)
hist1track_pt.GetXaxis().SetTitleSize(0.04)
hist1track_pt.GetXaxis().SetLabelSize(0.04)
hist1track_pt.SetTitle("Average track transverse momentum")
hist1track_pt.Draw('colZ')

hist1track_pt.GetYaxis().SetRangeUser(0,300)
hist1track_pt.GetXaxis().SetRangeUser(0,40)
hist1track_pt.GetXaxis().SetTitleOffset(1.4)
hist1track_pt.GetYaxis().SetTitleOffset(1.4)

# Set margins

canvas19.SetRightMargin(0.15)
canvas19.SetLeftMargin(0.15)
canvas19.SetBottomMargin(0.15)

# Add text to canvas

t19 = ROOT.TLatex()
t19.SetNDC(ROOT.kTRUE)
t19.SetTextSize(0.03)
t19.DrawLatex(0.18 ,0.86 ,"M_{h'} = 2 TeV , M_{q} = %.1f GeV , \Lambda = %.1f GeV"%(Mq,Mq))
t19.SetTextSize(0.03)
t19.DrawLatex(0.18 ,0.82 ,"M_{\pi} = %.1f GeV , M_{#rho} = %.1f GeV"%(m_pion, m_rho))
t19.SetTextSize(0.03)
t19.DrawLatex(0.18 , 0.78 , "N_{f} = %s , N_{c} = %s " %(Nf,Nc1))

# Add legend

legend19 = ROOT.TLegend(0.7,0.8,0.85,0.9)
legend19.SetFillStyle(1001)
legend19.SetLineWidth(1)
legend19.SetFillColor(0)
legend19.SetTextSize(0.03)
legend19.AddEntry(hist1track_pt,"Nf=%s,Nc=%s"%(Nf,Nc1))
legend19.Draw('same')

canvas19.Print("trackpt_Nf%s_Nc%s_Mq%.0f.pdf"%(Nf,Nc1,Mq))

########################################################################################################################################

# Creating and using twentieth canvas; i.e. track pt for Nf, Nc2

canvas20 = ROOT.TCanvas("canvas20")
canvas20.cd()

#Plotting histograms on canvas.

hist2track_pt.GetXaxis().SetTitle('p_{T} of tracks in leading jet')
hist2track_pt.GetYaxis().SetTitle('ntrk1')
hist2track_pt.SetStats(0)

hist2track_pt.GetYaxis().SetLabelSize(0.04)
hist2track_pt.GetYaxis().SetTitleSize(0.04)
hist2track_pt.GetXaxis().SetTitleSize(0.04)
hist2track_pt.GetXaxis().SetLabelSize(0.04)
hist2track_pt.SetTitle("Average track transverse momentum")
hist2track_pt.Draw('colZ')

hist2track_pt.GetYaxis().SetRangeUser(0,300)
hist2track_pt.GetXaxis().SetRangeUser(0,40)
hist2track_pt.GetXaxis().SetTitleOffset(1.4)
hist2track_pt.GetYaxis().SetTitleOffset(1.4)

# Set margins

canvas20.SetRightMargin(0.15)
canvas20.SetLeftMargin(0.15)
canvas20.SetBottomMargin(0.15)

# Add text to canvas

t20 = ROOT.TLatex()
t20.SetNDC(ROOT.kTRUE)
t20.SetTextSize(0.03)
t20.DrawLatex(0.18 ,0.86 ,"M_{h'} = 2 TeV , M_{q} = %.1f GeV , \Lambda = %.1f GeV"%(Mq,Mq))
t20.SetTextSize(0.03)
t20.DrawLatex(0.18 ,0.82 ,"M_{\pi} = %.1f GeV , M_{#rho} = %.1f GeV"%(m_pion, m_rho))
t20.SetTextSize(0.03)
t20.DrawLatex(0.18 , 0.78 , "N_{f} = %s , N_{c} = %s " %(Nf,Nc2))

# Add legend

legend20 = ROOT.TLegend(0.7,0.8,0.85,0.9)
legend20.SetFillStyle(1001)
legend20.SetLineWidth(1)
legend20.SetFillColor(0)
legend20.SetTextSize(0.03)
legend20.AddEntry(hist2track_pt,"Nf=%s,Nc=%s"%(Nf,Nc2))
legend20.Draw('same')

canvas20.Print("trackpt_Nf%s_Nc%s_Mq%.0f.pdf"%(Nf,Nc2,Mq))

########################################################################################################################################

# Creating and using 21st canvas; i.e. track pt for Nf, Nc3

canvas21 = ROOT.TCanvas("canvas21")
canvas21.cd()

#Plotting histograms on canvas.

hist3track_pt.GetXaxis().SetTitle('p_{T} of tracks in leading jet')
hist3track_pt.GetYaxis().SetTitle('ntrk1')
hist3track_pt.SetStats(0)

hist3track_pt.GetYaxis().SetLabelSize(0.04)
hist3track_pt.GetYaxis().SetTitleSize(0.04)
hist3track_pt.GetXaxis().SetTitleSize(0.04)
hist3track_pt.GetXaxis().SetLabelSize(0.04)
hist3track_pt.SetTitle("Average track transverse momentum")
hist3track_pt.Draw('colZ')

hist3track_pt.GetYaxis().SetRangeUser(0,300)
hist3track_pt.GetXaxis().SetRangeUser(0,40)
hist3track_pt.GetXaxis().SetTitleOffset(1.4)
hist3track_pt.GetYaxis().SetTitleOffset(1.4)

# Set margins

canvas21.SetRightMargin(0.15)
canvas21.SetLeftMargin(0.15)
canvas21.SetBottomMargin(0.15)

# Add text to canvas

t21 = ROOT.TLatex()
t21.SetNDC(ROOT.kTRUE)
t21.SetTextSize(0.03)
t21.DrawLatex(0.18 ,0.86 ,"M_{h'} = 2 TeV , M_{q} = %.1f GeV , \Lambda = %.1f GeV"%(Mq,Mq))
t21.SetTextSize(0.03)
t21.DrawLatex(0.18 ,0.82 ,"M_{\pi} = %.1f GeV , M_{#rho} = %.1f GeV"%(m_pion, m_rho))
t21.SetTextSize(0.03)
t21.DrawLatex(0.18 , 0.78 , "N_{f} = %s , N_{c} = %s " %(Nf,Nc3))

# Add legend

legend21 = ROOT.TLegend(0.7,0.8,0.85,0.9)
legend21.SetFillStyle(1001)
legend21.SetLineWidth(1)
legend21.SetFillColor(0)
legend21.SetTextSize(0.03)
legend21.AddEntry(hist3track_pt,"Nf=%s,Nc=%s"%(Nf,Nc3))
legend21.Draw('same')

canvas21.Print("trackpt_Nf%s_Nc%s_Mq%.0f.pdf"%(Nf,Nc3,Mq))

########################################################################################################################################

# Creating and using 22nd canvas; i.e. track pt for Nf, Nc4

canvas22 = ROOT.TCanvas("canvas22")
canvas22.cd()

#Plotting histograms on canvas.

hist4track_pt.GetXaxis().SetTitle('p_{T} of tracks in leading jet')
hist4track_pt.GetYaxis().SetTitle('ntrk1')
hist4track_pt.SetStats(0)
hist4track_pt.GetYaxis().SetLabelSize(0.04)
hist4track_pt.GetYaxis().SetTitleSize(0.04)
hist4track_pt.GetXaxis().SetTitleSize(0.04)
hist4track_pt.GetXaxis().SetLabelSize(0.04)
hist4track_pt.SetTitle("Average track transverse momentum")
hist4track_pt.Draw('colZ')

hist4track_pt.GetYaxis().SetRangeUser(0,300)
hist4track_pt.GetXaxis().SetRangeUser(0,40)
hist4track_pt.GetXaxis().SetTitleOffset(1.4)
hist4track_pt.GetYaxis().SetTitleOffset(1.4)

# Set margins

canvas22.SetRightMargin(0.15)
canvas22.SetLeftMargin(0.15)
canvas22.SetBottomMargin(0.15)

# Add text to canvas

t22 = ROOT.TLatex()
t22.SetNDC(ROOT.kTRUE)
t22.SetTextSize(0.03)
t22.DrawLatex(0.18 ,0.86 ,"M_{h'} = 2 TeV , M_{q} = %.1f GeV , \Lambda = %.1f GeV"%(Mq,Mq))
t22.SetTextSize(0.03)
t22.DrawLatex(0.18 ,0.82 ,"M_{\pi} = %.1f GeV , M_{#rho} = %.1f GeV"%(m_pion, m_rho))
t22.SetTextSize(0.03)
t22.DrawLatex(0.18 , 0.78 , "N_{f} = %s , N_{c} = %s " %(Nf,Nc4))

# Add legend

legend22 = ROOT.TLegend(0.7,0.8,0.85,0.9)
legend22.SetFillStyle(1001)
legend22.SetLineWidth(1)
legend22.SetFillColor(0)
legend22.SetTextSize(0.03)
legend22.AddEntry(hist4track_pt,"Nf=%s,Nc=%s"%(Nf,Nc4))
legend22.Draw('same')

canvas22.Print("trackpt_Nf%s_Nc%s_Mq%.0f.pdf"%(Nf,Nc4,Mq))
