import pandas as pd
import matplotlib.pyplot as plt

from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans

def main():

    # Step 1: Load the data
    df = pd.read_csv("Mall_Customers.csv")
    print("\nDataset loaded with values: ")
    print(df.head())
    print("\nMissing values: ")
    print(df.isnull().sum())

    # Step 2: Feature selection
    X = df[["AnnualIncome", "SpendingScore"]]
    print("\nSelected features: ")
    print(X.head())

    # Step 3: Scale the data
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)
    print("\nScaled Data: ")
    print(X_scaled[:5])

if __name__ == "__main__":
    main()