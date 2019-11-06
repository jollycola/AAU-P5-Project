#!/usr/bin/env pybricks-micropython
import socket
import sys

from pybricks import ev3brick as brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import (Port, Stop, Direction, Button, Color,
                                 SoundFile, ImageFile, Align)
from pybricks.tools import print, wait, StopWatch
from pybricks.robotics import DriveBase

# Write your program here
brick.sound.beep()



sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_address = ('10.42.0.3', 4269)
print("Starting server on '%s:%s'" % server_address)
sock.bind(server_address)

sock.listen(5)

try:
    while True:
        connection, client_address = sock.accept()

        try:
            print("Connection from ", client_address)

            while True:
                data = connection.recv(16)
                print("Received %s" % data.decode())

                if data:
                    print("Sending data back")
                    connection.send(data)
                else:
                    print("No more data")
                    break
        finally:
            connection.close()
finally:
    sock.close()
