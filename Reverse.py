import time
import random
last_brake_time = 0

# Simulate hardware components (placeholders for actual hardware control)
def moveBackward():
    print("Moving Backward")

def stopMotors():
    print("Motors Stopped")

def reverseBack():
    print("Safe to Reverse Back")

def reverseBackLeft():
    print("Safe to Reverse Back Left")

def reverseBackRight():
    print("Safe to Reverse Back Right")

def handleManualDirection(direction):
    if direction == 'Backward':
        moveBackward()
    elif direction == 'Left':
        reverseBackLeft()
    elif direction == 'Right':
        reverseBackRight()


def Reverse(back, backleft, backright, man_flag, direction):
    global last_brake_time

    current_time = time.time()
    if last_brake_time and (current_time - last_brake_time < 2):
        if direction == 's':
            print("Movement Backward is temporarily disabled due to recent braking.")
        return

    if man_flag == 1:
        handleManualDirection(direction)
        return

    # Automatic mode logic
    dist1 = 30
    dist2 = 20
    dist3 = 10

    if back > dist1:
        reverseBack()
    elif dist1 >= back > dist2:
        reverseBack()
    elif back <= dist2:
        print("Back - Brakes Applied")
        stopMotors()
        last_brake_time = current_time

    if backleft > dist1:
        reverseBackLeft()
    elif dist1 >= backleft > dist2:
        reverseBackLeft()
    elif backleft <= dist2:
        print("Back Left - Brakes Applied")
        stopMotors()
        last_brake_time = current_time

    if backright > dist1:
        reverseBackRight()
    elif dist1 >= backright > dist2:
        reverseBackRight()
    elif backright <= dist2:
        print("Back Right - Brakes Applied")
        stopMotors()
        last_brake_time = current_time

def get_direction_input():
    # Replace with actual input mechanism
    direction = input("Enter direction (s, a, d): ").strip()
    if direction not in ['s', 'a', 'd']:
        print("Invalid Direction Input")
        return None
    return direction

if __name__ == "__main__":
    man_flag = 1  # Example manual flag
    last_brake_time = None
    while True:
        direction = get_direction_input()
        if direction is None:
            continue  # Skip invalid inputs

        # Example sensor values
        back = random.randint(0, 40)
        backleft = random.randint(0, 40)
        backright = random.randint(0, 40)

        print(f"Calling Reverse with: back={back}, backleft={backleft}, backright={backright}, direction={direction}")  # Debug print

        Reverse(back, backleft, backright, man_flag, direction)
        time.sleep(0.1)  # Adding a small delay to simulate real-time updates
