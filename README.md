# Hardware Lab Project
## Introdction
| Creators | Mohammad Abolnejadian, Amirreza Mirzaei, Mohammadali Khodabandelou |
| :------: | :----------------------------------------------------------------: |
| Semester |                            Spring 2023                             |
|    TA    |                         Aboulfazl Younesi                          |

This project is built for the hardware lab class. The project involves building a car using Raspberry Pi and controlling its movement using hand gestures. The hand gestures are recorded using a phone's camera and detected using the YOLOv8 model.

## Project overview
The Hand Gesture Controlled Car is designed to demonstrate the integration of computer vision and hardware control using Raspberry Pi. By utilizing a phone's camera to capture hand gestures and the YOLOv8 model for gesture detection, the car can be controlled wirelessly based on the recognized gestures.

The key components of the project include:

Raspberry Pi: A credit card-sized single-board computer that serves as the brain of the car.
Motor Driver: Responsible for controlling the motors that drive the car's movement.
Phone Camera: Used to capture hand gestures.
YOLOv8 Model: A deep learning-based object detection model used to detect and classify hand gestures.

## Hardware Requirements
To replicate this project, the following hardware components are required:

Raspberry Pi (3 or later)
Motor Driver (compatible with the Raspberry Pi and your motor)
DC Motors (we used stepper motors in ours and you can so)
Wheels
Chassis or Car Frame (we used a lunch box!) + spacers
Power Source (battery or power bank)
Jumper Wires
USB Webcam or compatible Phone Holder for Raspberry Pi Camera Module
LED

## Software Requirements
The software components required for this project are as follows:

Raspbian OS: Operating system for the Raspberry Pi. You can download it from the official Raspberry Pi website.
Python 3: Programming language used for implementing the project.
OpenCV: Open-source computer vision library for image processing and manipulation.
YOLOv8 Model: Pre-trained YOLOv8 model for hand gesture detection.
IP Cam application: An application installed on your phone to mock the phone's camera as the camera module on Raspberry Pi. We used [Droidcam]([url](https://www.dev47apps.com/)) for this purpose.
Make sure you have the necessary software packages installed before proceeding with the setup.

## Setup Instructions
Follow these steps to set up the Hand Gesture Controlled Car:

- Assemble the Car: Build the car chassis, attach the wheels, and connect the motors to the motor driver as per the instructions provided by the car manufacturer.
- Install Raspbian OS: Flash the Raspbian OS onto an SD card and insert it into the Raspberry Pi. Connect the Raspberry Pi to a monitor, keyboard, and mouse, and boot it up. Follow the on-screen instructions to set up the OS.
- Connect the Hardware: Connect the motor driver to the Raspberry Pi using jumper wires. Make sure to connect the motor driver's control pins to the appropriate GPIO pins of the Raspberry Pi. Refer to the motor driver and Raspberry Pi documentation for the pin mappings.
- Install Dependencies: Install Python 3, OpenCV, and MQTT libraries on the Raspberry Pi. You can use the package manager pip to install these dependencies.
- Clone the Repository: Clone the project repository from GitHub onto the Raspberry Pi.

## Hardware and Packaging
You can see a full video of the final result in the `hardware results` folder. Following is a image of the packaging we came up with.

![alt text](<hardware results/packaging.jpeg>)

As you can see, as this project required a mobile device, and for sure DC motors and the Raspberry Pi needed a reliable power source, we provided three powerbanks, one for the Reaspberry Pi, and one for each of the Motor Drivers. Due to lack of equipments, we made the chasis out of a lunch box. This dicision was due to its plastic material, hard enough to stand the weight of Raspberry Pi, and light enough not to stop the vehicle from moving.