def Area(Radious, PI): # Parameters
    Ans = PI * Radious * Radious
    return Ans

def main():
    Ret = Area(PI=3.14, Radious=10.5) # Arguments
    print("Area of Circle is:", Ret)

if __name__ == "__main__":
    main()


# Keyword Parameter/Argument