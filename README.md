Authors and contacts:
Guillaume Albouy: guillaume.albouy@etu.grenoble-univ-alpes.fr
Akanksha Singh: akki153209@gmail.com
Harikrishnan Nair: hunair1996@gmail.com

This code needs helpers.py and histo_defs.py which are stored in the same folder as this file
Following cuts on events are assumed
jet1.PT > 500 and np.abs(jet1.Eta) < 2.5 and jet2.PT > 500 and np.abs(jet2.Eta) < 2.5
We assume that different branches corresponding to different jet radii are defined in root files
In this code jet clustering radius is fixed to 1.4, can be changed at line 52
This code will analyse input sample and create following reconstructed level normalized distributions:
1) pt of leading/subleading jet
2) dijet invarint mass
3) missing energy
4) transverse mass of dijet and met system
5) transverse ratio
6) delta phi between missin energy and leading/subleading jet
7) 2D histo of track pT of leading jet
8) delta eta between leading and subleading jet
9) pt and invariant mass for trimmed and SoftDropped leading/subleading jets

command: python /path_of_code/transverse_mass.py /path_of_rootfile/name_of_rootfile.root /path_of_rootfile/output_name.root
Takes the rootfile as input and computes the defined variables and fills the respective histograms.

Samples are stored at <Insert path>
Delphes card used to create these samples is stored in cards folder.
Cards folder also contains all the pythia command files used to generate signal. 
