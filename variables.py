globalVariable = 1

def addVariable():
    global globalVariable
    globalVariable+=1
    print(globalVariable)

addVariable()
print(globalVariable)

