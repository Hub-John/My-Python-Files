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