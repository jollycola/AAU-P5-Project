from .CONSTANTS import *

from numpy import array

DPP = (FOV / IMAGE_WIDTH)

def __calculateObjectCenter(coords: array):
    return ((coords[0] + coords[1]))/2
#END


def calculateDirection(coords: array):
    return DPP * (__calculateObjectCenter(coords)[0] - IMAGE_WIDTH/2)
# END
