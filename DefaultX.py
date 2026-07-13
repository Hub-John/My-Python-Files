def Area(PI=3.14, Radious):     #Error
    Ans = PI * Radious * Radious
    return Ans

def main():
    Ret = Area(17.4)
    print("Area of Circle is:", Ret)

    Ret = Area(17.4,20.14)
    print("Area of Circle is:", Ret)

if __name__ == "__main__":
    main()


#Default Parameter/Argument