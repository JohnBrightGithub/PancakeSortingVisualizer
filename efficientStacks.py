from collections import deque
from pancakeDist import getDistPerm
from draw import drawEdge
from common import nodeIDToList
from common import permToString
from common import flip
from common import findAllNeighbors

def bfs(start, r):
    # Create a queue for BFS
    queue1 = deque([start])
    queue2 = deque()
    n = len(start)
    # Keep track of visited nodes
    visited = set()
    visited.add(permToString(start))

    # List to store the order of traversal
    traversal_order = []
    index = 0
    while queue1:
        while(queue1):
            node = queue1.popleft()
            traversal_order.append(node)
            allNeighbors = findAllNeighbors(node, n)
            for adj in allNeighbors:
                neighbor = permToString(adj)
                if neighbor not in visited:
                    queue2.append(adj)
                    visited.add(neighbor)
        if(queue2):
            index+=1
            if(index==r):
                return traversal_order
        while(queue2):
            node = queue2.popleft()
            traversal_order.append(node)
            allNeighbors = findAllNeighbors(node, n)
            for adj in allNeighbors:
                neighbor = permToString(adj)
                if neighbor not in visited:
                    queue1.append(adj)
                    visited.add(neighbor)
        if(queue1):
            index+=1
            if(index==r):
                return traversal_order
    print(index)
    
    return traversal_order

def drawEfficient(n, r):
    start = []
    for i in range(n):
        start.append(i+1)
    print(bfs(start, r))
    

drawEfficient(6, 3)