#!/bin/bash

# for every item matching pattern supplied on command line do the following:
for i in "$@"
do
phenix.real_space_refine ${i}_5t9r_norm_psi_Class50_SVD12_bfac290_4.5A.pdb ../maps/norm_psi_Class50_SVD12_${i}_bfac290_4.5A.mrc resolution=5 write_all_states=false write_initial_geo_file=False  
done
