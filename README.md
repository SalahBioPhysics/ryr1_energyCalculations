# ryr1
For an overview on the ryanodine receptor (RyR1) being a Ca+2 channel that facilitates skeletal muscle excitation and contraction, we can refer to this [paper](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5142848/).

Excellent reviews on ryanodine receptors [(RYRs)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3156641/) , dihydropyridine receptors [(DHPRs)](https://www.ncbi.nlm.nih.gov/pubmed/19660468) and [Disease-causing mutations of calcium channels](https://www.tandfonline.com/doi/abs/10.4161/chan.2.3.5950)

In this project, we are calculating the energy landscapes using Multi-Conformer Continuum Electrostatics [(MCCE)](https://sites.google.com/site/mccewiki/home). Calculations are done with two datasets.  One set involves the RyR1 macromolecules in equilibrium with a thermal bath sans the activation of ligands; the other involves the RyR1 macromolecules in equilibrium with both a thermal bath as well as a reservoir of the activated ligands calcium, ATP, and caffeine. 

## testing/ligand_binding_sites:
These PDB files were prepared by Danya Ben Hail.  There are 50 files labeled frame_01 to frame_50.  The structure of this data set is modified such that only the activation core is calculated. Each frame_0i directory contains an input pdb, here highlighted in blue. 

Activation core top view | Activation core side view
------------ | -------------
![AC](input_data/actication_core_top.png) | ![AC](input_data/actication_core_side.png)

**Figure 1:** Activation core (PDBID: 5t9r).  Residues B3614-B5102
The generated output files are titled head3.lst and fort.38. 
### head3.lst
* iConf:conformer ID
* CONFORMER: conformer name
* FL: flag| f means the conformer is on, t means the conformer is off.
* occ: occupancy
* crg: charge
* Em0: Em in solution
* pKa0: pka in solution
* ne: # of electrons
* nH: # of protons
* vdw0: self vdW energy + implicit vdW energy (favorable) with solvent (water)
* vdw1:backbone vdW
* tors: torsion energy
* epol: backbone electrostatic interaction
* dsolv: desolvation energy 
* extra: extra energy term (This is the value we change when we want to calculate titration curve for the ligand)
* history: to keep track of the conformer

### fort.38
This file shows the occupancy of each conformer at differernt ph/eh/ch values.  In our case, we are using chemical titration (ch). The plot below shows the Ca+2 titration carve of frame01.
![Ca+2 titration carve](presentation/CADMG5104_002.png) 
**Figure 2:** Ca+2 titration carve of the activation code (**Figure 1**)


 
