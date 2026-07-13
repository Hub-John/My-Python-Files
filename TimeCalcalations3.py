import time

def Factorial(no):
 
    Fact = 1

    for i in range(1, no + 1):
        Fact = Fact * i  # i == collector
    
    return Fact

def main():
    value = int(input("Enter Number:"))

    start_time = time.time() # time is method

    Ret = Factorial(value)

    end_time = time.time() # time is method

    print(f"Factorial of {value} is {Ret}") # Formatted Printing

    print(f"Time required is {end_time-start_time} seconds")

if __name__ == "__main__":
    main()