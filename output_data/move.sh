for i in {10..50}
do
    cp /home/guest/ryr1_energyCalculations/calculations/frame_$i/$i.pdb /home/guest/ryr1_energyCalculations/output_data/frame_$i
    cp /home/guest/ryr1_energyCalculations/calculations/frame_$i/head3.lst /home/guest/ryr1_energyCalculations/output_data/frame_$i
    cp /home/guest/ryr1_energyCalculations/calculations/frame_$i/fort.38 /home/guest/ryr1_energyCalculations/output_data/frame_$i
    cp /home/guest/ryr1_energyCalculations/calculations/frame_$i/run.trace /home/guest/ryr1_energyCalculations/output_data/frame_$i
    #cp ../calculations/frame_$i/head3.lst frame_$i/
    #cp ../calculations/frame_$i/fort.38 frame_$i/
done
