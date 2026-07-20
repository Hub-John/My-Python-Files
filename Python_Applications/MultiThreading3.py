import threading

def Display(no): #def Display(*No)
    print(f"Inside Display {no}: ", threading.get_ident())

def main():
    print("Inside Main: ", threading.get_ident())

    tobj = threading.Thread(target=Display, args=(11), ) #Error

    tobj.start()

if __name__ == "__main__":
    main()