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

    # Step 4: Elbow Method
    WCSS = []
    for k in range(1, 11):
        model = KMeans(
            n_clusters = k,
            random_state = 42,
            n_init = 10
        )

        model.fit(X_scaled)
        WCSS.append(model.inertia_)

    print("\nValues of WCSS: ")

    for i in range(len(WCSS)):
        print(f"{i+1} : {WCSS[i]}")

    # Step 5: Visulisation
    plt.plot(range(1,11), WCSS, marker = "o")
    plt.xlabel("Number of Clusters: k")
    plt.ylabel("WCSS")
    plt.title("Marvellous Elbow Method")
    plt.grid(True)
    # plt.show()

    # Step 5: Final Model
    model = KMeans(
                n_clusters = 4,
                random_state = 42,
                n_init = 10
            )

    clusters = model.fit_predict(X_scaled)
    df["Cluster"] = clusters
    print("\nDataset with clusters: ")
    print(df.head(20))

if __name__ == "__main__":
    main()