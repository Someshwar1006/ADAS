import time
import random

# Simulate hardware components (placeholders for actual hardware control)
def moveForward():
    print("Moving Forward")
def stopMotors():
    print("Motors Stopped")

def lanecenter():
    print("Centering Lane")

def adaptiveCruiseControl():
    print("Adaptive Cruise Control")

def Drive(front, frontleft, frontright, backleft, backright):
    # Example constants for distances
    dist1 = 50
    dist2 = 30
    dist3 = 20
    dist4 = 10
    distl = 15
    distr = 15

    # Print the distances
    print(f"Distance from Sensor 23 front pin: {front:.2f} cm")
    print(f"Distance from Sensor 45 frontleft pin: {frontleft:.2f} cm")
    print(f"Distance from Sensor 67 frontright pin: {frontright:.2f} cm")
    print(f"Distance from Sensor 1011 backleft pin: {backleft:.2f} cm")
    print(f"Distance from Sensor 1213 backright pin: {backright:.2f} cm")

    # Example decisions based on distances
    if front > dist1:
        print("Lead Clear")
    elif dist1 >= front > dist2:
        print("Front1")
    elif dist2 >= front > dist3:
        print("Front2")
        stopMotors()
    elif front <= dist3:
        print("Front3")
        if frontleft > distl or frontright > distr:
            if frontleft > frontright:
                print("Turning Left")
            elif frontleft < frontright:
                print("Turning Right")
            else:
                print("Going Straight")
        stopMotors()

    # Front Left
    if frontleft > dist1:
        print("Front Left1")
    elif dist1 >= frontleft > dist2:
        print("Front Left2")
    elif dist2 >= frontleft > dist3:
        print("Front Left - Brakes Applied")
        stopMotors()
    elif frontleft <= dist4:
        print("Front Left - Steering Adjusted")
        stopMotors()

    # Front Right
    if frontright > dist1:
        print("Front Right1")
    elif dist1 >= frontright > dist2:
        print("Front Right2")
    elif dist2 >= frontright > dist3:
        print("Front Right - Brakes Applied")
        stopMotors()
    elif frontright <= dist4:
        print("Front Right - Steering Adjusted")
        stopMotors()

    # Back Left
    if backleft > dist1:
        print("Back Left Ext")
    elif dist1 >= backleft > dist2:
        print("Back Left")
    elif dist2 >= backleft > dist3:
        print("Back Left - Brakes Applied")
        stopMotors()
    elif backleft <= dist4:
        print("Back Left - Steering Adjusted")
        stopMotors()

    # Back Right
    if backright > dist1:
        print("Back Right Ext")
    elif dist1 >= backright > dist2:
        print("Back Right")
    elif dist2 >= backright > dist3:
        print("Back Right - Brakes Applied")
    elif backright <= dist4:
        print("Back Right - Steering Adjusted")
        stopMotors()
