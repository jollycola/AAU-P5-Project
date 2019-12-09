import tensorflow as tf

import keras
from keras.models import Sequential
from keras.layers import Dense

import numpy as np
import pandas as pd

import sklearn

from sklearn.model_selection import train_test_split

def get_data():
    data = pd.read_excel('training_data.xlsx')
    return data

# Normalizing data_sheet
def normalize_data(data):
    data_sheet[data] = data_sheet[data]/data_sheet[data].max() 
    return data_sheet

def build_model():
    model = Sequential()
    model.add(Dense(64, input_dim=1, activation= "relu"))
    model.add(Dense(64, activation= "relu"))
    model.add(Dense(2))

    optimizer = tf.keras.optimizers.RMSprop(0.001)

    model.compile(loss='mae',
                optimizer=optimizer,
                metrics=['mae', 'mse'])
    return model

target_columns = ['POWER', 'SWING']
removed_columns = ['POWER', 'SWING', 'HIT']

data_sheet = get_data()

# Data_sheet we work with to predict
input_data_sheet = list(set(list(data_sheet.columns))-set(removed_columns))

# Normalizing Data
X = normalize_data(input_data_sheet)[input_data_sheet].values
y = normalize_data(input_data_sheet)[target_columns].values

# Splitting into training and testing set
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20)

model = build_model()
model.fit(X_train, y_train, epochs=100) 
prediction = model.predict([30])
print(np.sqrt(prediction))