from .CONSTANTS import *

from numpy import array


def __calculateObjectCenter(coords: array):
    return ((coords[0] + coords[1]))/2
#END

def calculateDirection(coords: array):
    return (FOV / IMAGE_WIDTH) * __calculateObjectCenter(coords)[0]
# END
