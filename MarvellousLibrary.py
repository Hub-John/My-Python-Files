def filterX(Task, Elements):
    result = [] # Empty list data types

    for no in Elements:
        Ret = Task(no)  #CheckEven(no)
        
        if(Ret == True):
            result.append(no)
    return result

def mapX(Task, Elements):
    result = []

    for no in Elements:
        Ret = Task(no) #Increment(No)
        result.append(Ret)
    return result

def reduceX(Task, Elements):
    sum = 0

    for no in Elements:
        sum = Task(sum, no)

    return sum