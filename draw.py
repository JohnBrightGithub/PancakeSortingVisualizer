from dash import Dash, html
import dash_cytoscape as cyto
from path import getEdgeDict
from dash.dependencies import Input, Output
import math
from colour import Color
from path import drawPath
from path import flip
from path import genEdges
from path import getAddedDict
from common import permToString
from common import colexicographicPermutations
from common import permutations
from common import nodeIDToList
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
def drawGraph(layoutName):
    edgeDict = getEdgeDict()
    edges = getEdgesFromDict(Color('grey'), edgeDict)
    elements = nodes + edges
    #print("nodes ", nodes)
    #print("edges ", edges)
    app.layout = html.Div([
        cyto.Cytoscape(
            id='cytoscape-layout-1',
            elements=elements,
            style={'width': '100%', 'height': '750px'},
            layout={
                'name': layoutName
            }
        ),
        html.P(id='cytoscape-tapNodeData-output')
    ])
#["random","preset","circle","concentric","grid","breadthfirst","cose","cose-bilkent","fcose","cola","euler","spread","dagre","klay"].

app = Dash(__name__)
@app.callback(Output('cytoscape-layout-1', 'elements'),
            Input('cytoscape-layout-1', 'tapNodeData'))

def displayTapNodeData(data):
    if data:
        label = data['label']
        perm = nodeIDToList(label)
        drawPath(perm)
        addedEdgeDict = getAddedDict()
        edges = getEdgesFromDict(Color("red"), addedEdgeDict)
        elements = nodes + edges
        return elements
    else:
        edgeDict = getEdgeDict()
        return nodes+ getEdgesFromDict(Color("grey"), edgeDict)

nodes = []
def runAppAndDraw(nodeList, layout='preset'):
    cyto.load_extra_layouts()
    global nodes
    nodes = nodeList
    drawGraph(layout)
    
    app.run(debug=True, port=1718)
    