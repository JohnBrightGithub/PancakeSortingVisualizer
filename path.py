from pancakeDist import getDistPerm
from draw import drawEdge
from common import nodeIDToList
from common import permutations
from common import flip
from common import findAllEdges
pathDict = {}
addedEdgeDict ={}
edgeDict = {}
pathIndex = 0
def getAddedDict():
    return addedEdgeDict
def getEdgeDict():
    return edgeDict
def getPathDict():
    return pathDict
def getPathIndex():
    return pathIndex
def genEdges(n):
    #generate edges for all permutations
    #print(allPerms)
    allPerms = permutations(n)
    for perm in allPerms:
        perm = list(perm)
        allEdges = findAllEdges(perm, 3)
        for edge in allEdges:
            drawEdge(edge, edgeDict)
            print("edge: ", edge)
def drawNewEdges(perm, origDist, pathList):
    n=len(perm)
    if(origDist==0):
        global pathIndex
        pathDict[pathIndex] = pathList
        pathIndex+=1
        return
    for i in range(1, n):
        node2 = flip(perm, i)
        newDist = getDistPerm(node2)
        if(newDist<origDist):
            newPathList = pathList.copy()
            newPathList.append(node2)
            #print("new edge added ", (perm, node2))
            drawEdge((perm, node2), addedEdgeDict)
            drawNewEdges(node2, newDist, newPathList)


def drawPath(perm):
    global addedEdgeDict
    global pathIndex
    global pathDict
    pathIndex = 0
    addedEdgeDict = {}
    origDist = getDistPerm(perm)
    pathDict = {}
    pathList = [perm]
    drawNewEdges(perm, origDist, pathList)