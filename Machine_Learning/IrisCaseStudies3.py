from sklearn.datasets import load_iris

def main():
    print("_"*30)
    print("Iris Classification case studies")
    print("_"*30)

    Dataset = load_iris()

    # MetaData of the Dataset
    print("Independent variable are: ")
    print(Dataset.feature_names)
    print("Length of Independent variable: ", len(Dataset.feature_names))

    print("Dependent variable are: ")
    print(Dataset.target_names)
    print("Length of Dependent variable: ", len(Dataset.target_names))

if __name__ == "__main__":
    main()