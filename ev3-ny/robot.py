import time
import ev3dev2.motor as ev3Motor
from ev3dev2.motor import Motor, OUTPUT_A, OUTPUT_B, OUTPUT_D, SpeedPercent, MoveTank, MediumMotor
from ev3dev2.sound import Sound


class Robot:

    def __init__(self):
        self.sound = Sound()
        self.direction_motor = MediumMotor(OUTPUT_D)

    def beep(self, frequency=700, wait_for_comeplete=False):
        play_type = Sound.PLAY_WAIT_FOR_COMPLETE if wait_for_comeplete else Sound.PLAY_NO_WAIT_FOR_COMPLETE
        self.sound.beep("-f %i" % frequency, play_type=play_type)


    def calibrate_dir(self):
        ''' Calibrate direction motor '''
        # Run motor with 25% power, and wait until it stops running
        self.direction_motor.on(SpeedPercent(-25), block=False)
        self.direction_motor.wait_until_not_moving()

        self.direction_motor.stop_action = Motor.STOP_ACTION_COAST
        self.direction_motor.stop()

        # Reset to straight
        self.direction_motor.on_for_degrees(SpeedPercent(50), 150, brake=True, block=True)
        self.direction_motor.reset()
        print("Motor reset, position: " + str(self.direction_motor.position))

        time.sleep(.5)
        self.beep()
