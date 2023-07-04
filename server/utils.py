weights = ["best_yolov8n.pt", "best_yolov8s.pt", "best_yolov8m.pt", "best_yolov8l.pt"]

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


def get_prediction(model, img, classes, prob_thresh=0.5, show=False):
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
