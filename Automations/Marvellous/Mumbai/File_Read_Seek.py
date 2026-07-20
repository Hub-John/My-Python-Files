# Seek(Kuthe, Kuthun)
# Kutun : 0/1/2

# 0 Starting
# 1 Current
# 2 End

def main():
    try:
        fobj = open("Demo.text", "r")
        print("File gets opened")

        fobj.seek(10, 0)

        data = fobj.read()
        print(data)
        
        fobj.close()
    
    except FileNotFoundError as fobj:
        print("File is not present current directory.")

if __name__ == "__main__":
    main()