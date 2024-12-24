import pandas as pd
from common import permToString
distances = {}
def loadDistFile(n):
    xls = pd.ExcelFile('ASearch/PancakeDistances.xlsx')
    sheetString = "n=" + str(n)
    df = pd.read_excel(xls, sheetString, header=None)
    df = df.values.tolist()
    for row in df:
        dist = row[0]
        perm = row[1:-1]
        permString  = permToString(perm)
        distances[permString] = dist

def getDistPerm(perm):
    permString  = permToString(perm)
    return distances[permString]