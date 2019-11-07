#!/usr/bin/env pybricks-micropython
from robot import Robot
from connection import Connection

connection = Connection("10.42.0.3", 69420)
connection.start_server()
connection.wait_for_connection()

robot = Robot()
robot.calibrate_dir()
robot.calibrate_swing()

# MAIN LOOP
while True:


    robot.wait_for_button()
    connection.send_data_to_client("READY")

    (direction, power, angle) = connection.wait_for_data()

    robot.setDirection(direction)

    robot.ready_swing(angle)

    robot.wait_for_button()

    robot.shoot(power)


connection.stop_server()
