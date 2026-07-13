import Marvellous as MI #Alise the import file name

def main():
    print("Enter first Numer:")
    value1 = int(input())

    print("Enter Second Numer:")
    value2 = int(input())

    Ret = MI.Addition(value1, value2)  #Error already is here to just demo

    print("Addition is: ", Ret)

if __name__ == "__main__":      #True #__name = what is your name?
    main()


# Example: Bhaji & Ice Cream Vender