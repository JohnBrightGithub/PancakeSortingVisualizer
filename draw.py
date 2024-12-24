def drawEdge(edge, dict):
    edgeString = str(edge)
    reverseEdge = (edge[1],edge[0])
    reverseEdgeString = str(reverseEdge)
    if not edgeString in dict and not reverseEdgeString in dict:
        dict[edgeString] = 1