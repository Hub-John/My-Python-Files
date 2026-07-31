import sys
import os
import hashlib

def CalculateCheckSum(FileName):
    fobj = open(FileName, "rb")

    hobj = hashlib.md5()

    Buffer = fobj.read(1024)

    while(len(Buffer) > 0):
        hobj.update(Buffer)
        Buffer = fobj.read(1024)

    fobj.close()

    return hobj.hexdigest()

def FindDuplicate(DirectoryName):

    Ret = False

    Ret = os.path.exists(DirectoryName)

    if Ret == False:
        print("PATH is invalid")
        return 

    Ret = os.path.isdir(DirectoryName)

    if Ret == False:
        print("It is not directory")
        return

    Duplicate = {}

    for FolderName, SubFolder, FileName in os.walk(DirectoryName):

        for fname in FileName:
            fname = os.path.join(FolderName, fname)

            Checksum = CalculateCheckSum(fname)

            # print(f"{fname} : {Checksum}")

            if Checksum in Duplicate:
                Duplicate[Checksum].append(fname)
            else:
                Duplicate[Checksum] = [fname]

        return Duplicate

def DeleteDuplicate(DirectoryName):
    MyDict = FindDuplicate(DirectoryName)

    Result = list(filter(lambda x : len(x) > 1, MyDict.values())) # very important Line

    count = 0
    TotalDeleted = 0

    for value in Result:

        for subvalue in value:
            count = count + 1  # Run 4 Times

            if count > 1:
                os.remove(subvalue)
                print("Duplicate Found :", subvalue)
                TotalDeleted = TotalDeleted + 1

        count = 0

    print("Total Delated Files: ", TotalDeleted)

def main():

    Data = DeleteDuplicate("Test")

if __name__ == "__main__":
    main()