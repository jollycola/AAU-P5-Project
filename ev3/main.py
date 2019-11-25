#!/usr/bin/env pybricks-micropython
from robot import Robot
from communication.server import Server

from pybricks.tools import (print, wait, StopWatch)

robot = Robot()

try:
    connection = Server("10.42.0.3", 1234)
    connection.start_server()

    # Wait for connection from a client
    connection.wait_for_connection()
    robot.beep()

    robot.calibrate_swing()

    # MAIN LOOP
    while True:

        robot.wait_for_button()

        connection.send_data_to_client("READY")

        (direction, power, angle) = connection.wait_for_data()  # (0, 4000, 10)  # Accept data from raspi
        print(float(direction), ",", power, ",", angle)
        robot.setDirection(direction)

        robot.ready_swing(angle)

        robot.calibrate_dir()
        robot.setDirection(direction)
        robot.wait_for_button()

        robot.shoot(power)
except:
    connection.stop_server()


