#!/usr/bin/env python
"""
Input Data Format For first iteration:
NodeId:idNumber \t currRank,prevRank,outLink1,outLink2...
For after first iteration:
NodeId:idNumber:iter \t currRank,prevRank,outLink1,outLink2...

Output will be of 2 forms:
idNumber \t contribution
idNumber \t prevRank \t iter \t outLink1,outLink2...
"""
import sys

for line in sys.stdin:
    lineData = line.rstrip('\n').split('\t')
    nodeData = lineData[0].split(':')
    currNode = nodeData[1]
    rankData = lineData[1].split(',')
    currPageRank = float(rankData[0])
    # If there's atleast 1 outlink
    if len(rankData) > 2:
        outLinks = rankData[2:]
        numOutLinks = len(outLinks)
        for outLink in outLinks:
            print("%s\t%f" %(outLink, currPageRank/numOutLinks))
    # If no outlinks, then contribution is 1
    else:
        print("%s\t%f" %(currNode, 1))
    # If no iteration number yet start at 1
    if len(nodeData) < 3:
        iter = 1
    else:
        iter = int(nodeData[2]) + 1
    # prevRank becomes currPageRank
    # currPageRank will be recalculated in the next reduce
    if len(rankData) < 3:
        outLinks = ['no_outlinks']
    print ("%s\t%f\t%d\t%s" %(currNode, currPageRank, iter, ','.join(outLinks)))
