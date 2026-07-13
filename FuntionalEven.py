CheckEven = lambda No : (No % 2 == 0)
        
def main():
    Value = int(input("Enter Number: ")) # Input will do two task: Taking input and print statement

    Ret = CheckEven(Value) # Ret = (Value % 2 == 0)

    if(Ret == True):
        print("Its Even Number")
    else:
        print("Its Odd Number")

if __name__ == "__main__":
    main()