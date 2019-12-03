#!/usr/bin/env micropython
from robot import Robot
from server import Server

robot = Robot()
power = 1

robot.beep()

# server = Server("10.42.0.13", 1234)
# server.start_server()

# server.wait_for_connection()

while True:
    power = robot.wait_for_power_select(power)

    robot.calibrate_swing()
    robot.ready_swing(0)

    robot.calibrate_dir()
    robot.set_direction(0)

    robot.wait_for_button()
    robot.shoot(power)

