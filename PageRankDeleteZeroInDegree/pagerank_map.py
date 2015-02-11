#!/usr/bin/env python
"""
Input Data Format For first iteration:
NodeId:idNumber \t currRank,prevRank,outLink1,outLink2...
For after first iteration:
NodeId:idNumber:iter:degree:contr \t currRank,prevRank,outLink1,outLink2...

Output will be of 2 forms:
idNumber \t contribution
idNumber \t prevRank \t iter \t degree \t contr \t outLink1,outLink2...
"""
import sys

for line in sys.stdin:
    lineData = line.rstrip('\n').split('\t')
    nodeData = lineData[0].split(':')
    currNode = nodeData[1]
    rankData = lineData[1].split(',')
    currPageRank = float(rankData[0])

    # If wrong format then continue
    if (len(lineData) != 2):
        continue

    # If no iteration number yet start at 1
    if len(nodeData) == 2:
        iter = 1
    else:
        iter = int(nodeData[2]) + 1

    # If at first iteration compute degree, otherwise use precomputed degree
    degree = 0
    if (iter==1):
        # If atleast 1 outlink
        if len(rankData) > 2:
            degree = len(rankData[2:])
    else:
        degree = int(nodeData[3])

    # If there's atleast 1 outlink
    if degree >=1:
        outLinks = rankData[2:]
        for outLink in outLinks:
            print("%s\t%f" %(outLink, currPageRank/degree))
    # If no outlinks, then contribution is 1
    else:
        print("%s\t%f" %(currNode, currPageRank))

    # Add extra contribution from deleted nodes
    extraContr = 0
    if (len(nodeData) == 5):
        extraContr = float(nodeData[4])
        if (extraContr != 0):
            print("%s\t%f" %(currNode, extraContr))

    # prevRank becomes currPageRank
    # currPageRank will be recalculated in the next reduce
    if len(rankData) < 3:
        outLinks = ['no_outlinks']
    strFormat = "%s\t%f\t%d\t%d\t%f\t%s"
    if extraContr == 0:
        strFormat = "%s\t%f\t%d\t%d\t%d\t%s"
    print (strFormat %(currNode, currPageRank, iter, degree, extraContr, ','.join(outLinks)))
