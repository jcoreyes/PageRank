#!/usr/bin/env python

"""
Reducer for 1st step of PageRank that takes input from pagerank_map
Input will be of two forms:
idNumber \t contribtion
idNumber \t prevRank \t iter \t degree \t contr \t outLink1,outLink2...

Output will be of two forms:
NodeId:idNumber:iter:degree:contr \t currRank,prevRank,outLink1,outLink2...

If deleting then it will be
DeleteId:idNumber:iter:degree:contr \t currRank,prevRank,outLink1,outLink2...
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

MOMENTUM = 0.0
for nodeID in nodes:
    currRank = 1 - DAMPING_FACTOR + (DAMPING_FACTOR * sum(nodes[nodeID]['contributions']))
    prevRank = nodes[nodeID]['prevRank']
    # rankDiff = currRank - float(prevRank)
    # # Accelerate rank change
    # if (iter < 5):
    #     currRank += rankDiff * MOMENTUM

    outLinks = nodes[nodeID]['outLinks']
    degree = nodes[nodeID]['degree']
    extraContr = float(nodes[nodeID]['extraContr'])

    # If in degree of node is 0, then use flag for deleting node
    # If curr out degree of node is 0, then length of contributions will be 2
    numContr = len(nodes[nodeID]['contributions'])
    deleteFlag = "N"
    if numContr  <= 1 or (len(outLinks.split(',')) == 0 and numContr == 2) or (extraContr == 0 and numContr == 0):
        deleteFlag = "D"
    if outLinks != 'no_outlinks':
        print("%s:%s:%s:%s:%s\t%f,%s,%s" %(deleteFlag, nodeID, iter, degree, extraContr, currRank, prevRank, outLinks))
    else:
        print("%s:%s:%s:%s:%s\t%f,%s" % (deleteFlag, nodeID, iter, degree, extraContr, currRank, prevRank))