def main():
    try:
        fobj = open("Demo.text", "r")
        print("File gets opened")

        data = fobj.read(5)
        print(data)

        fobj.seek(10, 0)

        data = fobj.read(5)
        print(data)
        
        fobj.close()
    
    except FileNotFoundError as fobj:
        print("File is not present current directory.")

if __name__ == "__main__":
    main()