from numpy import array

from .constants import (FOV, IMAGE_WIDTH)

DPP = float(FOV / IMAGE_WIDTH)

def __calculate_object_center(coords: array):
    return (coords[0] + coords[1]) / 2

def calculate_direction(coords: array):
    """ Calculates the direction in angles from the center of the image,
    to the center of the object defined by the bounding box.

    Parameters:
    coords (array): The coordinates of the bounding box, as an array of int arrays

    Returns:
    int: The angle from the center of the photo to the center of the object

    """
    # converts any array_like into a numpy array
    _coords = array(coords)

    return DPP * (__calculate_object_center(_coords)[0] - (IMAGE_WIDTH / 2))
