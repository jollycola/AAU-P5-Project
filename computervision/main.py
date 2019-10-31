import os

import camera.camera as camera
import imagecal.distance_calc as distCalc
import imagecal.direction_calc as dirCalc
from colorRecognition.colorRecognition import boundingBoxFinder


def main():
    ''' Run the computer vision program '''

    # Take image
    try:
        image_path = camera.takePicture("image.jpg")
        image_path = os.path.dirname(os.path.abspath(__file__)) + "/" + image_path
    except AssertionError:
        print("Camera only works on the pi, using sample image")
        image_path = os.path.dirname(os.path.abspath(__file__)) + "\\test\\sample.jpg"

    # Use openCV to find bounding box
    # coords = (array([1215, 1363]), array([1261, 1363]), array([1215, 1750]), array([1263, 1749])) 
    try:
        coords = boundingBoxFinder(image_path)
    except Exception as err:
        exit(err)
    
    # Calculate distance from bounding box
    distance = distCalc.calculate_distance(coords)

    # Calculate direction from bounding box
    direction = dirCalc.calculate_direction(coords)

    # Send calculated dist and dir to connected PC
    print("Done!")
    print("Distance: %i " % distance)
    print("Direction: %i " % direction)


if __name__ == "__main__":
    main()
