from ev3dev2.motor import Motor, OUTPUT_A, OUTPUT_B, OUTPUT_D, SpeedPercent, MoveTank, MediumMotor


motor = MediumMotor(OUTPUT_D)

motor.run_direct(20)

while True:
    pass