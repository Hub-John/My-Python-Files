import pandas as pd
import matplotlib.pyplot as plt

from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix
from sklearn.preprocessing import StandardScaler

def MarvellousClassifier(DataPath):

    border = "-"*50

    # Step 1: Load the dataset from CSV file
    print(border)
    print("Step 1: Load the dataset from CSV file")
    print(border)

    df = pd.read_csv(DataPath)

    print(border)
    print("Some entries from dataset:")
    print(df.head())
    print(border)


    # Step 2: Clean the dataset
    print(border)
    print("Step 2: Clean the dataset")
    print(border)

    df.dropna(inplace=True) # Remove missing values (at least one value missing)

    print("Shape of dataset:", df.shape)
    print("Total records: ", df.shape[0])
    print("Total columns: ", df.shape[1])

    print(border)

    # Step 3: Seperate independent and dependent variables
    print(border)
    print("Step 3: Seperate independent and dependent variables")
    print(border)

    X = df.drop(columns=['Class']) # csv "Class" column exclude
    Y = df["Class"]

    print("Shape of X: ", X.shape)
    print("Shape of Y: ", Y.shape)

    print(border)
    print("Input Columns: ", X.columns.to_list())
    print("Output Columns: ", "Class")
    

def main():
    MarvellousClassifier("WinePredictor.csv")

if __name__ == "__main__":
    main()