import pandas as pd

def main():
    sobj = pd.Series([27000, 32000, 35000], index=["Amit", "Sagar", "Sagar"]) # You can define custom indexing

    print(sobj)

    print(sobj["Sagar"]) # Access index through this line

if __name__ == "__main__":
    main()