#!/usr/bin/env pybricks-micropython
from robot import Robot

from pybricks.tools import (print, wait, StopWatch)

robot = Robot()

robot.calibrate_swing()

power = 2000

# MAIN LOOP
while True:

    power = robot.wait_for_power_select(power)
    angle = 0
    direction = 0

    print(float(direction), ",", power, ",", angle)
    
    robot.ready_swing(angle)

    robot.calibrate_dir()
    print("Calibrated")
    robot.setDirection(direction)

    

    robot.wait_for_button()
    robot.shoot(power)


