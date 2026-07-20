def CheckEven(No):

    if(No % 2 == 0):
        print("Its Even number")
    else:
        print("Its Odd number")

def main():
    Value = int(input("Enter Number: ")) # Input will do two task: Taking input and print statement

    CheckEven(Value)

if __name__ == "__main__":
    main()