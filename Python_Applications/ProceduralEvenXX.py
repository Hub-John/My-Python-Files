def CheckEven(No):
    return (No % 2 == 0)
        
def main():
    Value = int(input("Enter Number: ")) # Input will do two task: Taking input and print statement

    Ret = CheckEven(Value)

    if(Ret == True):
        print("Its Even Number")
    else:
        print("Its Odd Number")

if __name__ == "__main__":
    main()