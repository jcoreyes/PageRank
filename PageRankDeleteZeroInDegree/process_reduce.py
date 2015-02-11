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
# maxRankDiff = -sys.maxint
# maxRank = -sys.maxint
# totalRank = 0
iter = 0
nodesToDelete = set()

for line in sys.stdin:
    lineData = line.split('\t')

    nodeData = lineData[0].split(':')
    nodeID = int(nodeData[1])
    iter = int(nodeData[2])
    degree = int(nodeData[3])

    rankData = lineData[1].strip('\n').split(',')
    currRank = float(rankData[0])
    prevRank = float(rankData[1])

    # totalRank += currRank
    rankDiff =  currRank - prevRank
    totRankDiff += abs(rankDiff)
    # maxRankDiff = max(maxRankDiff, rankDiff)
    # maxRank = max(maxRank, currRank)
    nodes[nodeID] = {}
    nodes[nodeID]['line'] = line
    nodes[nodeID]['rankDiff'] = rankDiff
    nodes[nodeID]['currRank'] = currRank
    nodes[nodeID]['prevRank'] = prevRank
    nodes[nodeID]['nodeData'] = nodeData
    nodes[nodeID]['rankData'] = rankData
    nodes[nodeID]['degree'] = degree

    if nodeData[0] == "D":
        nodesToDelete.add(nodeID)

numNodes = len(nodes)
avgRankDiff = totRankDiff/float(numNodes)

# Stopping criterion is if avg rank difference below threshold
STOP = False
if avgRankDiff < .0004 or iter >= 50:
    STOP = True

# Deletion criterion is if avg rank diff below threshold
DELETE = False
if len(nodesToDelete) > 0:
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
        # Find more nodes to delete based on low rank diff
        # if (iter == 5):
        #     topRanks = sorted(nodes.items(), key=lambda x:x[1]['rankDiff'])
        #     numDelete = int(numNodes * 0.1)
        #     for i in range(numDelete):
        #         nodesToDelete.add(topRanks[i][0])

        # Find contribution of outlinks of deleted nodes
        outLinksContr = {}
        totRank = 0
        for node in nodesToDelete:
            degree = nodes[node]['degree']
            if degree == 0:
                continue
            outLinks = nodes[node]['rankData'][2:]
            # Save what that deleted node would have contributed to its outlink
            for outLink in outLinks:
                if outLink not in outLinksContr:
                    outLinksContr[outLink] = nodes[node]['currRank'] / float(degree)
                else:
                    outLinksContr[outLink] += nodes[node]['currRank'] / float(degree)

        # Print nodes with extra contribution and delete nodes to delete from all outlinks
        nodesToDeleteStr = set([str(x) for x in nodesToDelete])
        for node, data in nodes.items():
            if node in nodesToDelete:
                continue
            outLinks = set()
            rankData = nodes[node]['rankData']
            if len(rankData) > 2:
                outLinks = set(rankData[2:])
                outLinks = outLinks - nodesToDeleteStr
            rankData = ','.join(rankData[0:2] + list(outLinks))
            extraContr = 0
            if (str(node)) in outLinksContr:
                extraContr = outLinksContr[str(node)]
            strFormat = "%s:%f\t%s"
            if extraContr == 0:
                strFormat = "%s:%d\t%s"
            print(strFormat %(':'.join(nodes[node]['nodeData'][:-1]), extraContr, rankData))
