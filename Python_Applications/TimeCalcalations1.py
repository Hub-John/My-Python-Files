# 6 : 1 * 2 * 3 * 4 * 5 * 6

def Factorial(no):
 
    Fact = 1

    for i in range(1, no + 1):
        Fact = Fact * i  # i == collector
    
    return Fact

def main():
    value = int(input("Enter Number:"))

    Ret = Factorial(value)

    print("Factorial Number: ", Ret)

if __name__ == "__main__":
    main()