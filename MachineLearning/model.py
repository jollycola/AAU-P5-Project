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

model = keras.models.load_model('model.model')

dataset = pd.read_excel('training-set.xlsx')

test_predictions = model.predict(dataset['DIST'])

print(model.predict([50]))

plt.xlabel('Distance')
plt.ylabel('Power')
plt.xlim([0, 200])
plt.ylim([0, 1])
_ = plt.plot(dataset[['DIST']].values, test_predictions[:,1])

plt.show()
