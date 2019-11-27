import os
from colorRecognition import colorRecognition as cr


def main():

    f = open("test.csv", "w+")

    for file in os.listdir(".\\sample"):
        coords = cr.boundingBoxFinder(os.path.join(".\\sample", file))
        f.write("%i:%i;%i:%i;%i:%i;%i:%i\n" % (coords[0][0], coords[0][1], coords[1][0], coords[1][1], coords[2][0], coords[2][1], coords[3][0], coords[3][1]))

    f.close()


if __name__ == "__main__":
    main()