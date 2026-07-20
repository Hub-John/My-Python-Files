import os

def main():

    if (os.path.exists("Demo.text")):
        print("File is present in currect directory")
    else:
        print("There is no such file")


if __name__ == "__main__":
    main()