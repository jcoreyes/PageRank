"""
Reducer for 1st step of PageRank
Takes input from pagerank_map where each line in std input is of form
0\t0.2
where 0 is the id of the node and 0.2  is the contribution to that node
from another node
Output wil be of form
0\t1.1
where 0 is the id of the node, and 1.1 is its new rank computed
from the sum of its contributions
"""


import sys
prevNodeID = -1
for line in sys.stdin:
    lineData = line.rstrip('\n').split('\t')
    nodeID = lineData[0]
    if prevNodeID == -1:
        rankContr = []
        rankContr.append(float(lineData[1]))
        prevNodeID = nodeID
        continue
    if nodeID != prevNodeID:
        print("%s\t%f" %(nodeID, sum(rankContr)))
        rankContr = []
        prevNodeID = nodeID
    else:
        rankContr.append(float(lineData[1]))