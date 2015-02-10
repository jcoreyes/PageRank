#!/usr/bin/env python
"""
Input will be of form:
NodeId:idNumber:iter \t currRank,prevRank,outLink1,outLink2...
"""
import sys

for line in sys.stdin:
    # If at final iteration, then output final results
    iter = int(line.split('\t')[0].split(':')[2])
    if iter < 51:
        sys.stdout.write(line)
    else:
        lineData = line.split('\t')
        nodeID = lineData[0].split(':')[1]
        currRank = lineData[1].split(',')[0]
        sys.stdout.write("FinalRank:%s %s\n" %(nodeID, currRank))
