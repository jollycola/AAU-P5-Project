from model import Model
import numpy as np

my_model = Model("minigolfmodel")
my_model.load_model()

power, swing = my_model.predict_one(100)

print("Power: %f\nSwing: %f" % (power, swing))
