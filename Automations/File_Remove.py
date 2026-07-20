import os

def main():
    try:
        
        # fobj.remove() => Not applicable
        os.remove("Demo.text")

    except FileNotFoundError as fobj:
        print("File is not present current directory.")

if __name__ == "__main__":
    main()