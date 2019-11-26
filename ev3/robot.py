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
DIRECTION_MOTOR = Motor(Port.D, Direction.CLOCKWISE)

TOUCH_BUTTON = TouchSensor(Port.S4)

SWING_MOTORS = [SWING_MOTOR, SWING_MOTOR_1, SWING_MOTOR_2]


class Robot:

    def beep(self, frequency=700):
        brick.sound.beep(frequency)

    def calibrate_dir(self):
        ''' Calibrate direction motor '''
        # Run motors until stalled
        # DIRECTION_MOTOR.set_dc_settings(55, 0)

        # DIRECTION_MOTOR.run(-90)

        DIRECTION_MOTOR.dc(-50)

        wait(300)

        while not DIRECTION_MOTOR.speed() == 0:
            pass

        DIRECTION_MOTOR.stop(Stop.HOLD)

        DIRECTION_MOTOR.set_dc_settings(100, 0)

        # Reset to straight
        DIRECTION_MOTOR.run_angle(150, 148, Stop.HOLD, True)

        # Set motor angle to zero to make it easier to calculate target angles
        print("Angle before reset: %i" % DIRECTION_MOTOR.angle())
        DIRECTION_MOTOR.reset_angle(0)

        print("Angle reset: " + str(DIRECTION_MOTOR.angle()))

        # wait two seconds before swing calibration
        wait(2000)
        brick.sound.beep(700)
    # End

    def calibrate_swing(self):
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

    def ready_swing(self, angle: int):
        ''' Ready the swing arm to the specified angle '''

        # Adjust motors to hit angle
        for m in SWING_MOTORS:
            m.run_target(100, angle, Stop.HOLD, False)

        # Keep running until middle motor is in corecct position
        time = StopWatch()
        while abs(SWING_MOTOR.angle() - angle) > 2:
            for m in SWING_MOTORS:
                wait(10)
                m.track_target(angle)

            # Stop adjusting if stuck for more than 2 seconds
            if time.time() > 2000:
                print("Used more than 2 seconds adjusting, stopping at angle: %d" % abs(SWING_MOTOR.angle() - angle))
                break

        # Play confirm sound
        play_sound_in_background(SoundFile.CONFIRM, 50)

    # End

    def setDirection(self, direction):
        print("Setting direction to: " + str(direction))

        # while abs(DIRECTION_MOTOR.angle() - direction) < 1.5:
        #     DIRECTION_MOTOR.track_target(direction)
        #     wait(100)

        # DIRECTION_MOTOR.stop(Stop.HOLD)

        DIRECTION_MOTOR.run_target(30, direction, Stop.HOLD, True)
        wait(1000)

        print("Ready to shoot, angle: " + str(DIRECTION_MOTOR.angle()))
    # End

    def shoot(self, speed: int):
        dc = (float(speed) / 4000.0) * 100.0
        for m in SWING_MOTORS:
            m.dc(dc)
        # Thread(target=brick.sound.file, args=(SoundFile.KUNG_FU, 50)).start()

        brick.sound.beep()

        print("SHOOT")

        timer = StopWatch()
        timer.pause()
        timerActive = False

        while True:            

            if SWING_MOTOR.speed() == 0:
                timer.reset()
                timer.resume()
                timerActive = True

            while timerActive:
                if timer.time() >= 500:
                    print("Timer more than 500, speed: %f" % SWING_MOTOR.speed())
                    if SWING_MOTOR.speed() < 1 and SWING_MOTOR.speed() > -1:
                        timer.pause()
                        break
                    else:
                        timer.pause()
                        timerActive = False

            if timerActive:
                break

            # print("Speed: %i" % SWING_MOTOR.speed())
            # print("Angle: %i" % SWING_MOTOR.angle())

        for m in SWING_MOTORS:
            m.stop()
        wait(250)
    # End

    def __set_display(self, str):
        brick.display.clear()
        brick.display.text(str, (60, 50))

    def wait_for_power_select(self, power=0, steps=50):
        self.__set_display(str(power))

        while not TOUCH_BUTTON.pressed():
            if Button.LEFT in brick.buttons():
                power -= steps
                if power < 0:
                    power = 0
                self.__set_display(str(power))

            elif Button.RIGHT in brick.buttons():
                power += steps
                if power > 4000:
                    power = 4000
                self.__set_display(str(power))

            wait(100)

        return power
    # End


    def wait_for_button(self):
        while not TOUCH_BUTTON.pressed():
            pass
    # End
