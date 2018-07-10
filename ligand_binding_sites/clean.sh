for i in {10..50}
do
    echo "clean frame_$i"
    cd frame_$i
    rm acc.* debug.log energies.opp energies.opp error.log head1.lst head2.lst new.tpl progress.log respair.lst rot_stat run.trace step* vdw0.lst
    cd binding
    rm energies.opp entropy.out error.log pK.out respair.lst run.trace
    cd ../..
done
