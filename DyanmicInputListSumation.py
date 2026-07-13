def Sumation(Data):
    sum = 0

    for no in Data:
        sum = sum + no
     
    return sum

def main():
    Size = 0
    Arr = list() # Empty object list

    print("Enter the number of elements: ")
    Size = int(input())

    print("Enter the elements: ")
    for i in range(Size):
        no = int(input())
        Arr.append(no)

    Ret = Sumation(Arr)

    print("Sumation is:", Ret)
    
if __name__ == "__main__":
    main()