#!/bin/bash
python pagerank_map.py < GNPn100p05 | sort -n | python pagerank_reduce.py | sort > in2.data
for (( c=2; c<$1; c++ ))
do
	python pagerank_map.py < in2.data | sort -n | python pagerank_reduce.py | sort | sponge in2.data
done

python process_map.py < in2.data | sort -n | python process_reduce.py > out.data