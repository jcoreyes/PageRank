#!/usr/bin/env python
"""
Input will be of form:
NodeId:idNumber:iter \t currRank,prevRank,outLink1,outLink2...
"""
import sys
import operator
nodes = {}
avgRankDiff = 0
maxRankDiff = -sys.maxint
maxRank = -sys.maxint
iter = 0
for line in sys.stdin:
    lineData = line.split('\t')

    nodeData = lineData[0].split(':')
    nodeID = int(nodeData[1])
    iter = int(nodeData[2])

    rankData = lineData[1].split(',')
    currRank = float(rankData[0])
    prevRank = float(rankData[1])

    rankDiff =  abs(currRank - prevRank)
    maxRankDiff = max(maxRankDiff, rankDiff)
    maxRank = max(maxRank, currRank)
    nodes[nodeID] = {}
    nodes[nodeID]['line'] = line
    nodes[nodeID]['rankDiff'] = rankDiff
    nodes[nodeID]['currRank'] = currRank

if iter == 51:
    topRanks = sorted(nodes.items(), key=lambda x:x[1]['currRank'], reverse=True)
    for i in range(20):
        print("FinalRank:%f %d" %(topRanks[i][1]['currRank'], topRanks[i][0]))
else:
    thresh = 0.2 * maxRank
    for node, data in nodes.items():
        # Remove node if rank less than 20% of max
        if (data[currRank] < maxRank):
            continue
        sys.stdout.write(data['line'])
