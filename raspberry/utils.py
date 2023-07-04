from enum import Enum
from PIL import Image
import numpy as np
import requests
import os
import base64
import json
import cv2

captured_image_name = "captured.jpg"
high_speed_delay = 0.001
low_speed_delay = 0.01

weights = ["best_yolov8n.pt", "best_yolov8m.pt", "best_yolov8l.pt"]

classes = {
    0: "A",
    1: "B",
    2: "C",
    3: "D",
    4: "E",
    5: "F",
    6: "G",
    7: "H",
    8: "I",
    9: "J",
    10: "K",
    11: "L",
    12: "M",
    13: "N",
    14: "O",
    15: "P",
    16: "Q",
    17: "R",
    18: "S",
    19: "T",
    20: "U",
    21: "V",
    22: "W",
    23: "X",
    24: "Y",
    25: "Z",
}

needed_classes = [
    "B",
    "C",
    "L",
    "U",
    "V",
    "W",
    "G",
    "H",
    "A",
    "E",
    "M",
    "N",
    "O",
    "S",
    "T",
    "K",
]


class CarMovement(Enum):
    # each enum value represents its priority (higher is more important)
    FORWARD = 1
    BACKWARD = 2
    LEFT = 3
    RIGHT = 4
    STOP = 5


def send_request(image_path):
    # Load the image
    image = cv2.imread(image_path)

    request_params = {"input_data": np.array(image).tolist()}
    print("request sent")
    response = requests.post(os.getenv("REQUEST_URL"), json=request_params)
    print("request received")
    if response:
        # server_response = response.json()
        server_response = response
    else:
        return None
    print(f"response: {server_response.text}")
    return server_response.text


def get_prediction(model, img, classes, prob_thresh=0.2, show=False):
    result = model(img, show=show)[0].boxes
    class_index = result.cls
    conf = result.conf
    print(class_index, conf)
    if len(class_index) == 0 or conf[0] < prob_thresh:
        return
    for i in range(len(class_index)):
        class_name = classes[int(class_index[i])]
        if class_name in needed_classes:
            return class_name


def map_letter_to_movement(letter: str):
    letter = letter.lower()
    if letter in ["b", "c"]:
        return CarMovement.FORWARD
    elif letter in ["u", "v", "w", "k"]:
        return CarMovement.BACKWARD
    elif letter == "l":
        return CarMovement.LEFT
    elif letter in ["g", "h"]:
        return CarMovement.RIGHT
    elif letter in ["a", "e", "m", "n", "o", "s", "t"]:
        return CarMovement.STOP


def map_car_movement_to_motors_movement(car_movement: CarMovement):
    if car_movement == CarMovement.FORWARD:
        return high_speed_delay, high_speed_delay, True
    elif car_movement == CarMovement.BACKWARD:
        return high_speed_delay, high_speed_delay, False
    elif car_movement == CarMovement.LEFT:
        return 0, high_speed_delay, None
    elif car_movement == CarMovement.RIGHT:
        return high_speed_delay, 0, None
