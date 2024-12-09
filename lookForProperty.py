from common import nodeIDToList
from common import permutations
from common import pathStringToArrs
from pancakeDist import loadDistFile
from path import drawPath
from path import getAddedDict
perms = []
def init(n):
    global perms
    perms = permutations(n)
    loadDistFile(n)

def lookForAllPaths(property):
    global perms
    for perm in perms:
        perm = list(perm)
        lookForPropetyInPaths(perm, property)
def lookForPropetyInPaths(perm, property):
    drawPath(perm)
    paths = getAddedDict()
    if(len(paths)==0):
        return False
    if(property(paths)):
        print("property found! ")
        print(paths)
        return True
def pathChangesLast(path):
    #print("pathChangesLast ", path)
    n=len(path[0])
    firstLastEl = int(path[0][-1])
    for perm in path:
         lastEl = perm[-1]
         #print("lastEl ", lastEl, " firsLtEl ", firstLastEl)
         if(lastEl!=firstLastEl and lastEl!=n):
              return True
    return False
def allPathsChangeLast(paths):
    #print("paths: ", paths)
    for path in paths:
        path = pathStringToArrs(path)
        if(not pathChangesLast(path)):
             return False
    return True

def testAllPathsChangeLast():
    paths = ['[3,4,2,1], [1,2,4,3], [1,2,3,4]', '[3,4,2,1], [1,3,4,2], [1,2,3,4]']
    print(allPathsChangeLast(paths))

# n=9
#init(n)
# lookForAllPaths(allPathsChangeLast)
#testAllPathsChangeLast()