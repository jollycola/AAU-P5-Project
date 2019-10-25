from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)

def isMotorsAtAngle(motors, angle):
    for m in motors:
        if m.angle() != angle:
            return False
    
    return True


def motorsRun(motors: [Motor], speed: int):
    for m in motors:
        m.run(speed)