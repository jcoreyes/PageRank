#!/usr/bin/env python

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


# import sys
# prevNodeID = -1
DAMPING_FACTOR = 0.85

# for line in sys.stdin:
#     lineData = line.rstrip('\n').split('\t')
#     nodeID = lineData[0]
#     if len(lineData) > 2:
#         prevRank = float(lineData[1])
#         outLinks = lineData[2]
#         continue
#     if prevNodeID == -1:
#         rankContr = [float(lineData[1])]
#         prevNodeID = nodeID
#         continue
#     if nodeID != prevNodeID:
#         if prevNodeID == 14:
#             print out
#         pageRank = 1 - DAMPING_FACTOR + (DAMPING_FACTOR * sum(rankContr))
#         if outLinks != 'no_outlinks':
#             print("NodeID:%s\t%f,%f,%s" %(prevNodeID, pageRank, prevRank, outLinks))
#         else:
#             print("NodeID:%s\t%f,%f" % (prevNodeID, pageRank, prevRank))
#         rankContr = [float(lineData[1])]
#         outLinks = []
#         prevNodeID = nodeID
#     else:
#         rankContr.append(float(lineData[1]))

# pageRank = 1 - DAMPING_FACTOR + (DAMPING_FACTOR * sum(rankContr))
# if outLinks != 'no_outlinks':
#     print("NodeID:%s\t%f,%f,%s" %(prevNodeID, pageRank, prevRank, outLinks))
# else:
#     print("NodeID:%s\t%f,%f" % (prevNodeID, pageRank, prevRank))

import sys
nodes = {}
for line in sys.stdin:
    lineData = line.rstrip('\n').split('\t')
    nodeID = lineData[0]
    if nodeID not in nodes:
        nodes[nodeID] = {}
        nodes[nodeID]['contributions'] = []
    if len(lineData) > 2:
        nodes[nodeID]['prevRank'] = float(lineData[1])
        nodes[nodeID]['outLinks'] = lineData[2]
    else:
        nodes[nodeID]['contributions'].append(float(lineData[1]))

for nodeID in nodes:
    currRank = 1 - DAMPING_FACTOR + (DAMPING_FACTOR * sum(nodes[nodeID]['contributions']))
    prevRank = nodes[nodeID]['prevRank']
    outLinks = nodes[nodeID]['outLinks']
    if outLinks != 'no_outlinks':
        print("NodeID:%s\t%f,%f,%s" %(nodeID, currRank, prevRank, outLinks))
    else:
        print("NodeID:%s\t%f,%f" % (nodeID, currRank, prevRank))