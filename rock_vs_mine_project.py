# -*- coding: utf-8 -*-
"""Rock Vs Mine Project.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1q_M6TLTxq6c6O_dSat3S7zGhL3jTyMtg

Rock Vs Mine prediction
"""

#  importing libraries
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

"""Data Collection and Processing"""

sonar_data =pd.read_csv("/content/sonar data.csv", header = None)
sonar_data.head()

#number of rows and column
sonar_data.shape

sonar_data.describe()

sonar_data[60].value_counts()

sonar_data.groupby(60).mean()

"""Seperate data and labels"""

X = sonar_data.drop(columns = 60, axis = 1)
Y = sonar_data[60]

print(X, Y)

"""Spliting Data in Training and Test data"""

X_train, X_test, Y_train, Y_test =  train_test_split(X, Y, test_size = 0.1, stratify=Y, random_state=1)

print(X_train.shape, X_test.shape, X.shape)

"""Logistic Regression"""

#traininig logistic regresssion model
model = LogisticRegression()
model.fit(X_train, Y_train)

"""Model Evaluation"""

#accuracy from training data
X_train_prediction = model.predict(X_train)
training_data_accuracy = accuracy_score(X_train_prediction,Y_train)

print(training_data_accuracy)

#accuracy from test data
X_test_prediction = model.predict(X_test)
test_data_accuracy = accuracy_score(X_test_prediction,Y_test)

print(test_data_accuracy)

"""Making Prediction"""

input_data = (0.0286,0.0453,0.0277,0.0174,0.0384,0.0990,0.1201,0.1833,0.2105,0.3039,0.2988,0.4250,0.6343,0.8198,1.0000,0.9988,0.9508,0.9025,0.7234,0.5122,0.2074,0.3985,0.5890,0.2872,0.2043,0.5782,0.5389,0.3750,0.3411,0.5067,0.5580,0.4778,0.3299,0.2198,0.1407,0.2856,0.3807,0.4158,0.4054,0.3296,0.2707,0.2650,0.0723,0.1238,0.1192,0.1089,0.0623,0.0494,0.0264,0.0081,0.0104,0.0045,0.0014,0.0038,0.0013,0.0089,0.0057,0.0027,0.0051,0.0062)
#changing input data into numpy array

input_data_as_numpy = np.asarray(input_data)

#reshape the np
input_data_reshaped = input_data_as_numpy.reshape(1,-1)

prediction = model.predict(input_data_reshaped)
print(prediction)

if (prediction[0]== "R"):
  print("Its Rock")
else:
  print("Its a Mine")



