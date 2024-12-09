



totalIndex = 0
initX = 0
initY = 0 
odd = True
for k in range(2):
    initX = 0
    for l in range(2):
        
        newInitY = initY
        for i in range(2):
            newInitX = initX
            for j in range(2):
                print(sorted_perm_list[totalIndex], " x ", newInitX, " y ", newInitY)
                newInitX += 1
                totalIndex+=1
            newInitY += 1
        initX = newInitX
    initY = newInitY
if(odd):
    newInitYOdd  = initY-2.5
    for i in range(2):
        newInitXOdd = initX-2.5
        for j in range(2):
            print(sorted_perm_list[totalIndex], " x ", newInitXOdd, " y ", newInitYOdd)
            newInitXOdd += 1
            totalIndex+=1
        newInitYOdd += 1

def genInitPos(initX, initY, r):
    global totalIndex
    if(r==4):
        newInitY = initY
        for i in range(2):
            newInitX = initX
            for j in range(2):
                print(sorted_perm_list[totalIndex], " x ", newInitX, " y ", newInitY)
                newInitX += 1
                totalIndex+=1
            newInitY += 1
        initX = newInitX
        return newInitX, newInitY
    odd = (r % 2)==1
    newInitX = initX
    for k in range(r):
        newInitX = 10 * r * math.cos(2*math.pi*k/n) + initX
        newInitY = 10 * r * math.sin(2*math.pi*k/n) + initY
        newInitX, newInitY = genInitPos(newInitX, newInitY, r-1)
        #initY = newInitY
    # if(odd):
    #     genInitPos(newInitX-width - 0.5, newInitY-width - 0.5, r-1)
    return newInitX, newInitY


totalIndex = 0
n=6
genInitPos(0,0,n)