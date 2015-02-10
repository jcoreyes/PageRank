#!/bin/bash
python pagerank_map.py < ../rankmaniac-lib/local_test_data/EmailEnron | sort | python pagerank_reduce.py |
    python process_map.py | sort | python process_reduce.py > input.txt
for i in $(seq 0 49); do
    python pagerank_map.py < input.txt | sort | python pagerank_reduce.py | python process_map.py | sort | python process_reduce.py > output.txt
    echo $i
    rm input.txt
    cp output.txt input.txt
    rm output.txt
done
