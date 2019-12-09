import tensorflow as tf

import keras
from keras.models import Sequential
from keras.layers import Dense
from keras.utils import plot_model
import seaborn as sns

import numpy as np
import pandas as pd

import sklearn

from sklearn.model_selection import train_test_split

import matplotlib.pyplot as plt

# import os

# os.environ["PATH"] += os.pathsep + 'C:/Program Files (x86)/Graphviz2.38/bin/'

def get_data():
    data = pd.read_excel('training_data.xlsx')
    return data

# Normalizing data_sheet
def normalize_data(data):
    data_sheet[data] = data_sheet[data]/data_sheet[data].max() 
    return data_sheet

def build_model():
    model = Sequential()
    model.add(Dense(32, input_dim=1, activation= "sigmoid"))
    model.add(Dense(32, activation= "sigmoid"))
    model.add(Dense(1))

    optimizer = tf.keras.optimizers.RMSprop(0.001)

    model.compile(
                optimizer='adam',
                loss='mean_squared_error')
    return model

target_columns = ['POWER']
removed_columns = ['POWER']
input_columns = ['DIST']

data_sheet = get_data()

# Data_sheet we work with to predict
input_data_sheet = list( set(list(data_sheet.columns)) - set(removed_columns))

# Normalizing Data
# X = normalize_data(input_data_sheet)[input_data_sheet].values
# y = normalize_data(input_data_sheet)[target_columns].values

X = data_sheet[input_columns].values
Y = data_sheet[target_columns].values

print(X)

exit()

# Splitting into training and testing set
X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.20)

model = build_model()
model.fit(X_train, y_train, epochs=500, batch_size=32) 
prediction = model.predict([50])
print(prediction)
print(model.summary())

plot_model(model, to_file="model.png")

y_pred = model.predict(X)

y_test.sort()
y_pred.sort()

print(y_pred)

plt.plot(Y, color ='red', label="Real Data")
plt.plot(y_pred, color ='blue', label="Predicted Data")
plt.title("Prediction")
plt.legend()
plt.show()