import RPi.GPIO as GPIO
import time


class Motor:
    def __init__(
        self,
        in1_1=14,
        in1_2=15,
        in1_3=18,
        in1_4=23,
        in2_1=2,
        in2_2=3,
        in2_3=4,
        in2_4=17,
    ) -> None:
        # self.in1_1 = 17
        # self.in1_2 = 18
        # self.in1_3 = 27
        # self.in1_4 = 22

        # self.in2_1 = 5
        # self.in2_2 = 6
        # self.in2_3 = 16
        # self.in2_4 = 26
        self.in1_1 = in1_1
        self.in1_2 = in1_2
        self.in1_3 = in1_3
        self.in1_4 = in1_4

        self.in2_1 = in2_1
        self.in2_2 = in2_2
        self.in2_3 = in2_3
        self.in2_4 = in2_4

        # defining stepper motor sequence (found in documentation http://www.4tronix.co.uk/arduino/Stepper-Motors.php)
        self.step_sequence = [
            [1, 0, 0, 1],
            [1, 0, 0, 0],
            [1, 1, 0, 0],
            [0, 1, 0, 0],
            [0, 1, 1, 0],
            [0, 0, 1, 0],
            [0, 0, 1, 1],
            [0, 0, 0, 1],
        ]
        self.motor_1_pins = [self.in1_1, self.in1_2, self.in1_3, self.in1_4]
        self.motor_2_pins = [self.in2_1, self.in2_2, self.in2_3, self.in2_4]

        # setting up motor 1 pins
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.in1_1, GPIO.OUT)
        GPIO.setup(self.in1_2, GPIO.OUT)
        GPIO.setup(self.in1_3, GPIO.OUT)
        GPIO.setup(self.in1_4, GPIO.OUT)

        # setting up motor 2 pins
        GPIO.setup(self.in2_1, GPIO.OUT)
        GPIO.setup(self.in2_2, GPIO.OUT)
        GPIO.setup(self.in2_3, GPIO.OUT)
        GPIO.setup(self.in2_4, GPIO.OUT)

        # # initializing motor 1 pins
        # GPIO.output(self.in1_1, GPIO.LOW)
        # GPIO.output(self.in1_2, GPIO.LOW)
        # GPIO.output(self.in1_3, GPIO.LOW)
        # GPIO.output(self.in1_4, GPIO.LOW)

        # # initializing motor 2 pins
        # GPIO.output(self.in2_1, GPIO.LOW)
        # GPIO.output(self.in2_2, GPIO.LOW)
        # GPIO.output(self.in2_3, GPIO.LOW)
        # GPIO.output(self.in2_4, GPIO.LOW)

    def cleanup(self):
        self._motor_1_cleanup()
        self._motor_2_cleanup()
        GPIO.cleanup()

    def _motor_1_cleanup(self):
        GPIO.output(self.in1_1, GPIO.LOW)
        GPIO.output(self.in1_2, GPIO.LOW)
        GPIO.output(self.in1_3, GPIO.LOW)
        GPIO.output(self.in1_4, GPIO.LOW)

    def _motor_2_cleanup(self):
        GPIO.output(self.in2_1, GPIO.LOW)
        GPIO.output(self.in2_2, GPIO.LOW)
        GPIO.output(self.in2_3, GPIO.LOW)
        GPIO.output(self.in2_4, GPIO.LOW)

    def set_step(self, pin1, pin2, pin3, pin4, w1, w2, w3, w4):
        GPIO.output(pin1, w1)
        GPIO.output(pin2, w2)
        GPIO.output(pin3, w3)
        GPIO.output(pin4, w4)

    def run_each_motor(self, direction, delay, motor_pins):
        loop_range = range(8) if not direction else range(7, -1, -1)
        for i in loop_range:
            self.set_step(
                motor_pins[0],
                motor_pins[1],
                motor_pins[2],
                motor_pins[3],
                self.step_sequence[i][0],
                self.step_sequence[i][1],
                self.step_sequence[i][2],
                self.step_sequence[i][3],
            )
            time.sleep(delay)
        # if direction == True:
        #     self.step_sequence.insert(0, self.step_sequence.pop())
        # elif direction == False:
        #     self.step_sequence.append(self.step_sequence.pop(0))

    def run_both_motors(
        self, motor_1_direction, motor_2_direction, delay_1, delay_2, run, duration=0
    ):
        start_time = time.time()
        while run:
            # when time runs out
            try:
                if time.time() - start_time > duration and duration != 0:
                    break
                self.run_each_motor(motor_1_direction, delay_1, self.motor_1_pins)
                self.run_each_motor(motor_2_direction, delay_2, self.motor_2_pins)
            except KeyboardInterrupt:
                self.motor_1_cleanup()
                self.motor_2_cleanup()
                exit(1)

    # def run_motor(self, motor_1_direction, motor_2_direction, delay_1, delay, duration):
    #     try:
    #         motor_1_step_counter = 0
    #         motor_2_step_counter = 0
    #         i = 0

    #         start_time = time.time()

    #         # for i in range(step_count):
    #         while True:
    #             # jump out of the loop after five seconds
    #             if time.time() - start_time > duration:
    #                 break

    #             # motor 1
    #             for pin in range(0, len(self.motor_1_pins)):
    #                 GPIO.output(
    #                     self.motor_1_pins[pin],
    #                     self.step_sequence[motor_1_step_counter][pin],
    #                 )
    #             time.sleep(delay)
    #             if motor_1_direction == True:
    #                 motor_1_step_counter = (motor_1_step_counter - 1) % 8
    #             elif motor_1_direction == False:
    #                 motor_1_step_counter = (motor_1_step_counter + 1) % 8

    #             # motor 2
    #             for pin in range(0, len(self.motor_2_pins)):
    #                 GPIO.output(
    #                     self.motor_2_pins[pin],
    #                     self.step_sequence[motor_2_step_counter][pin],
    #                 )
    #             if motor_2_direction == True:
    #                 motor_2_step_counter = (motor_2_step_counter - 1) % 8
    #             elif motor_2_direction == False:
    #                 motor_2_step_counter = (motor_2_step_counter + 1) % 8

    #             else:  # defensive programming
    #                 print("uh oh... direction should *always* be either True or False")
    #                 self.motor_1_cleanup()
    #                 exit(1)
    #             time.sleep(self.step_sleep)

    #     except KeyboardInterrupt:
    #         self.motor_1_cleanup()
    #         self.motor_2_cleanup()
    #         exit(1)
