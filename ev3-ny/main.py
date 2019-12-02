#!/usr/bin/env micropython
from robot import Robot


robot = Robot()
robot.calibrate_swing()
robot.ready_swing(60)

robot.calibrate_dir()
robot.set_direction(0)

robot.wait_for_button()
robot.shoot(2000)

