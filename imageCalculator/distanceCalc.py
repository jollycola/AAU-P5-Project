from CONSTANTS import *
import sys

def calculateDistance(objectPixelHeight: float):
    return (FOCAL_LENGTH * OBJECT_REAL_HEIGHT * IMAGE_HEIGHT) / \
                    (objectPixelHeight * SENSOR_HEIGHT)
# END


if (len(sys.argv) == 2):
    objectPixelHeight = float(sys.argv[1])
    print(calculateDistance(objectPixelHeight))

else:
    exit("Error: Number of arguments must be exactly 1")