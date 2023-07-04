from flask import Flask, jsonify
from flask import request
import numpy as np
import time
import base64
import json
from utils import get_prediction, weights, classes
from ultralytics import YOLO
import cv2

app = Flask(__name__)
MODEL_SELECTION = 2
model = YOLO(weights[MODEL_SELECTION])


@app.route("/process_image", methods=["POST"])
def process_image():
    print("request received")
    data = request.json

    input_data = np.array(data["input_data"])
    # cv2.imwrite("gotten.jpg", input_data)

    print(input_data)
    start_time = time.time()
    prediction = get_prediction(model, input_data, classes)
    end_time = time.time()
    print(prediction)
    print(
        f"Prediction took {end_time - start_time} seconds for model {weights[MODEL_SELECTION]} on laptop"
    )
    return prediction


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5555, debug=True)
