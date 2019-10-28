from CONSTANTS import *
import sys

def calculateDirection(objectPixelCoordinate: float):
    pass
# END


if (len(sys.argv) == 2):
    objectPixelHeight = float(sys.argv[1])
    print(calculateDirection(objectPixelCoordinate))

else:
    exit("Error: Number of arguments must be exactly 1")