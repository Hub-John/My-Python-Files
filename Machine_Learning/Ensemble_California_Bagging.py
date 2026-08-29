import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import BaggingRegressor
from sklearn.metrics import mean_squared_error, r2_score


################################################################
# Step 1: Load the Dataset
################################################################

df = pd.read_csv("california_housing.csv")
print("\nShape of Dataset: ", df.shape)
print("\nFirst few records: ", df.head())


################################################################
# Step 2: Separate feature and lables
################################################################

X = df.drop("target", axis=1)
Y = df["target"]

print("\nShape of X: ", X.shape)
print("Shape of Y: ", Y.shape)

################################################################
# Step 3: Split dataset for training and testing
################################################################

X_train, X_test, Y_train, Y_test = train_test_split(X,Y,test_size=0.2,random_state=42)

################################################################
# Step 4.1: Create the base model
################################################################

base_model = DecisionTreeRegressor(random_state=42)

################################################################
# Step 4.2: Create the bagging model
################################################################

model = BaggingRegressor(
    estimator=base_model,
    n_estimators=10,
    random_state=42
)

################################################################
# Step 5: Train the model
################################################################

model = model.fit(X_train,Y_train)

################################################################
# Step 6: Test the model
################################################################

Y_pred = model.predict(X_test)

################################################################
# Step 7: Evaluate the model
################################################################

print("\nMean Square Error: ", mean_squared_error(Y_test,Y_pred))
print("\nR2: ", r2_score(Y_test,Y_pred))