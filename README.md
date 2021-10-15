Authors and contacts:

* Guillaume Albouy: guillaume.albouy@etu.grenoble-univ-alpes.fr
* Akanksha Singh: akki153209@gmail.com
* Harikrishnan Nair: hunair1996@gmail.com

The code needs ```Delphes``` installed and linked such that delphes library can be invoked. 
Delphes can be found at
``` https://cp3.irmp.ucl.ac.be/projects/delphes```
In order for this to work, install Delphes and in your bashrc set following variables
```
export DELPHESPATH=<PATH_TO_DELPHES_INSTALLATION>
export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:$DELPHESPATH
```
Following cuts on events are assumed

jet1.PT > 500 and np.abs(jet1.Eta) < 2.5 and jet2.PT > 500 and np.abs(jet2.Eta) < 2.5

We assume that different branches corresponding to different jet radii are defined in root files.

In this code jet clustering radius is fixed to 1.4, can be changed at line 52 in analysis.py.

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

command: 
```
python /path_of_code/analysis.py /path_of_rootfile/name_of_rootfile.root /path_of_rootfile/output_name.root
```

takes the rootfile as input and computes the defined variables and fills the respective histograms.

A test sample is available at
``` https://sandbox.zenodo.org/record/927391```

Samples will be stored at Zenodo after initial testing is done. Note: The root version used to create these samples should be mentioned in the Zenodo repo.
 
Delphes card used to create these samples is stored in cards folder.
Cards folder also contains all the pythia command files used to generate signal.
The cards folder should contain the following
  * Scalar mediator: two seperate directories one corresponding to rho to pi pi mode open and another one corresponding to rho to pi pi mode closed will be made available.
  * Vector mediator: cards only for rho to pi pi mode closed are made available. (When rho decays to pions in this case, the final states will contain mostly missing energy and hence aren't very interesting)
  
Along with this ```plotter.py``` contains plotting scripts to make plots. These scrips are useful only when making 'global' plots to compare different Nc distributions for given Nf values. For immediate plotting purposes with one sample file, you will need to make your own code. 
