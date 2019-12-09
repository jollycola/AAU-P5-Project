from __future__ import absolute_import, division, print_function, unicode_literals

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

import tensorflow as tf

from tensorflow import keras
from tensorflow.keras import layers

import tensorflow_docs as tfdocs
import tensorflow_docs.plots
import tensorflow_docs.modeling

dataset = pd.read_excel('training-set.xlsx')

train_dataset = dataset.sample(frac=0.8, random_state=0)
test_dataset = dataset.drop(train_dataset.index)

train_stats = train_dataset.describe()
train_stats.pop("POWER")
train_stats = train_stats.transpose()


print(train_stats)

train_targets = train_dataset[['POWER', 'SWING']]
train_dataset.pop("POWER")
train_dataset.pop("SWING")

test_targets = test_dataset[['POWER', 'SWING']]
test_dataset.pop("POWER")
test_dataset.pop("SWING")

print("==========TRAIN DATASET==========\n")
print(train_dataset)

def build_model():
    model = keras.Sequential([
        layers.Dense(16, activation='sigmoid', input_shape=[1]),
        layers.Dense(2)
    ])

    model.compile(loss='mse',
                    optimizer='adam',
                    metrics=['mse'])

    return model


model = build_model()

EPOCHS = 1000

history = model.fit(
    train_dataset, train_targets,
    epochs=EPOCHS, validation_split=0.2, verbose=0,
    callbacks=[tfdocs.modeling.EpochDots()]
)

print(model.predict([20]))

model.save("model.model")


# test_predictions = model.predict(test_dataset).flatten()

test_predictions = model.predict(dataset['DIST'])


dataset = pd.read_excel('training-set.xlsx')

test_predictions = model.predict(dataset['DIST'])

print(model.predict([50]))

plt.xlabel('Distance')
plt.ylabel('Power')
plt.xlim([0, 200])
plt.ylim([0, 1])
_ = plt.plot(dataset[['DIST']].values, test_predictions[:,1])

plt.show()

