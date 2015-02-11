#!/usr/bin/env python

"""
Reducer for 1st step of PageRank that takes input from pagerank_map
Input will be of two forms:
idNumber \t contribtion
idNumber \t prevRank \t iter \t degree \t contr \t outLink1,outLink2...

Output will be of form:
NodeId:idNumber:iter:degree:contr \t currRank,prevRank,outLink1,outLink2...
"""

DAMPING_FACTOR = 0.85

import sys
nodes = {}
iter = '0'
for line in sys.stdin:
    lineData = line.rstrip('\n').split('\t')
    nodeID = lineData[0]
    if nodeID not in nodes:
        nodes[nodeID] = {}
        nodes[nodeID]['contributions'] = []
    # If line is of first type, just save contributions
    if len(lineData) == 2:
        nodes[nodeID]['contributions'].append(float(lineData[1]))
    else:
        # Save prev rank, outlinks, iter, degree, and extra Contr
        nodes[nodeID]['prevRank'] = lineData[1]
        iter = lineData[2]
        nodes[nodeID]['degree'] = lineData[3]
        nodes[nodeID]['extraContr'] = lineData[4]
        nodes[nodeID]['outLinks'] = lineData[5]

for nodeID in nodes:
    currRank = 1 - DAMPING_FACTOR + (DAMPING_FACTOR * sum(nodes[nodeID]['contributions']))
    prevRank = nodes[nodeID]['prevRank']
    outLinks = nodes[nodeID]['outLinks']
    degree = nodes[nodeID]['degree']
    extraContr = nodes[nodeID]['extraContr']
    if outLinks != 'no_outlinks':
        print("NodeID:%s:%s:%s:%s\t%f,%s,%s" %(nodeID, iter, degree, extraContr, currRank, prevRank, outLinks))
    else:
        print("NodeID:%s:%s:%s:%s\t%f,%s" % (nodeID, iter, degree, extraContr, currRank, prevRank))