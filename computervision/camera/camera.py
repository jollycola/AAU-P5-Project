import os
import sys

cameraCommand = "raspistill -o "

def takePicture(path: str): 
    
    assert('linux' in sys.platform), "This code only runs on linux"

    print("Taking picture...")
    os.system(cameraCommand)
    print("Picture taken: '" + path + "'")

    return path

# END