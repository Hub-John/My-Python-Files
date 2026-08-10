import pandas as pd # EDA

import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier

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


########################################################
# Step 4: Visualise of Dataset
########################################################

print(Border)
print("Step 4: Visualise of Dataset")
print(Border)

# Scatter plot
plt.figure(figsize=(7,5))

for sp in df["species"].unique():

    temp = df[df["species"] == sp]
    plt.scatter(temp["petal length (cm)"], temp["sepal width (cm)"],label = 50)


plt.title("Marvellous Iris Case Study")

plt.xlabel("petal length (cm)")
plt.ylabel("petal width (cm)")


plt.legend()
plt.grid()
plt.show()


########################################################
# Step 5: Split the dataset for training and testing
########################################################

print(Border)
print("Step 5: Split the dataset for training and testing")
print(Border)

x_train, x_test, y_train, y_test = train_test_split(x,y,test_size=5, random_state=42) #data shuffling

print("Dataset spliting activity done")

print("X: ", x.shape) # (150,4)
print("Y: ", y.shape) # (150, o)

print("x_train: ", x_train.shape) # 75,4
print("x_test: ", x_test.shape)   # 75,4

print("y_train: ", y_train.shape) # 75,
print("y_test: ", y_test.shape)   # 75,


########################################################
# Step 6: Build the model
########################################################

print(Border)
print("Step 6: Build the model")
print(Border)

model = DecisionTreeClassifier(max_depth=5)

print("Model gets created successfully")