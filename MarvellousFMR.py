CheckEven = lambda No : (No % 2 == 0)
Increment = lambda No : No + 1
Addition = lambda No1, No2 : No1 + No2


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


def main():
    Data = [13,12,8,10,11,20]

    print("Input Data Is:", Data)

    FData = list(filterX(CheckEven, Data)) # Filter Data

    print("Data After Filter:", FData)

    MData = list(mapX(Increment, FData)) # Map Data

    print("Data After Map:", MData)

    RData = reduceX(Addition, MData)

    print("Data After Reduce:", RData) # Reduce Data

if __name__ == "__main__":
    main()