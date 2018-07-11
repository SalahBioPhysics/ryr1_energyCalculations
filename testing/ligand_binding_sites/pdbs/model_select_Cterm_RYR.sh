#/bin/bash

while read -r LINE
do
echo "$LINE"
awk 'NR>1 && NR<1113; NR>52333 && NR<60207; NR==122653' "$LINE"_5t9v_class1_ca_atp_cff-fit-coot-0_real_space_refined.pdb > "$LINE"_5t9v_class1_ca_atp_cff.pdb
done < list
