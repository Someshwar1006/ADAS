import time
import random

# Simulate hardware components (placeholders for actual hardware control)
def moveBackward():
    print("Moving Backward")

def stopMotors():
    print("Motors Stopped")

def Reverse(back, backleft, backright):
    # Example constants for distances
    dist1 = 30
    dist2 = 20
    dist3 = 10

    # Print the distances
    print(f"Distance from Sensor 89 back pin: {back:.2f} cm")
    print(f"Distance from Sensor 1011 backleft pin: {backleft:.2f} cm")
    print(f"Distance from Sensor 1213 backright pin: {backright:.2f} cm")

    # BACK
    if back > dist1:
        print("Safe to Reverse back")
    elif dist1 >= back > dist2:
        print("Back")
    elif back <= dist2:
        print("Back - Brakes Applied")
        stopMotors()

    # BACK LEFT
    if backleft > dist1:
        print("Safe to Reverse back left")
    elif dist1 >= backleft > dist2:
        print("Back Left")
    elif backleft <= dist2:
        print("Back Left - Brakes Applied")
        stopMotors()

    # BACK RIGHT
    if backright > dist1:
        print("Safe to Reverse back right")
    elif dist1 >= backright > dist2:
        print("Back Right")
    elif backright <= dist2:
        print("Back Right - Brakes Applied")
        stopMotors()
