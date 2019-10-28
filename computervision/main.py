import os


imagePath = "image.jpg"
cameraCommand = "raspistill -o " + imagePath

print("Taking picture")
os.system(cameraCommand)
print("Picture taken: '" + imagePath + "'")