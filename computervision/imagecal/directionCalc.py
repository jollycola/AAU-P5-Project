from .CONSTANTS import *

from numpy import array


def __calculateObjectCenter(coords):
    return ((coords[0] + coords[1]))/2
#END

def calculateDirection(coords):
    return (FOV / IMAGE_WIDTH) * __calculateObjectCenter(coords)[0]
# END
