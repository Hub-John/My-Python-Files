def Addition(No1, No2): #Inside Bracket Parameters
    ans = 0             #Local Variable(It is int)
    ans = No1 + No2     #Business logic
    return ans          #who ever call this funtion it will return

def main():
    print("Enter first Numer:")
    value1 = int(input())

    print("Enter Second Numer:")
    value2 = int(input())

    Ret = Addition(value1, value2)

    print("Addition is: ", Ret)

if __name__ == "__main__":      #True #__name = what is your name?
    main()


# Example: Bhaji & Ice Cream Vender