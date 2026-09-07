####### --------------- Deep Learning Pipeline ---------------
# 1  - Read the data from CSV
# 2  - Data Analysis (Exploratory Data Analysis - EDA)
# 3  - Preprocessing
# 4  - Train Test Split
# 5  - Feature Scaling
# 6  - FNN Model Training (Machine Learning to Deep Learning)
# 7  - Model Evaluation
# 8  - Graphical Representation
# 9  - Model Preserve
# 10 - Model Loading & Preserve
# 11 - Test Unseen Data
####### --------------- Deep Learning Pipeline ---------------

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import joblib

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score, confusion_matrix

# -------------------------------------------------------------
# Step 1 - Read the data from CSV
# -------------------------------------------------------------

print("-------------------------------")
print("Step 1 - Read the data from CSV")
print("-------------------------------")

data = pd.read_csv("placement_data.csv")

print("Complete dataset: ")
print(data)

# -------------------------------------------------------------
# Step 2 - Data analysis (Exploratory data analysis - EDA)
# -------------------------------------------------------------

print("-------------------------------")
print("Step 2 - Data analysis (Exploratory data analysis - EDA)")
print("-------------------------------")

print("First 5 rows: ")
print(data.head())

print("\nColumns names: ")
print(data.columns)

print("\nShape of data: ")
print(data.shape)

print("\nStatistical summary: ")
print(data.describe())

# -------------------------------------------------------------
# Step 3 - Preprocessing
# -------------------------------------------------------------

print("-------------------------------")
print("Step 3 - Preprocessing")
print("-------------------------------")

X = data[['Aptitude', 'Coding', 'Communication', 'Academics', 'Internship']]
Y = data['Placed']

print("Input features: ")
print(X.head())

print("\nTarget: ")
print(Y.head())

# -------------------------------------------------------------
# Step 4 - Train test split
# -------------------------------------------------------------

print("-------------------------------")
print("Step 4 - Train test split")
print("-------------------------------")

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.30, random_state=42)

print("Training input shape: ", X_train.shape)
print("\nTesting input shape: ", X_test.shape)
print("\nTraining output shape: ", Y_train.shape)
print("\nTesting output shape: ", Y_test.shape)

# -------------------------------------------------------------
# Step 5 - Feature scaling
# -------------------------------------------------------------

print("-------------------------------")
print("Step 5 - Feature scaling")
print("-------------------------------")

scalar = StandardScaler()

X_train_scaled = scalar.fit_transform(X_train)
X_test_scaled = scalar.fit_transform(X_test)

print("Scaled training data: ")
print(X_test_scaled[:5])

# -------------------------------------------------------------
# Step 6 - FNN model training
# -------------------------------------------------------------

print("-------------------------------")
print("Step 6 - FNN model training")
print("-------------------------------")

model = MLPClassifier(
    hidden_layer_sizes=(8,4),
    activation='relu',
    solver='adam',
    max_iter=1000, # One neuron run
    random_state=42
)

print(model)

print("Train the model: ")

model.fit(X_train_scaled,Y_train)

print("Model training completed")

# -------------------------------------------------------------
# Step 7 - Model evaluation
# -------------------------------------------------------------

print("-------------------------------")
print("Step 7 - Model evaluation")
print("-------------------------------")

Y_pred = model.predict(X_test_scaled)

accuracy = accuracy_score(Y_test,Y_pred)

print("Accuracy is: ", accuracy)

cm = confusion_matrix(Y_test, Y_pred)

print("\nConfusion matrix: ", cm)

print("\nPredict the probablity: ")

Y_prob = model.predict_proba(X_test_scaled)

print(Y_prob[:5])

# -------------------------------------------------------------
# Step 9 - Model preserve
# -------------------------------------------------------------

print("-------------------------------")
print("Step 9 - Model preserve")
print("-------------------------------")

joblib.dump(model, "placement_fnn_model.pkl")
joblib.dump(scalar, "placement_scaler.pkl") # .pkl = Pickle File

print("\nModel & Scalar gets dump succesfully\n")

# -------------------------------------------------------------
# Step 10 - Model loading and preserve
# -------------------------------------------------------------

print("-------------------------------")
print("Step 10 - Model loading & preserve")
print("-------------------------------")

loaded_model = joblib.load("placement_fnn_model.pkl")
loaded_scalar = joblib.load("placement_scaler.pkl")

print("\nModel gets loaded succesfully\n")

# -------------------------------------------------------------
# Step 11 - Test unseen data
    # Aptitude      : 70
    # Coding        : 75
    # Communication : 80
    # Acadamics     : 85
    # Internship    : 1
# -------------------------------------------------------------

print("-------------------------------")
print("Step 11 - Test unseen data")
print("-------------------------------")

new_student = pd.DataFrame([[70, 75, 80, 85, 1]], columns=['Aptitude', 'Coding', 'Communication', 'Academics', 'Internship'])

new_student_scaled = loaded_scalar.transform(new_student)

new_prediction = loaded_model.predict(new_student_scaled)

new_probablity = loaded_model.predict_proba(new_student_scaled)

print("New students data: ")
print(new_student)

print("\nPrediction probability: ", new_probablity)

if new_prediction[0] == 1:
    print("\nPrediction is: Placed\n")
else:
    print("\nPrediction is: Not Placed\n")