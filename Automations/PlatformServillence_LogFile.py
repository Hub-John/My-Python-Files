import psutil
import sys
import os

def PlatforServillence(FolderName):
    border = "_"*50

    Ret = False

    Ret = os.path.exists(FolderName)

    if(Ret == True):
        Ret = os.path.isdir(FolderName)
        if(Ret == False):
            print("Unable to processed as directory name is existing but its not a directory")
            return
    else:
        os.mkdir(FolderName)
        print("\nDirectory for the log file gets created successfully")

def main():
    border = "_"*50

    print(border)
    print("\nMarvellous Platform Servillence System")
    print(border)

    # --h and --u handling
    if(len(sys.argv) == 2):
        if(sys.argv[1] == "--h" or sys.argv[1] == "--H"):
            print("\nThis script use to perform")
            print("1: It fetch the information of running process")
            print("2: It fetch the information of running RAM")
            print("3: It fetch the information of Secondary Stroage")
            print("4: It fetch the information of microprocessor")
            print("5: It get auto scheduled periodically")
            print("6: It maintains all records into log file")
            print("7: It send the log files through mail periodically")
        elif(sys.argv[1] == "--u" or sys.argv[1] == "--U"):
            print("\nUse the automation script as: ")
            print(f"Python {sys.argv[0]} Time_Interval Folder_Name")
            print("Time_Interval: Time in minutes for periodic execution")
            print("Folder_Name: Name of folder for the log file creation")
        else:
            print("\nUnable to proceed as there is no mathching argument")
            print("Please use --h or --u flag getting more details")
            

    # Actual Project Code
    elif(len(sys.argv) == 3):
        PlatforServillence(sys.argv[2])

    else:
        print("\nInvalid number of argument")
        print("Unable to proceed as argument are not matching")
        print("Please use --h or --u flag getting more details")

    print(border)
    print("\nThan you for using out Automation System")
    print(border)

if __name__ == "__main__":
    main()