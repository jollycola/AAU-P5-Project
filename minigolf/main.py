#!/usr/bin/env pybricks-micropython

from threading import Thread
from pybricks import ev3brick as brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import (Port, Stop, Direction, Button, Color,
                                 SoundFile, ImageFile, Align)
from pybricks.tools import print as pyPrint, wait, StopWatch
from pybricks.robotics import DriveBase

import util
import time

# Devices
swingMotor      = Motor(Port.A, Direction.COUNTERCLOCKWISE, [3, 1])
swingMotor1     = Motor(Port.B, Direction.COUNTERCLOCKWISE, [3, 1])
swingMotor2     = Motor(Port.C, Direction.COUNTERCLOCKWISE, [3, 1])
directionMotor  = Motor(Port.D)

button = TouchSensor(Port.S1)

swingMotors = [swingMotor, swingMotor1, swingMotor2]

# Motor Setup

swingMotor.reset_angle(0)
swingMotor1.reset_angle(0)
swingMotor2.reset_angle(0)
brick.sound.beep()

print("First angle %i" % swingMotor.angle())

pressed = False

def justPressed():
    global pressed
    if button.pressed():
        if not pressed:
            pressed = True
            return True
    else:
        pressed = False

    return False

# Motor actions
angle = 0

f = open("output.csv", "w")

while True:
    for m in swingMotors: m.track_target(angle)
    # pyPrint(swingMotor.angle()) 

    wait(1000)
    print(angle, swingMotor.angle(), sep=",", end='\n', file=f)
    pyPrint("Angle: %i" % angle)
    angle -= 1

    if Button.CENTER in brick.buttons():
        Thread(target=brick.sound.file, args=(SoundFile.KUNG_FU, 50)).start()
        for m in swingMotors: m.run(4000)
        break

    if (angle == -180):
        Thread(target=brick.sound.file, args=(SoundFile.FANFARE, 30)).start()
        break


f.close()

#brick.sound.beep(700, 200)
wait(1000)
for m in swingMotors: m.run_angle(200, 0, Stop.HOLD, False)
wait(1000)
print("Stopping, angle is: %i" % swingMotor.angle())
brick.sound.beep(200, 100)