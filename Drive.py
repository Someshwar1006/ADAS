import random
import threading
import time

distance_front = 0
distance_front_left = 0
distance_front_right = 0
distance_back = 0
distance_back_left = 0
distance_back_right = 0

stopflag = False
lanebool = False
ACC = False
dist1 = 30
dist2 = 20
dist3 = 10
dist4 = 5
anglelt = 180
anglert = 0
cruiseSpeed = 50

def readDistance(sensor):
    return random.randint(1, 100)

def steer(angle):
    print(f"Steer set to {angle} degrees")

def moveForward():
    print("Moving forward")

def stopMotors():
    global stopflag
    stopflag = True
    print("Motors stopped")

def startMotors():
    motorSpeed = cruiseSpeed * 2.55 
    print(f"Motors started at speed {motorSpeed}")

def lanecenter():
    print("Centering lane")

def adaptiveCruiseControl():
    print("Adaptive Cruise Control activated")

def lcd_clear():
    print("LCD cleared")

def lcd_setCursor(x, y):
    print(f"LCD cursor set to {x}, {y}")

def lcd_print(message):
    print(f"LCD message: {message}")

def Wire_beginTransmission(address):
    print(f"Starting transmission to {address}")

def Wire_write(message):
    print(f"Sending message: {message}")

def Wire_endTransmission():
    print("Ending transmission")

def drive():
    global stopflag

    if lanebool:
        lanecenter()
    if ACC:
        adaptiveCruiseControl()
    if not stopflag:
        moveForward()

    distance_front = readDistance('ultrasonicfr')
    distance_front_left = readDistance('ultrasonicfrleft')
    distance_front_right = readDistance('ultrasonicfrright')

    print(f"Distance front: {distance_front} cm")
    print(f"Distance front left: {distance_front_left} cm")
    print(f"Distance front right: {distance_front_right} cm")

    lcd_clear()
    lcd_setCursor(0, 0)
    lcd_print("Gear : D")

    if distance_front > dist1:
        lcd_setCursor(0, 1)
        lcd_print("Lead Clear")
        Wire_beginTransmission(9)
        Wire_write("4")
        Wire_endTransmission()
        print("Front Ext")
    elif dist2 <= distance_front < dist1:
        print("Front1")
        Wire_beginTransmission(9)
        Wire_write("1")
        Wire_endTransmission()
    elif dist3 < distance_front < dist2:
        print("Front2")
        stopMotors()
        Wire_beginTransmission(9)
        Wire_write("2")
        Wire_endTransmission()
    elif distance_front <= dist3:
        print("Front3")
        if distance_front_left > dist4 or distance_front_right > dist4:
            if distance_front_left > distance_front_right:
                steer(anglelt)
            elif distance_front_left < distance_front_right:
                steer(anglert)
            else:
                steer(90)
        stopMotors()
        Wire_beginTransmission(9)
        Wire_write("3")
        Wire_endTransmission()
