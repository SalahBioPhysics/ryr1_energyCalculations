#/bin/bash

while read -r LINE
do
echo "$LINE"
bash phenix_refine.sh $LINE >>model_refine.txt
done < list1.txt
