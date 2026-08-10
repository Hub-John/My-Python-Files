import pandas as pd

Border = "_"*30
########################################################
# Step 1: Load the dataset
########################################################

print(Border)
print("Step 1: Load the dataset")
print(Border)

DataPath = "iris.csv" 

df = pd.read_csv(DataPath) # df = dataframe

print("Dataset load succesfully")

print("Initial entries from dataset are: ")
print(df.head())

########################################################
# Step 2: Data Analysis (EDA)
########################################################

print(Border)
print("Step 2: Load data analysis")
print(Border)

print("Shape of dataset: ", df.shape) # all data display

print("Column names: ", list(df.columns)) # column only print

print("Missing values per column: ") # empty cell

print(df.isnull().sum()) # is cononical methed - total count

print("Class distribution (species count)")

print(df["species"].value_counts())

print("Statistical report of dataset: ")

print(df.describe())


########################################################
# Step 3: Decides Independent and Dependent variables
########################################################

print(Border)
print("Step 3: Decides Independent and Dependent variables")
print(Border)

# x = Independent varialbe / fetures
# y = Dependent variable / labels

fetures_cols = [
    "sepal length (cm)",
    "sepal width (cm)",
    "petal length (cm)",
    "petal width (cm)"
    ]

x = df[fetures_cols] # 150 * 4
y = df["species"]    # 150 * 1/0

print("X Shape: ", x.shape)
print("Y Shape: ", y.shape)