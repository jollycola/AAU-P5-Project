import os
from colorRecognition import colorRecognition as cr


def main():
    run_single("4000 (2).JPG")

    # run_all()


def run_single(path):
    coords = cr.boundingBoxFinder(os.path.join("sample", path), True)
    print(coords)


def run_all():
    f = open("test.csv", "w+")

    for file in os.listdir(".\\sample"):
        coords = cr.boundingBoxFinder(os.path.join(".\\sample", file))
        f.write("%s;%i:%i;%i:%i;%i:%i;%i:%i\n" % (file, coords[0][0], coords[0][1], coords[1][0], coords[1][1], coords[2][0], coords[2][1], coords[3][0], coords[3][1]))

    f.close()


if __name__ == "__main__":
    main()