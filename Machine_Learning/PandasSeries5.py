import pandas as pd

def main():
    sobj = pd.Series([11, 21, 51, 101], index=[5, 6, 7, 8]) # You can define custom indexing

    print(sobj)

    print(sobj[7]) # Access index through this line

if __name__ == "__main__":
    main()