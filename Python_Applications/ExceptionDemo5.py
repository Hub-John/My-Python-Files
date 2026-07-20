def main():
    
    Ans = 0

    try:
        print("Enter First Number: ")
        No1 = int(input())

        print("Enter Second Number: ")
        No2 = int(input())

        Ans = No1 / No2     # Error occours here

        print("Division is succesful")
    
    except Exception as eobj: # Generic Exception = It will catch everything
        print("Exception occured: ", eobj)

    # except ZeroDivisionError as zobj: # Input = 0
    #     print("Exception occured due to second operand is zero: ", zobj)
    
    # except ValueError as vobj: # Input = character h
    #     print("Exception occured due to invalid data type: ", vobj)

    print("Result is:", Ans)

if __name__ == "__main__":
    main()