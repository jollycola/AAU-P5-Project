import math

from .CONSTANTS import (FOCAL_LENGTH, OBJECT_REAL_HEIGHT, IMAGE_HEIGHT, SENSOR_HEIGHT)


def calculate_distance(coords):
    """
    Calculate the distance from the camera to the object defined by the bounding box

    Parameters:
    coords (array): The coordinates of the bounding box, as an array of int arrays

    Returns:
    int: The distance from the camera to the object

    """

    object_pixel_height = __calculate_pixel_height(coords)

    return (FOCAL_LENGTH * OBJECT_REAL_HEIGHT * IMAGE_HEIGHT) / \
        (object_pixel_height * SENSOR_HEIGHT)
# END


def __calculate_pixel_height(coords):
    height1 = math.sqrt(
        math.pow((coords[0][0] - coords[2][0]), 2) + math.pow((coords[0][1] - coords[2][1]), 2))

    height2 = math.sqrt(
        math.pow((coords[1][0] - coords[3][0]), 2) + math.pow((coords[1][1] - coords[3][1]), 2))

    return (height1 + height2) / 2.0
# END
