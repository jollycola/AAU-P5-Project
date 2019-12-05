#!/usr/bin/env micropython
from robot import Robot
from server import Server

PORT_RANGE = (1234, 1235, 1236, 1237, 1238)

robot = Robot()
power = 1

robot.beep()

connection_enabled = robot.select_connection_mode()

if connection_enabled:
    i = 0
    while True:
        try:
            server = Server("10.42.0.13", PORT_RANGE[i % len(PORT_RANGE)])
            server.start_server()
        except OSError:
            i += 1
            

    server.wait_for_connection()


while True:
    if connection_enabled:
        robot.print("Press to take picture")
        server.send_data_to_client("READY")
        (direction, power, angle) = server.wait_for_data()
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

    robot.wait_for_button()

