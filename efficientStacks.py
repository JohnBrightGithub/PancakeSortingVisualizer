from collections import deque
from pancakeDist import getDistPerm
from path import drawEdgePath
from common import nodeIDToList
from common import permToString
from common import generate_positions
from common import findAllEffNeighbors
from dash import Dash, html
import dash_cytoscape as cyto
from dash.dependencies import Input, Output
from draw import runAppAndDraw
from draw import drawGraph

nodes = []
def manageQueues(queue1, queue2, traversal_order, n, visited, r, index):
 while queue1:
    xPos = 0
    while(queue1):
        node = queue1.popleft()
        traversal_order.append(node)
        allNeighbors = findAllEffNeighbors(node, n)
        numNeighbors = len(allNeighbors)
        positions = generate_positions(numNeighbors)
        nodeString = permToString(node)
        neighborIndex = 0
        for adj in allNeighbors:
            neighbor = permToString(adj)
            if neighbor not in visited:
                queue2.append(adj)
                visited.add(neighbor)
                edge = (node, adj)
                permX[neighbor], permY[neighbor] = permX[nodeString]+(xIncrement/(3*index+1)*positions[neighborIndex]), yPos
                drawEdgePath(edge)
                neighborIndex+=1
    if(queue2):
        if(index==r):
            return traversal_order
yPos = 10
xIncrement = 50
def bfs(start, r):
    global yPos
    # Create a queue for BFS
    queue1 = deque([start])
    queue2 = deque()
    n = len(start)
    # Keep track of visited nodes
    visited = set()
    startString = permToString(start)
    visited.add(startString)

    # List to store the order of traversal
    traversal_order = []
    index = 0
    permX[startString], permY[startString] = 0, 0
    while(queue1 or queue2):
        manageQueues(queue1, queue2, traversal_order, n, visited, r, index)
        yPos+=10
        index+=1
        manageQueues(queue2, queue1, traversal_order, n, visited, r, index)
        yPos+=10
        index+=1
    
    return traversal_order
edgeDict = {}
def drawEfficient(n, r):
    start = []
    for i in range(n):
        start.append(i+1)
    allPerms = bfs(start, r)
    #drawGraph()
    return allPerms
def getEdgesFromDict(color, dict):
    color = color.get_hex()
    edgeStrings = []
    for edgeString in dict:
        splitAt = edgeString.find("],") + 1
        firstNode = edgeString[1:splitAt]
        secondNode = edgeString[splitAt+2:-1]
        edgeStrings.append((firstNode, secondNode))
    edges = [
        {'data': {'source': source, 'target': target},
         'style': {'lineColor': color}}
        for source, target in (
            edgeStrings
        )
    ]
    return edges
from colour import Color
permX = {} #x position of perm
permY = {} #y position of perm
allPerms = drawEfficient(6, 7)

numPerms = len(allPerms)
permStrings = []
for i in range(numPerms):
    allPerms[i] = list(allPerms[i])
    perm = allPerms[i]
    permStrings.append(permToString(perm))
nodeTuples = []

for i in range(numPerms):
    nodeTuples.append((permStrings[i], permStrings[i], permY[permStrings[i]], permX[permStrings[i]], Color("green").get_hex()))
nodes = [
    {
        'data': {'id': short, 'label': label},
        'position': {'x': 20 * lat, 'y': -20 * long},
        'style': {'background-color': color, "height": 150, "width": 150},

    }
    for short, label, long, lat, color in (nodeTuples)
]
runAppAndDraw(nodes, layout='dagre')
for node in nodes:
    print("node ", node, " pos ", node.position)
