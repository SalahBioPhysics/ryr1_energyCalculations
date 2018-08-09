for i in {1..9}
do
    cp /home/guest/ryr1_energyCalculations/calculations/5t9r/frame_0$i/fort.38 /home/guest/ryr1_energyCalculations/output_data/frame_0$i/
done

for i in {10..50}
do
    cp /home/guest/ryr1_energyCalculations/calculations/5t9r/frame_$i/fort.38 /home/guest/ryr1_energyCalculations/output_data/frame_$i/
done
