#!/usr/bin/env bash

batches=(500, 1000 5000 10000 15000 20000 25000 30000)
algorithms=('bubble' 'bubble_improved' 'heap' 'insertion' 'merge' 'quick' 'quick_median' 'selection'
            'iquick' 'iquick_median')
modes=('r' 'a' 'd')

for batch in "${batches[@]}"
do
    echo ${batch}
    for algorithm in "${algorithms[@]}"
    do
        for mode in "${modes[@]}"
        do
            echo -e "\t ${algorithm} - ${mode}"
            python runner.py -a=${algorithm} --mode=${mode} --size=${batch} --times=10 -f
        done
    done
done