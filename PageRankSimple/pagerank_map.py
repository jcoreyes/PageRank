"""
Mapper for 1st step of PageRank
Takes input from stdin which will be tab delimited form for each line:
NodeId:0\t1.0, 0,0, 83, 212, 301
where 0 is the curret node identifier, 1.0 and 0.0 are the current and previous PageRanks of this node,
and 81...301 are nodes which node 0 links to.
"""


import sys

for line in sys.stdin:
    lineData = line.rstrip('\n').split('\t')[1].split(',')
    currPageRank = float(lineData[0])
    if len(lineData) > 2:
        numOutLinks = len(lineData[2:])
        for outLink in lineData[2:]:
            print("%s\t%f" %(outLink, currPageRank/numOutLinks))