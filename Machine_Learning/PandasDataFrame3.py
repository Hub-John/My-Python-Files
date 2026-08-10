import pandas as pd

def main():
    #series > dataframe > panel
    Data = {
        "Name" : ["Sagar", "Amit", "Pooja"],
        "Age" : [27, 28, 25],
        "City" : ["Pune", "Kolhapur", "Satara"]
    }

    dobj = pd.DataFrame(Data)

    print(dobj[["Name", "Age"]]) # This is a "Panel"

if __name__ == "__main__":
    main()