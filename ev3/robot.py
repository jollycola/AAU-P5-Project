import time
import ev3dev2.motor as ev3Motor
from ev3dev2.motor import Motor, OUTPUT_A, OUTPUT_B, OUTPUT_C, OUTPUT_D, SpeedPercent, MoveTank, MediumMotor, MotorSet, LargeMotor, SpeedDPS
from ev3dev2.sound import Sound
from ev3dev2.sensor.lego import TouchSensor
from ev3dev2.sensor import INPUT_1
from ev3dev2.console import Console
from ev3dev2.button import Button

# https://python-ev3dev.readthedocs.io/en/ev3dev-stretch/#library-documentation

DEFAULT_FONT = "Lat15-TerminusBold22x11.psf.gz"
LARGER_FONT = "Lat15-TerminusBold16.psf.gz"

class Robot:

    def __init__(self):
        self.sound = Sound()
        self.direction_motor = MediumMotor(OUTPUT_D)
        self.swing_motorL = LargeMotor(OUTPUT_A)
        self.swing_motorC = LargeMotor(OUTPUT_B)
        self.swing_motorR = LargeMotor(OUTPUT_C)
        self.swing_motors = [self.swing_motorL, self.swing_motorC, self.swing_motorR]
        self.touch_sensor = TouchSensor(INPUT_1)
        self.console = Console(DEFAULT_FONT)
        self.buttons = Button()
        self.beeps_enabled = True

    def beep(self, frequency=700, wait_for_comeplete=False):
        if not self.beeps_enabled:
            return
        play_type = Sound.PLAY_WAIT_FOR_COMPLETE if wait_for_comeplete else Sound.PLAY_NO_WAIT_FOR_COMPLETE
        self.sound.beep("-f %i" % frequency, play_type=play_type)

    def disable_beeps(self):
        self.beeps_enabled = False

    def enable_beeps(self):
        self.beeps_enabled = True

    def is_beeps_enabled(self):
        return self.beeps_enabled

    def calibrate_dir(self):
        ''' Calibrate direction motor '''
        # Run motor with 25% power, and wait until it stops running
        self.direction_motor.on(SpeedPercent(-10), block=False)
        # while (not self.direction_motor.STATE_OVERLOADED):
        #     print(self.direction_motor.duty_cycle)
        self.direction_motor.wait_until(self.direction_motor.STATE_OVERLOADED) 

        self.direction_motor.stop_action = Motor.STOP_ACTION_COAST
        self.direction_motor.stop()

        time.sleep(.5)

        # Reset to straight
        # self.direction_motor.on_for_seconds(SpeedPercent(10), .835, brake=True, block=True)
        self.direction_motor.on_for_degrees(SpeedPercent(10), 127, brake=True, block=True)
        self.direction_motor.reset()

        print("Motor reset, position: " + str(self.direction_motor.position))

        time.sleep(.5)

    def calibrate_swing(self):
        for m in self.swing_motors:
            m.stop_action = m.STOP_ACTION_HOLD
            m.on(SpeedPercent(6))
           
        self.swing_motorC.wait_until(self.swing_motorC.STATE_OVERLOADED, 2000)

        for m in self.swing_motors:
            m.stop_action = m.STOP_ACTION_HOLD
            m.on_for_degrees(SpeedPercent(5), -15, brake=True, block=False)

        self.swing_motorC.wait_while('running')

        for m in self.swing_motors:
            m.reset()
            m.stop_action = m.STOP_ACTION_HOLD
            m.stop()
        
        print("Ready Angle: %i" % self.swing_motorC.position)
        

    def ready_swing(self, angle: int):
        right_angle = -(angle / 3)
        # adjust motors to target angle
        for m in self.swing_motors:       
            m.stop_action = Motor.STOP_ACTION_HOLD    
            m.on_for_degrees(SpeedPercent(2), right_angle, brake=True, block=False)
            
        self.swing_motorC.wait_while('running')

        for m in self.swing_motors:       
            m.stop_action = Motor.STOP_ACTION_HOLD    
            m.stop()
        
        print("Swing Angle: %i" % self.swing_motorC.position)

             
        

    def set_direction(self, direction):
        print("Setting direction to: " + str(direction))
        self.direction_motor.on_for_degrees(SpeedPercent(10), round(direction*3))
        print("Direction set to: " + str(self.direction_motor.position))
        
    def shoot(self, power):
        # self.swing_motorC.on(SpeedPercent(-dc), block=False)
        # self.swing_motorL.on(SpeedPercent(-dc), block=False)
        # self.swing_motorR.on(SpeedPercent(-dc), block=False)

        print("SHOOT, power: %i" % power)

        for m in self.swing_motors:
            m.duty_cycle_sp = -power

        for m in self.swing_motors:
            m.run_direct()
      
        
        time.sleep(.5)

        self.swing_motorC.wait_until_not_moving()

        for m in self.swing_motors:
            m.reset()

    # End

    def wait_for_button(self):
        self.touch_sensor.wait_for_bump()

    def __set_display(self, str):
        self.console.set_font(font=LARGER_FONT, reset_console=True)
        self.console.text_at(str, column=1, row=1, reset_console=True)


    def wait_for_power_select(self, power=0, angle=0, steps=1):
        self.__set_display("Pow: %i\nAngle: %i" % (power, angle))

        def left():
            power -= steps
            if power < 0:
                power = 0
            self.__set_display("Pow: %i\nAngle: %i" % (power, angle))
            self.buttons.wait_for_released(buttons=['left'], timeout_ms=150)

        def right():
            power += steps
            if power > 100:
                power = 100
            self.__set_display("Pow: %i\nAngle: %i" % (power, angle))
            self.buttons.wait_for_released(buttons=['right'], timeout_ms=150)

        def up():
            angle += steps
            if angle > 110:
                angle = 110
            self.__set_display("Pow: %i\nAngle: %i" % (power, angle))
            self.buttons.wait_for_released(buttons=['up'], timeout_ms=150)

        def down():
            angle -= steps
            if angle < 0:
                angle = 0
            self.__set_display("Pow: %i\nAngle: %i" % (power, angle))
            self.buttons.wait_for_released(buttons=['down'], timeout_ms=150)


        while not self.touch_sensor.is_pressed:
            if self.buttons.left:
                left()
            elif self.buttons.right:
                right()
            elif self.buttons.up:
                up()
            elif self.buttons.down:
                down()

        self.console.set_font(font=DEFAULT_FONT, reset_console=True)
        return (power, angle)

    def select_connection_mode(self):
        self.__set_display("Enable Connection\nLeft: True - Right: False")

        enabled = True
        
        while not self.touch_sensor.is_pressed:
            if self.buttons.left:
                enabled = True
                self.buttons.wait_for_released(buttons=['left'])
                break
            elif self.buttons.right:
                enabled = False
                self.buttons.wait_for_released(buttons=['right'])
                break

        self.console.set_font(font=DEFAULT_FONT, reset_console=True)
        return enabled

    def print(self, string):
        print(string)