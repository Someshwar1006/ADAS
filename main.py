import Drive
import Reverse
import Park
import Cruise
import random
import time
import threading
import tkinter as tk
import sys
import keyboard  # Import the keyboard library

# Global variables for distances and driving modes
distances = {'front': 0, 'back': 0, 'frontleft': 0, 'frontright': 0, 'backleft': 0, 'backright': 0}
modes = {'Drive': False, 'Reverse': False, 'Cruise': False, 'Park': False}

# Debug mode flag
debug_mode = '--debug' in sys.argv

# Create a Tkinter window for debugging
if debug_mode:
    root = tk.Tk()
    root.title("Sensor Data Debug")
    root.geometry("300x200")

    labels = {
        'front': tk.Label(root, text=""),
        'frontleft': tk.Label(root, text=""),
        'frontright': tk.Label(root, text=""),
        'backleft': tk.Label(root, text=""),
        'backright': tk.Label(root, text=""),
        'back': tk.Label(root, text="")
    }

    for i, key in enumerate(labels.keys()):
        labels[key].pack()

def update_distance(key):
    global distances
    random_distance = random.randint(1, 100)
    distances[key] = random_distance

def update_distances_threaded(gear):
    global modes
    threads = []

    if gear == 'drive':
        keys = ['front', 'frontleft', 'frontright', 'backleft', 'backright']
    elif gear == 'reverse':
        keys = ['back', 'backleft', 'backright']
    elif gear == 'park':
        keys = ['backleft', 'backright']
    else:
        return

    for key in keys:
        thread = threading.Thread(target=update_distance, args=(key,))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()  # Ensure all threads complete before proceeding

def handle_key_events():
    global modes
    while True:
        if keyboard.is_pressed('d'):
            modes.update({'Drive': True, 'Reverse': False, 'Park': False, 'Cruise': False})
        elif keyboard.is_pressed('p'):
            modes.update({'Drive': False, 'Reverse': False, 'Park': True, 'Cruise': False})
        elif keyboard.is_pressed('r'):
            modes.update({'Drive': False, 'Reverse': True, 'Park': False, 'Cruise': False})
        elif keyboard.is_pressed('c'):
            modes.update({'Drive': False, 'Reverse': False, 'Park': False, 'Cruise': True})
        time.sleep(0.1)  # Short delay to avoid high CPU usage

# Print sensor data in the Tkinter window
def print_sensor_data():
    if debug_mode:
        for key in distances:
            labels[key].config(text=f"Distance from {key}: {distances[key]:.2f} cm")
        root.update_idletasks()

def main():
    global modes
    if modes['Drive']:
        update_distances_threaded("drive")
        print_sensor_data()
        Drive.Drive(distances['front'], distances['frontleft'], distances['frontright'], distances['backleft'], distances['backright'])
    if modes['Reverse']:
        update_distances_threaded("reverse")
        print_sensor_data()
        Reverse.Reverse(distances['backleft'], distances['backright'], distances['back'])
    if modes['Park']:
        update_distances_threaded("park")
        print_sensor_data()
        Park.Park(distances['backleft'], distances['backright'])
    if modes['Cruise']:
        Cruise.Cruise()

if __name__ == "__main__":
    # Start the key event handling in a separate thread
    key_event_thread = threading.Thread(target=handle_key_events, daemon=True)
    key_event_thread.start()

    # Main loop
    while True:
        main()
        time.sleep(0.1)  # Adding a small delay to simulate real-time updates
