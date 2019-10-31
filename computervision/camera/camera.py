import os
import sys

# raspistill is the camera command on the Raspberry Pi
# -vf -hf rotates the image 180 degrees
# -o specifies the output
CAMERA_COMMAND = "raspistill -vf -hf -o "

def take_picture(path: str):
    """
    Take a picture on the Raspberry Pi and save it at the specified path

    Parameters:
    path (str): The path where to save the picture

    Returns
    string: Returns the path
    """

    # Make sure that we are on Linux, this is to avoid this running on windows
    assert('linux' in sys.platform), "This code only runs on linux"

    print("Taking picture...")
    os.system(CAMERA_COMMAND + path)
    print("Picture taken: '" + path + "'")

    return path

# END
