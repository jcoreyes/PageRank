#!/usr/bin/env python


import sys
import operator
DAMPING_FACTOR = 0.85
nodes = {}
for line in sys.stdin:
    lineData = line.rstrip('\n').split('\t')
    nodeID = lineData[0]
    if nodeID not in nodes:
        nodes[nodeID] = []
    nodes[nodeID].append(float(lineData[1]))

for nodeID in nodes:
    currRank = 1 - DAMPING_FACTOR + (DAMPING_FACTOR * sum(nodes[nodeID]))
    nodes[nodeID] = currRank


sorted_ranks = sorted(nodes.items(), key=operator.itemgetter(1), reverse=True)

for i in xrange(20):
	print ("FinalRank:%f\t%s" % (sorted_ranks[i][1], sorted_ranks[i][0]))
