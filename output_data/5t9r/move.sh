for i in {1..10}
do 
    mkdir /home/guest/ryr1_energyCalculations/output_data/5t9r/frame_0$i/binding/
    mkdir /home/guest/ryr1_energyCalculations/output_data/5t9r/frame_0$i/binding/Ca/
    mkdir /home/guest/ryr1_energyCalculations/output_data/5t9r/frame_0$i/binding/Ca/100_0/
done

for i in {11..50}
do
    mkdir /home/guest/ryr1_energyCalculations/output_data/5t9r/frame_$i/binding/
    mkdir /home/guest/ryr1_energyCalculations/output_data/5t9r/frame_$i/binding/Ca/
    mkdir /home/guest/ryr1_energyCalculations/output_data/5t9r/frame_$i/binding/Ca/100_0/
done




for i in {1..10}
do
    cp /home/guest/ryr1_energyCalculations/calculations/5t9r/frame_0$i/binding/Ca/100_0/fort.38 /home/guest/ryr1_energyCalculations/output_data/5t9r/frame_0$i/binding/Ca/100_0/
done

for i in {11..50}
do
    cp /home/guest/ryr1_energyCalculations/calculations/5t9r/frame_$i/binding/Ca/100_0/fort.38 /home/guest/ryr1_energyCalculations/output_data/5t9r/frame_$i/binding/Ca/100_0/
done
