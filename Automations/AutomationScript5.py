import sys

def main():
    
    if(len(sys.argv) == 2):
        
        print("-----------------------------------------------")
        print("Automatin Script")
        print("-----------------------------------------------")

        if(sys.argv[1] == "--h" or sys.argv[1] == "--H"):
            print("This automation script is used travel the directory")
            print("For better usage please check --u flag")
        elif(sys.argv[1] == "--u" or sys.argv[1] == "--U"):
            print("Please execute script as")
            print("python3 File.name.py DirectoryName")
            print("Direectory name should be absolute path")
        else:
            DirectoryName = sys.argv[1]
            print("Directory name is:", DirectoryName)    
    else:
        print("Invalid number of argument")
        print("Please use --h or --u for more information")

    print("-----------------------------------------------")
    print("Thank you for automation script ")
    print("-----------------------------------------------")

if __name__ == "__main__":
    main()