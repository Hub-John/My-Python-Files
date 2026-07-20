import os

def main():
    for FolderName, SubFolder, FileName in os.walk("Marvellous"):
        print("Folder name:", FolderName)

        for subf in SubFolder:
            print("Sub Folder Name: ", subf)

        for fname in FileName:
                print("File Name: ", fname)

if __name__ == "__main__":
    main()