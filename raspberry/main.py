import os
from dotenv import load_dotenv

import threading
import multiprocessing
from ultralytics import YOLO
import time
import cv2
from actuators.led import Led
from actuators.motor import Motor
from utils import (
    weights,
    classes,
    captured_image_name,
    get_prediction,
    send_request,
    CarMovement,
    map_letter_to_movement,
    map_car_movement_to_motors_movement,
)

load_dotenv()

CAMERA_URL = os.getenv("CAMERA_URL")
MODEL_SELECTION = 0


def blink_leds(led_left: Led, led_right: Led, movement):
    if movement == CarMovement.RIGHT:
        led_left.turn_on()
        led_right.blink()
    elif movement == CarMovement.LEFT:
        led_right.turn_on()
        led_left.blink()
    else:
        led_left.turn_on()
        led_right.turn_on()


def run_car(process_method, motor: Motor, led_left: Led, led_right: Led):
    if process_method == 1:
        model = YOLO("models/" + weights[MODEL_SELECTION])
    led_left.turn_on()
    led_right.turn_on()
    motor_proc = None
    led_proc = None
    last_direction = True
    while True:
        cap = cv2.VideoCapture(CAMERA_URL)
        ###TAKE IMAGE
        ret, frame = cap.read()
        if ret:
            print("inja")
            if os.path.exists(captured_image_name):
                os.remove(captured_image_name)
            cv2.imwrite(captured_image_name, frame)
            cap.release()
            print(f"Saved latest frame as {captured_image_name}")
            if process_method == 1:
                ###GET PREDICTION ON IMAGE
                start_time = time.time()
                pred = get_prediction(model, captured_image_name, classes)
                end_time = time.time()
                print(
                    f"Prediction took {end_time - start_time} seconds for model {weights[MODEL_SELECTION]} on raspberry"
                )
            else:
                ###SEND REQUEST TO SERVER
                pred = send_request(captured_image_name)

            if pred is not None:
                print("we got a prediction!")
                print(pred)
                ###GET MOVEMENT BASED ON LETTER
                movement = map_letter_to_movement(pred)
                print(movement.name)

                ###MOTOR MOVEMENT BASED ON MOVEMENT
                if movement != CarMovement.STOP:
                    (
                        left_delay,
                        right_delay,
                        direction,
                    ) = map_car_movement_to_motors_movement(movement)
                if direction is None:
                    direction = last_direction
                last_direction = direction

                ###MOVE MOTOR
                if motor_proc and motor_proc.is_alive():
                    motor_proc.terminate()

                if movement != CarMovement.STOP and movement:
                    motor_proc = multiprocessing.Process(
                        target=motor.run_both_motors,
                        args=(
                            direction,
                            direction,
                            right_delay,
                            left_delay,
                            True,
                        ),
                    )
                    motor_proc.start()

                ###LIGHTS
                if led_proc and led_proc.is_alive():
                    led_proc.terminate()
                led_proc = multiprocessing.Process(
                    target=blink_leds, args=(led_left, led_right, movement)
                )
                led_proc.start()
        else:
            break

    led_left.turn_off()
    led_right.turn_off()


if __name__ == "__main__":
    process_method = int(
        input(
            "Which way of processing do you want?\n1. Local on Raspberry\n2. On Laptop"
        )
    )
    motor = Motor()
    led_left = Led(pin=12)
    led_right = Led(pin=21)
    run_car(process_method, motor, led_left, led_right)
