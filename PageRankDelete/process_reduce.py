#!/usr/bin/env python
"""
Input will be of form:
NodeId:idNumber:iter:degree:contr \t currRank,prevRank,outLink1,outLink2...

Output will be of form:
NodeId:idNumber:iter:degree:contr \t currRank,prevRank,outLink1,outLink2...
"""
import sys
import math
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
    degree = int(nodeData[3])

    rankData = lineData[1].strip('\n').split(',')
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
    nodes[nodeID]['prevRank'] = prevRank
    nodes[nodeID]['nodeData'] = nodeData
    nodes[nodeID]['rankData'] = rankData
    nodes[nodeID]['degree'] = degree

numNodes = len(nodes)
avgRankDiff = totRankDiff/float(numNodes)

# Stopping criterion is if avg rank difference below threshold
STOP = False
if avgRankDiff < .001 or iter >= 50:
    STOP = True

# Deletion criterion is if avg rank diff below threshold
DELETE = False
if iter >= 5 and (iter % 5 == 0) and numNodes > 50:
    DELETE = True

if STOP:
    topRanks = sorted(nodes.items(), key=lambda x:x[1]['currRank'], reverse=True)
    for i in range(20):
        print("FinalRank:%f\t%d" %(topRanks[i][1]['currRank'], topRanks[i][0]))
    print numNodes
else:
    if (not DELETE):
        for node, data in nodes.items():
            sys.stdout.write(data['line'])
    else:
        # Find nodes to delete based on lowest rank
        nodesToDelete = set()
        topRanks = sorted(nodes.items(), key=lambda x:x[1]['currRank'])
        numDelete = int(numNodes * 0.05)
        for i in range(numDelete):
            nodesToDelete.add(str(topRanks[i][0]))

        # Find contribution of outlinks of deleted nodes
        outLinksContr = {}
        totRank = 0
        for node in nodesToDelete:
            degree = nodes[int(node)]['degree']
            if degree == 0:
                continue
            outLinks = nodes[int(node)]['rankData'][2:]
            # Save what that deleted node would have contributed to another node
            for outLink in outLinks:
                if outLink not in outLinksContr:
                    outLinksContr[outLink] = nodes[int(node)]['currRank'] / float(degree)
                else:
                    outLinksContr[outLink] += nodes[int(node)]['currRank'] / degree

        # Print nodes with extra contribution and delete nodes to delete from all outlinks
        for node, data in nodes.items():
            if (str(node) in nodesToDelete):
                continue
            outLinks = set()
            rankData = nodes[node]['rankData']
            if len(rankData) > 2:
                outLinks = set(rankData[2:])
                outLinks = outLinks - nodesToDelete
            rankData = ','.join(rankData[0:2] + list(outLinks))
            extraContr = 0
            if (str(node)) in outLinksContr:
                extraContr = outLinksContr[str(node)]
            print("%s:%f\t%s" %(':'.join(nodes[node]['nodeData'][:-1]), extraContr, rankData))
