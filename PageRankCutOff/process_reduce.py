#!/usr/bin/env python
"""
Input will be of form:
NodeId:idNumber:iter \t currRank,prevRank,outLink1,outLink2...
"""
import sys
nodes = {}
totRankDiff = 0
maxRankDiff = -sys.maxint
maxRank = -sys.maxint
totalRank = 0
iter = 0
for line in sys.stdin:
    lineData = line.split('\t')

    nodeData = lineData[0].split(':')
    nodeID = int(nodeData[1])
    iter = int(nodeData[2])

    rankData = lineData[1].split(',')
    currRank = float(rankData[0])
    prevRank = float(rankData[1])

    totalRank += currRank
    rankDiff =  abs(currRank - prevRank)
    totRankDiff += rankDiff
    maxRankDiff = max(maxRankDiff, rankDiff)
    maxRank = max(maxRank, currRank)
    nodes[nodeID] = {}
    nodes[nodeID]['line'] = line
    nodes[nodeID]['rankDiff'] = rankDiff
    nodes[nodeID]['currRank'] = currRank

numNodes = len(nodes)

STOP = False
if totRankDiff/float(numNodes) < .0001:
    STOP = True
if iter >= 50:
    STOP = True

if STOP:
    topRanks = sorted(nodes.items(), key=lambda x:x[1]['currRank'], reverse=True)
    for i in range(20):
        print("FinalRank:%f\t%d" %(topRanks[i][1]['currRank'], topRanks[i][0]))
else:
    for node, data in nodes.items():
        sys.stdout.write(data['line'])
