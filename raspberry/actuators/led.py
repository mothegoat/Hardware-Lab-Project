import RPi.GPIO as GPIO
import time

# GPIO.setmode(GPIO.BCM)
# GPIO.setwarnings(False)
# GPIO.setup(21, GPIO.OUT)

# # While loop
# while True:
#     # set GPIO14 pin to HIGH
#     GPIO.output(21, GPIO.HIGH)
#     # show message to Terminal
#     print("LED is ON")
#     # pause for one second
#     time.sleep(1)


#     # set GPIO14 pin to HIGH
#     GPIO.output(23, GPIO.LOW)
#     # show message to Terminal
#     print("LED is OFF")
#     # pause for one second
#     time.sleep(1)


class Led:
    def __init__(self, pin=21) -> None:
        self.pin = pin
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        GPIO.setup(pin, GPIO.OUT)

    def blink(self):
        while True:
            GPIO.output(self.pin, GPIO.HIGH)
            time.sleep(1)
            GPIO.output(self.pin, GPIO.LOW)
            time.sleep(1)

    def turn_on(self):
        GPIO.output(self.pin, GPIO.HIGH)

    def turn_off(self):
        GPIO.output(self.pin, GPIO.LOW)
