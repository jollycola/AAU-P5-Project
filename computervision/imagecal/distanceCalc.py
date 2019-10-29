from .CONSTANTS import *

import sys
import math
from numpy import array

def calculateDistance(coords):

    objectPixelHeight = __calculatePixelHeight(coords)

    return (FOCAL_LENGTH * OBJECT_REAL_HEIGHT * IMAGE_HEIGHT) / \
                    (objectPixelHeight * SENSOR_HEIGHT)
# END


def __calculatePixelHeight(coords):
    height1 = math.sqrt(
        math.pow((coords[0][0] - coords[2][0]), 2) + 
        math.pow((coords[0][1] - coords[2][1]), 2))
        
    height2 = math.sqrt(
        math.pow((coords[1][0] - coords[3][0]), 2) + 
        math.pow((coords[1][1] - coords[3][1]), 2))

    return (height1 + height2) / 2.0
# END    