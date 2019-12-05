#!/usr/bin/env micropython
from robot import Robot
from server import Server


robot = Robot()
power = 1

robot.beep()

connection_enabled = robot.select_connection_mode()

if connection_enabled:
    server = Server("10.42.0.13", 1234)
    server.start_server()

    server.wait_for_connection()


while True:
    if connection_enabled:
        robot.print("Press to take picture")
        #Send message to pi
        (direction, power, angle) = server.wait_for_data
    else:
        power = robot.wait_for_power_select(power)
        angle = 0
        direction = 0

    robot.calibrate_swing()
    robot.ready_swing(angle)

    robot.calibrate_dir()
    robot.set_direction(direction)

    robot.wait_for_button()
    robot.shoot(power)

