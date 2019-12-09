
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import sklearn

from sklearn.model_selection import train_test_split
#from sklearn.metrics import mean_squared_error
#from math import sqrt

# Open data_sheet
data_sheet = pd.read_excel('training-set.xlsx')

target_columns = ['POWER', 'SWING']
removed_columns = ['STROKE']

# Data_sheet we work with to predict
input_data_sheet = list(set(list(data_sheet.columns))-set(removed_columns))

# Normalizing data_sheet
# data_sheet[input_data_sheet] = data_sheet[input_data_sheet]/data_sheet[input_data_sheet].max() 

X = data_sheet[input_data_sheet].values
Y = data_sheet[target_columns].values

x_train, x_test, y_train, y_test = train_test_split(X, Y, test_size=0.30, random_state=40)

# Building model
model = Sequential()
model.add(Dense(500, input_dim=1, activation= "relu"))
model.add(Dense(100, activation= "relu"))
model.add(Dense(50, activation= "relu"))
model.add(Dense(2))

model.compile(loss= "mean_squared_error" , optimizer="adam", metrics=["mean_squared_error"])

# Training for K-epochs
model.fit(x_train, y_train, epochs=50)
model.save('minigolf-network.model')