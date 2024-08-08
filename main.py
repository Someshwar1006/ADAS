import Drive
import Reverse
import Park
import Cruise
import threading
import random
import time

distance_front = 0
distance_back = 0
distance_left = 0
distance_right = 0
distance_backleft = 0
distance_backright = 0

Drivebool = 0
Reversebool = 0
Cruisebool = 0
Parkbool = 0

def update_distance(direction):
    global distance_front, distance_back, distance_left, distance_right, distance_backleft, distance_backright

    while True:
        random_distance = random.randint(1, 100)
        with lock:
            if direction == 'front':
                distance_front = random_distance
            elif direction == 'back':
                distance_back = random_distance
            elif direction == 'left':
                distance_left = random_distance
            elif direction == 'right':
                distance_right = random_distance
            elif direction == 'backleft':
                distance_backleft = random_distance
            elif direction == 'backright':
                distance_backright = random_distance

def Get_char():
    global Drivebool
    global Reversebool
    global Parkbool
    global Cruisebool

    key = input()
    print(key)
    if key in ['D', 'd']:
        Drivebool = 1
    elif key in ['P', 'p']:
        Parkbool = 1
    elif key in ['R', 'r']:
        Reversebool = 1
    elif key in ['C', 'c']:
        Cruisebool = 1

def main():
    #print(Reversebool)
    if Drivebool:
        Drive.Drive()
    if Reversebool:
        Reverse.Reverse()
    if Parkbool:
        Park.Park()
    if Cruisebool:
        Cruise.Cruise()

if __name__ == "__main__":
    Get_char()
    while True:
        main()

