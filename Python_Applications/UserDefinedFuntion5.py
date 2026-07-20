# Accept : Multiple Parameters - 2 or more
# Return : Multiple Values     - 2 or more

def Marvellous(value1, Value2):
    print("Inside Marvellous:", value1, Value2)
    return 21, 51

def main():
    Ret1, Ret2 = Marvellous(10, 20)     #Multiple Bags from Home
    print("Return Values are: ", Ret1, Ret2)
     
if __name__ == "__main__": #Entry Point
    main()