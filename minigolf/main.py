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
swingMotor      = Motor(Port.B, Direction.COUNTERCLOCKWISE, [3, 1])
swingMotor1     = Motor(Port.A, Direction.COUNTERCLOCKWISE, [3, 1])
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

# Motor input
angle = 90
shootSpeed = 1000

# Zero
def calibrate():
    # Run motors until stalled
    for m in swingMotors: 
        m.run(-500)

    ## Wait until motors are stalled
    while not swingMotor.stalled():
        pass

    # Motors will "overtighten", so run them forward a bit
    for m in swingMotors:
        m.run_angle(100, 30, Stop.HOLD, False)
        
    ## Give motors 1 second to adjust 
    wait(1000)

    # Set motor angle to zero to make it easier to calculate target angles 
    for m in swingMotors: 
        m.reset_angle(0)
    
    brick.sound.beep(700)
# End

def ready(angle: int):
    # Adjust motors to hit angle
    for m in swingMotors:
        m.run_target(100, angle, Stop.HOLD, False)

    # Keep running until middle motor is in corecct position
    while abs(swingMotor.angle() - angle) > 1:
        for m in swingMotors: m.track_target(angle)

    # Start new thread to play sound
    Thread(target=brick.sound.file, args=(SoundFile.CONFIRM, 50)).start()

    # Wait for button press
    while not button.pressed():
        for m in swingMotors: m.track_target(angle)

# End

def shoot(speed: int):
    for m in swingMotors: m.run(speed)
    Thread(target=brick.sound.file, args=(SoundFile.KUNG_FU, 50)).start()

    while not swingMotor.stalled():
        pass

    for m in swingMotors: m.stop()
    wait(250)
# End


# MAIN LOOP
while True:
    calibrate()

    ready(angle)

    shoot(shootSpeed)


# Wrapup
f.close()