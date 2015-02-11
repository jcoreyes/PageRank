#!/bin/bash
testFile=$1
echo $testFile
rm input.txt
python pagerank_map.py < "../rankmaniac-lib/local_test_data/$testFile" | sort | python pagerank_reduce.py |
    python process_map.py | sort | python process_reduce.py > input.txt
for i in $(seq 1 49); do
    python pagerank_map.py < input.txt | sort | python pagerank_reduce.py | python process_map.py | sort | python process_reduce.py > output.txt
    rm input.txt
    cp output.txt input.txt
    rm output.txt
    if [[ $(head -c 1 input.txt) == "F" ]]; then break; else echo $i; fi
done
cut -f 2 input.txt > output.txt && diff -c "../rankmaniac-lib/sols/$testFile" output.txt && rm output.txt