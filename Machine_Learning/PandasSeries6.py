import pandas as pd

def main():
    sobj = pd.Series([11, 21, 51, 101], index=["C", "C++", "Java", "Python"]) # You can define custom indexing

    print(sobj)

    print(sobj["Python"]) # Access index through this line

if __name__ == "__main__":
    main()