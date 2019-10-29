focalLength = 3.04
objectRealHeight = 100
imageHeight = 2464
objectPixelHeight = 1
sensorHeight = 2.76

def calculateResult():
    result = (focalLength*objectRealHeight*imageHeight)/(objectPixelHeight*sensorHeight)
    print("Distance to object is %d" %result)
    print("Enter actual distance to calculate deviance or press enter to return to main manu")
    choice = input()
    if isinstance(choice, float) or isinstance(choice, int):
        calculateDeviance(result, choice)

def calculateDeviance(actual, expected):
    result = ((expected - actual) / actual) * 100
    print("Deviance is %f %%" %result)

def changeVar(varToChange, varName):
    print("Enter value to change %s" %varName)
    oldValue = varToChange
    newValue = input()
    varToChange = newValue
    print("Set %s to %s from %s" % (varName, varToChange, oldValue))
    return varToChange

##"Main" starts here##
choice = ""

while choice != 6:
    print("""Select a variable to change value or choose to calculate: \n
        0. Calculate result\n
        1. Focal length: %f\n
        2. Object real height: %f\n
        3. Image height: %f\n
        4. Object pixel height: %f\n
        5. Sensor height: %f\n
        6. Exit\n
        All real-world measurements should be in mm
        """ % (focalLength, objectRealHeight, imageHeight, objectPixelHeight, sensorHeight)) 
    tempCheck = input()
    if tempCheck is None:
        print("test")
    else:
        choice = int(tempCheck)

        if choice > 6 or choice < 0:
            print("Wrong range for choice") 
        else:
            if choice == 0:
                calculateResult()
            elif choice == 1:
                focalLength = changeVar(focalLength, "Focal length")
            elif choice == 2:
                objectRealHeight = changeVar(objectRealHeight, "Object real height")
            elif choice == 3:
                imageHeight = changeVar(imageHeight, "Image height")
            elif choice == 4:
                objectPixelHeight = changeVar(objectPixelHeight, "Object pixel height")
            elif choice == 5:
                sensorHeight = changeVar(sensorHeight, "Sensor height")
