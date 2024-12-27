import itertools
def permToString(perm):
    return str(perm)

def permutations(n):
    return list(itertools.permutations(range(1,(n+1))))

def colexicographicPermutations(n):
    
    # Generate all permutations of n numbers
    perm_list = itertools.permutations(list(range(1, n + 1)), r=n-3)
    
    # Sort the permutations in colexicographic order
    sorted_perm_list = sorted(perm_list, key=lambda x: x[::-1], reverse=True)

    return sorted_perm_list
def pathStringToArrs(path):
    edges = path.split("],")
    #print("edgesSplit: ", edges)
    retEdges = []
    for edge in edges:
        edge = edge.replace(")", "")
        edge = edge.replace("(", "")
        retEdges.append(nodeIDToList(edge))
    #print("retEdges: ", retEdges)
    return retEdges
def nodeIDToList(permStr):
    permStrList = permStr.replace("[", "")
    permStrList = permStrList.replace("]", "")
    permStrList = permStrList.split(",")
    perm = []
    for permStr in permStrList:
        perm.append(int(permStr))
    return perm

def flip(perm, flip):
    newPerm = perm.copy()
    newPerm[0:flip+1] = newPerm[0:flip+1][::-1]
    return newPerm

def isEfficient(state, move, n):
     if move==n:
          if state[0]==n:
               return True
     elif(abs(state[0]-state[move])==1):
          if(abs(state[move-1]-state[move])!=1):
            return True
     return False

def isdefficient(state, move, n):
     if move==n:
          if state[-1]==n:
               return True
     elif(abs(state[0]-state[move])!=1):
          if(abs(state[move-1]-state[move])==1):
            return True
     return False

def findAllEffNeighbors(perm, n):
    edges = []
    for i in range(1, n):
        if(isdefficient(perm, i, n)):
            node2 = flip(perm, i)
            edges.append(node2)
    return edges

def findAllEdges(perm, upTo):
    edges = []
    if(upTo!=-1):
        n = upTo
    else:
        n = len(perm)
    for i in range(1, n):
        node2 = flip(perm, i)
        edges.append((perm, node2))
    return edges