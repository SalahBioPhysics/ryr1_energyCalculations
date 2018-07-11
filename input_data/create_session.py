import os
from chimera import runCommand as rc

rng=(0,50)
k=0
for i in xrange(*rng):
    Str = "%02d" % (i+1)
    rc("open #%d ~/Dropbox/RyR_NLSA_Maps/maps_relion_morph/2018_290bfactor_maps_models_5t9r/%s_5t9r_norm_psi_Class50_SVD12_bfac290_4.5A.pdb" % (k, Str))
    k+=1


