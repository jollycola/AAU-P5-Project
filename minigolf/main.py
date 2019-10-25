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

# Setup
swingMotor      = Motor(Port.A, Direction.COUNTERCLOCKWISE, [3, 1])
swingMotor1     = Motor(Port.B, Direction.COUNTERCLOCKWISE, [3, 1])
swingMotor2     = Motor(Port.C, Direction.COUNTERCLOCKWISE, [3, 1])
directionMotor  = Motor(Port.D)

button = TouchSensor(Port.S4)

swingMotors = [swingMotor, swingMotor1, swingMotor2]
f = open("output.csv", "w")


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
angle = 60
shootSpeed = 1000


while True:

    for m in swingMotors: 
        m.run(-100)

    wait(1000)
    while not swingMotor.stalled():
        pass

    brick.sound.beep()
    for m in swingMotors:
        m.run_angle(100, 30, Stop.HOLD, False)

    wait(1000)
    brick.sound.beep()

    for m in swingMotors: 
        m.reset_angle(0)
        m.stop(Stop.HOLD)
    wait(1500)

    for m in swingMotors:
        m.run_target(30, angle, Stop.HOLD, False)

    while abs(swingMotor.angle() - angle) > 1:
        pass

    for m in swingMotors: m.stop(Stop.HOLD)

    brick.sound.file(SoundFile.CONFIRM)

    while not button.pressed():
        for m in swingMotors: m.track_target(angle)

    for m in swingMotors: m.run(shootSpeed)
    Thread(target=brick.sound.file, args=(SoundFile.KUNG_FU, 50)).start()

    wait(1000)

pyPrint(swingMotor.angle())

f.close()