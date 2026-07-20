import sys
import os

def DirectoryScanner(DirectoryPath):
    
    print("Files from the directory are: ")
    
    for FolderName, SubFolder, FileName in os.walk(DirectoryPath):

        for fname in FileName:
            print(fname)

def main():

    Border = "-"*50
    print(Border)
    print("Automatin Script")
    print(Border)

    
    if(len(sys.argv) == 2):

        if(sys.argv[1] == "--h" or sys.argv[1] == "--H"):
            print("This automation script is used travel the directory")
            print("For better usage please check --u flag")
        elif(sys.argv[1] == "--u" or sys.argv[1] == "--U"):
            print("Please execute script as")
            print("python3 File.name.py DirectoryName")
            print("Direectory name should be absolute path")
        else:
           DirectoryScanner(sys.argv[1])
    
    else:
        print("Invalid number of argument")
        print("Please use --h or --u for more information")


    print(Border)
    print("Thank you for automation script ")
    print(Border)

if __name__ == "__main__":
    main()