'''Main Raspberry Pi Program'''
import os
import camera.camera as camera
import imagecal.distance_calc as distCalc
import imagecal.direction_calc as dirCalc
from communication.client import Client
from model import Model
from colorRecognition.colorRecognition import (boundingBoxFinder)


def main():
    ''' Run the computer vision program '''
    
    mi_model = Model("minigolfmodel")
    mi_model.load_model()

    connection = Client("10.42.0.3")
    connection.connect_to_server()

    while True:
        connection.wait_for_string("READY")
        print("Received READY message")

        # Take image
        try:
            image_path = camera.take_picture("image.jpg")
            image_path = os.path.dirname(os.path.abspath(__file__)) + "/" + image_path
        except AssertionError:
            print("Camera only works on the pi, using sample image")
            image_path = os.path.dirname(os.path.abspath(__file__)) + "\\test\\sample.jpg"

        # Use openCV to find bounding box
        coords = boundingBoxFinder(image_path)
        
        # coords = [[1215, 1363], [1261, 1363], [1215, 1750], [1263, 1749]]

        # Calculate distance from bounding box
        distance = (distCalc.calculate_distance(coords) / 10)

        # Calculate direction from bounding box
        direction = dirCalc.calculate_direction(coords)

        # Send calculated dist and dir to connected PC
        print("Done!")
        print("Distance: %i " % distance)
        print("Direction: %f " % direction)
        print("Predicting...")
        power, swing = mi_model.predict_one(distance)
        print("Power: %f" % power)
        print("Swing: %f" % swing)  
        
        connection.send_data_to_server("%.2f,%d,%i" % (direction, power, swing))

if __name__ == "__main__":
    main()
