from tensorflow import keras

class Model:

    def __init__(self, path):
        self.model_path = path

    def load_model(self):
        self.model = keras.models.load_model(self.model_path)

    def predict_one(self, distance):
        result = self.model.predict([distance])
        power = round(result[0][0] * 100)
        distance = round(result[0][1])


        return (power, distance)

