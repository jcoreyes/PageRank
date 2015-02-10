#!/usr/bin/env python

import sys

for line in sys.stdin:
    currNode = line.rstrip('\n').split('\t')[0].split(':')[1]
    lineData = line.rstrip('\n').split('\t')[1].split(',')
    currPageRank = float(lineData[0])
    if len(lineData) > 2:
        numOutLinks = len(lineData[2:])
        for outLink in lineData[2:]:
            print("%s\t%f" %(outLink, currPageRank/numOutLinks))
    else:
    	print("%s\t%f" %(currNode, 1))