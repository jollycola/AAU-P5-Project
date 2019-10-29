import camera.camera as camera
import imagecal.distanceCalc as distCalc
import imagecal.directionCalc as dirCalc
from colorRecognition.colorRecognition import boundingBoxFinder

import os

from numpy import array

def main():
    # Take image
    try:
        image_path = camera.takePicture("image.jpg")
    except AssertionError:
        print("Camera only works on the pi, using sample image")
        image_path = os.path.dirname(os.path.abspath(__file__)) + "\\test\\sample.jpg"

    # Use openCV to find bounding box
    # coords = (array([1215, 1363]), array([1261, 1363]), array([1215, 1750]), array([1263, 1749])) 
    coords = boundingBoxFinder(image_path)

    # Calculate distance from bounding box
    distance = distCalc.calculateDistance(coords)

    # Calculate direction from bounding box
    direction = dirCalc.calculateDirection(coords)

    # Send calculated dist and dir to connected PC
    print("Done!")
    print("Distance: %i " % distance)
    print("Direction: %i " % direction)


if __name__ == "__main__":
    main()
