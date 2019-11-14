#!/usr/bin/env pybricks-micropython
from robot import Robot
from connection.server import Server

connection = Server("10.42.0.3", 1234)
connection.start_server()

# Wait for connection from a client
connection.wait_for_connection()

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
