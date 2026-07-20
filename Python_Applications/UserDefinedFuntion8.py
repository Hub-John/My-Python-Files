def BigBazar():
    print("Inside BigBazar")

    def Amul():
        print("Inside Amul Ice-cream parlor")

def main():
    BigBazar()      #Allowed
    Amul()          #Error
    BigBazar.Amul() #Error
    
if __name__ == "__main__":
    main()