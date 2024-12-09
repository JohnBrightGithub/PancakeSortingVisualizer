def drawEdge(edge, dict):
    edgeString = str(edge)
    reverseEdge = (edge[1],edge[0])
    reverseEdgeString = str(reverseEdge)
    #print("edgeString ", edgeString, " reverseEdgeString ", reverseEdgeString)
    if not edgeString in dict and not reverseEdgeString in dict:
        dict[edgeString] = 1
        #print("adding to edge dict: ", edgeString)