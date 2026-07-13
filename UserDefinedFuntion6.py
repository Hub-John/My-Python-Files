def Multiplication(No1, No2):
    return No1 * No2

def Division(No1, No2):
    return No1 / No2

def main():
    Ret1 = Multiplication(10, 5)    #Multiplication Shop 1
    print("Multiplication is:", Ret1)

    Ret2 = Division(12,6)           #Division Shop 2
    print("Division is:", Ret2)
     
if __name__ == "__main__": #Entry Point
    main()