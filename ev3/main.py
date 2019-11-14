#!/usr/bin/env pybricks-micropython
from robot import Robot

robot = Robot()
robot.calibrate_dir()
robot.calibrate_swing()

# MAIN LOOP
while True:

    robot.wait_for_button()

    (direction, power, angle) = (0, 4000, 10)  # Accept data from raspi

    robot.setDirection(direction)

    robot.ready_swing(angle)

    robot.wait_for_button()

    robot.shoot(power)
