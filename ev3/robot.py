#!/usr/bin/env pybricks-micropython
from threading import Thread
import socket

from pybricks import ev3brick as brick

from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import (Port, Stop, Direction, Button, Color,
                                 SoundFile, ImageFile, Align)
from pybricks.tools import (print, wait, StopWatch)
from pybricks.robotics import DriveBase

from my_util import (play_sound_in_background)

# Setup
SWING_MOTOR = Motor(Port.B, Direction.COUNTERCLOCKWISE, [3, 1])
SWING_MOTOR_1 = Motor(Port.A, Direction.COUNTERCLOCKWISE, [3, 1])
SWING_MOTOR_2 = Motor(Port.C, Direction.COUNTERCLOCKWISE, [3, 1])
DIRECTION_MOTOR = Motor(Port.D, Direction.COUNTERCLOCKWISE, [1, 3])

TOUCH_BUTTON = TouchSensor(Port.S4)

SWING_MOTORS = [SWING_MOTOR, SWING_MOTOR_1, SWING_MOTOR_2]


class Robot:
    def calibrate_dir():
        ''' Calibrate direction motor '''
        # Run motors until stalled
        DIRECTION_MOTOR.set_dc_settings(30, 0)

        DIRECTION_MOTOR.run(30)

        while not DIRECTION_MOTOR.stalled():
            pass

        DIRECTION_MOTOR.stop(Stop.HOLD)

        DIRECTION_MOTOR.set_dc_settings(100, 0)

        # Reset to straight
        DIRECTION_MOTOR.run_angle(30, -54, Stop.COAST, True)

        # Set motor angle to zero to make it easier to calculate target angles
        DIRECTION_MOTOR.reset_angle(0)

        # wait two seconds before swing calibration
        wait(2000)
        brick.sound.beep(700)
    # End

    def calibrate_swing():
        ''' Calibrate swing motors '''
        # Run motors until stalled
        for m in SWING_MOTORS:
            m.run(-500)

        while not SWING_MOTOR.stalled():
            pass

        # Motors will "overtighten", so run them forward a bit
        for m in SWING_MOTORS:
            m.run_angle(100, 30, Stop.HOLD, False)

        # Give motors 1 second to adjust
        wait(1000)

        # Set motor angle to zero to make it easier to calculate target angles
        for m in SWING_MOTORS:
            m.reset_angle(0)

        brick.sound.beep(700)
    # End

    def ready_swing(angle: int):
        ''' Ready the swing arm to the specified angle '''

        # Adjust motors to hit angle
        for m in SWING_MOTORS:
            m.run_target(100, angle, Stop.HOLD, False)

        # Keep running until middle motor is in corecct position
        time = StopWatch()
        while abs(SWING_MOTOR.angle() - angle) > 2:
            for m in SWING_MOTORS:
                m.track_target(angle)

            # Stop adjusting if stuck for more than 2 seconds
            if time.time() > 2000:
                print("Used more than 2 seconds adjusting, stopping at angle: %d" % abs(SWING_MOTOR.angle() - angle))
                break

        # Play confirm sound
        play_sound_in_background(SoundFile.CONFIRM, 50)

        # Wait for button press
        while not TOUCH_BUTTON.pressed():
            for m in SWING_MOTORS:
                m.track_target(angle)
    # End

    def setDirection(direction: int):
        DIRECTION_MOTOR.run_angle(30, direction, Stop.HOLD, True)
        wait(2000)
    # End

    def shoot(speed: int):
        for m in SWING_MOTORS:
            m.run(speed)
        Thread(target=brick.sound.file, args=(SoundFile.KUNG_FU, 50)).start()

        while not SWING_MOTOR.stalled():
            pass

        for m in SWING_MOTORS:
            m.stop()
        wait(250)
    # End


    def wait_for_button():
        while not TOUCH_BUTTON.pressed():
            pass
    # End
