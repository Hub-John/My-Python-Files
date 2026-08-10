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