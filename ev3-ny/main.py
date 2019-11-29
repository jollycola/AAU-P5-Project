#!/usr/bin/env python3
from ev3dev2.sensor import INPUT_1
from ev3dev2.sensor.lego import TouchSensor
from ev3dev2.led import Led
from ev3dev2.sound import Sound
from ev3dev2.motor import Motor, OUTPUT_A, OUTPUT_B, OUTPUT_D, SpeedPercent, MoveTank, MediumMotor


motor = Motor(OUTPUT_A)
speed = 20
motor.run_timed(time_sp=1000)


while True:
    pass
