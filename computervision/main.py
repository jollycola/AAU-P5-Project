import camera.camera as camera
import imagecal.distanceCalc as distCalc
import imagecal.directionCalc as dirCalc

from numpy import array

# Take image
try:
    imagePath = camera.takePicture("image.jpg")
except AssertionError:
    print("Camera only works on the pi, using sample image")
    imagePath = "test/sampleImage.jpg"

# Use openCV to find bounding box
coords = (array([1215, 1363]), array([1261, 1363]), array([1215, 1750]), array([1263, 1749])) 

# Calculate distance from bounding box
distance = distCalc.calculateDistance(coords)

# Calculate direction from bounding box
direction = dirCalc.calculateDirection(coords)

# Send calculated dist and dir to connected PC
print("Done!")
print("Distance: %i " % distance)
print("Direction: %i " % direction)