def Area(Radious, PI):
    Ans = PI * Radious * Radious
    return Ans

def main():
    Ret = Area(10.5, 3.14)
    print("Area of Circle is:", Ret)

    Ret = Area(13.6, 7.12)
    print("Area of Circle is:", Ret)

if __name__ == "__main__":
    main()


#Positional Parameter/Argument