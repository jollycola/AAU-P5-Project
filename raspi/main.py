'''Main Raspberry Pi Program'''
import os

import camera.camera as camera
import imagecal.distance_calc as distCalc
import imagecal.direction_calc as dirCalc
from communication.client import Client

from colorRecognition.colorRecognition import (boundingBoxFinder)


def main():
    ''' Run the computer vision program '''

    connection = Client("10.42.0.3", 1234)
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

        # Calculate distance from bounding box
        distance = distCalc.calculate_distance(coords)

        # Calculate direction from bounding box
        direction = dirCalc.calculate_direction(coords)

        # Send calculated dist and dir to connected PC
        print("Done!")
        print("Distance: %i " % distance)
        print("Direction: %i " % direction)

        connection.send_data_to_server((direction, distance * 2, 10))


if __name__ == "__main__":
    main()
