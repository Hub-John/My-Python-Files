from Marvellous import Addition  # Additon funtion will import in this case

def main():
    print("Enter first Numer:")
    value1 = int(input())

    print("Enter Second Numer:")
    value2 = int(input())

    Ret = Addition(value1, value2)

    print("Addition is: ", Ret)

    Ret = Substraction(value1, value2)      #Error

    print("Substraction is: ", Ret)

if __name__ == "__main__":      #True #__name = what is your name?
    main()


# Example: Bhaji & Ice Cream Vender