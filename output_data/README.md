
### PDB file
Input: This file has all the residues of the activation core (B3614 to B5102)

### head3.lst
Output: Energy per charged residue
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
Output: This file shows the occupancy of each conformer at differernt ph/eh/ch values.  In our case, we are using chemical titration (ch). The plot below shows the Ca+2 titration carve of frame01.
![Ca+2 titration carve](output_data/frame_01.png) 
**Figure 2:** Ca+2 titration carve of the activation code (**Figure 1**)
