from sklearn.datasets import load_iris

def main():
    print("_"*30)
    print("Iris Classification case studies")
    print("_"*30)

    Dataset = load_iris()

    # MetaData of the Dataset
    print("Independent variable are: ")
    print(Dataset.feature_names)
    print("_"*30)
    print("Dependent variable are: ")
    print(Dataset.target_names)

if __name__ == "__main__":
    main()