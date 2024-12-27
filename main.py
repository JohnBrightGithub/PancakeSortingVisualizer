from dash import Dash, html
import dash_cytoscape as cyto
from common import permToString
from common import colexicographicPermutations
from common import permutations
from common import nodeIDToList
from pancakeDist import getDistPerm
from pancakeDist import loadDistFile
from path import drawPath
from path import flip
from path import genEdges
from path import getEdgeDict
from path import getAddedDict
import argparse
from dash.dependencies import Input, Output
import math
from colour import Color



graphEdges = []

n = 5

class CommandLineEstimate:
    def __init__(self):
        parser = argparse.ArgumentParser()
        parser.add_argument("-n", "--n", help = " length of pancake stacks ", required = False, default = 5)
        
        argument = parser.parse_args()
        
        if argument.n:
            global n
            n = int(argument.n)
def hexagonPos(initPerm, initX, initY):
    #writes in positions for nodes in a hexagon, starts with initPerm
    spacer = 10
    node1 = initPerm
    node1String = str(node1)
    permX[node1String], permY[node1String] = initX, initY
    node2 = flip(initPerm, 1)
    node2String = str(node2)
    permX[node2String], permY[node2String] = initX-spacer, initY-spacer
    node3 = flip(initPerm, 2)
    node3String = str(node3)
    permX[node3String], permY[node3String] = initX+spacer, initY-spacer
    node4 = flip(node2, 2)
    node4String = str(node4)
    permX[node4String], permY[node4String] = initX-spacer, initY-2*spacer
    node5 = flip(node3, 1)
    node5String = str(node5)
    permX[node5String], permY[node5String] = initX+spacer, initY-2*spacer
    node6 = flip(node5, 2)
    node6String = str(node6)
    permX[node6String], permY[node6String] = initX, initY-3*spacer
onlyHexagonEdges = True

edgeDict = {}
addedEdgeDict = {}


app = Dash(__name__)

def getInitPos(hexNumber):
    k = len(hexNumber)

spacerP4 = 40
def genInitPos(initX, initY, r):
    global totalIndex
    if(r==4):
        newInitY = initY
        for i in range(2):
            newInitX = initX
            for j in range(2):
                tempPerm = list(sorted_perm_list[totalIndex])
                index = 0
                for k in range(1, n+1):
                    if not k in tempPerm:
                        tempPerm.insert(index, k)
                        index+=1
                hexagonPos(tempPerm, -newInitX, -newInitY)
                newInitX += spacerP4
                totalIndex+=1
            newInitY += spacerP4
        return 
    for k in range(r, 0, -1):
        newInitX = radii[r-5]*math.cos(2*math.pi*k/r) + initX
        newInitY = radii[r-5] * math.sin(2*math.pi*k/r) + initY
        genInitPos(newInitX, newInitY, r-1)
    return

def getColors():
    max = 0
    for i in range(numPerms):
        perm = list(allPerms[i])
        dist = getDistPerm(perm)
        if(dist>max):
            max=dist
        permString = permToString(perm)
        permDists[permString] = dist
    
    green = Color("green")
    colors = list(green.range_to(Color("blue"),max))
    colors.append(Color("red"))
    for i in range(max+1):
        colors[i] = colors[i].get_hex()
    for i in range(numPerms):
        perm = list(allPerms[i])
        permString = permToString(perm)
        dist = permDists[permString]
        nodeColors[permString] = colors[dist]

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
def drawGraph():
    edges = getEdgesFromDict(Color('grey'), edgeDict)
    elements = nodes + edges
    print("elements ", elements)
    app.layout = html.Div([
        cyto.Cytoscape(
            id='cytoscape-layout-1',
            elements=elements,
            style={'width': '100%', 'height': '750px'},
            layout={
                'name': 'preset'
            }
        ),
        html.P(id='cytoscape-tapNodeData-output')
    ])

if __name__ == "__main__":
    cmdLine = CommandLineEstimate()
    radii = [75, 250, 850, 2600]

    allPerms = permutations(n)
    numPerms = len(allPerms)
    genEdges(n)
    permStrings = []
    for i in range(numPerms):
        allPerms[i] = list(allPerms[i])
        perm = allPerms[i]
        permStrings.append(permToString(perm))
    permX = {}
    permY = {}
    nodeTuples = []

    sorted_perm_list = colexicographicPermutations(n)
    totalIndex = 0
    genInitPos(0,0,n)

    nodeColors = {}
    permDists = {}
    #Assign colors to nodes
    colors = []
    loadDistFile(n)
    getColors()

    for i in range(numPerms):
        nodeTuples.append((permStrings[i], permStrings[i], permY[permStrings[i]], permX[permStrings[i]], nodeColors[permStrings[i]]))
    nodes = [
        {
            'data': {'id': short, 'label': label},
            'position': {'x': 20 * lat, 'y': -20 * long},
            'style': {'background-color': color, "height": 150, "width": 150},

        }
        for short, label, long, lat, color in (nodeTuples)
    ]
    drawGraph()






@app.callback(Output('cytoscape-layout-1', 'elements'),
              Input('cytoscape-layout-1', 'tapNodeData'))
def displayTapNodeData(data):
    if data:
        
        perm = nodeIDToList(data['label'])
        drawPath(perm)
        addedEdgeDict = getAddedDict()
        edges = getEdgesFromDict(Color("red"), addedEdgeDict)
        elements = nodes + edges
        return elements
    else:
        edgeDict = getEdgeDict()
        return nodes+ getEdgesFromDict(Color("grey"), edgeDict)
        

if __name__ == '__main__':
    app.run(debug=True, port=1718)

