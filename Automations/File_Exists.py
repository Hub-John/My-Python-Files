import os

def main():
    ret = os.path.exists("Demo.text")

    if ret == True:
        print("File is present in currect directory")
    else:
        print("There is no such file")


if __name__ == "__main__":
    main()