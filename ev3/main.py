#!/usr/bin/env pybricks-micropython
from robot import Robot

from pybricks.tools import (print, wait, StopWatch)

robot = Robot()

robot.calibrate_swing()

# MAIN LOOP
while True:

    

    power = robot.wait_for_power_select(2000)
    angle = 0
    direction = 0

    print(float(direction), ",", power, ",", angle)
    robot.setDirection(direction)

    robot.ready_swing(angle)

    robot.calibrate_dir()
    robot.setDirection(direction)

    robot.wait_for_button()
    robot.shoot(power)


