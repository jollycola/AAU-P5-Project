import array as arr
import numpy as np 

import cv2


def boundingBoxFinder(path):
    # Path for pictures
    print("Path: " + path)

    # Reads the picture by path and converts the color system to HSV
    image = cv2.imread(path)
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    # HSV range for the color red
    lower_red = np.array([161, 155, 84])
    upper_red = np.array([179, 255, 255])

    # Mask after the HSV colors and contours 
    mask = cv2.inRange(hsv, lower_red, upper_red)
    contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    i = 0
    biggestBox = []
    biggestArea = 0


    # Finds the biggest bounding box
    for contour in contours:
        area = cv2.contourArea(contour)

        if(area > 800):
            x, y, w, h = cv2.boundingRect(contour)
            box = arr.array('f', [area, x, y, w, h])

            # Checks if the new area is the biggest are, and if the box has the same width, height ratio as the flag with some deviation.
            if(box[0] >= biggestArea and (((box[3] * 10) - box[2]) < 30) and (((box[3] * 10) - box[2]) > -30)): 
                biggestArea = box[0]       
                biggestBox = arr.array('f', [box[0], box[1], box[2], box[3], box[4]])

            i = i + 1

    # informs if no red box was found
    if (len(biggestBox) == 0):
        raise Exception("Error: No red objects found!")

    # Coords for the bounding box converts from float to integer
    firstCoord = np.array([int(biggestBox[1]), int(biggestBox[2])])
    secondCoord = np.array([int(biggestBox[1] + biggestBox[3]), int(biggestBox[2])])
    thirdCoord = np.array([int(biggestBox[1]), int(biggestBox[2] + biggestBox[4])])
    fourthCoord = np.array([int(biggestBox[1] + biggestBox[3]), int(biggestBox[2] + biggestBox[4])])

    # Coords inserted into a tuple
    coords = np.array([firstCoord, secondCoord, thirdCoord, fourthCoord])

    return coords
