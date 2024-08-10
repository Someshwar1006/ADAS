import Drive
import Reverse
import Park
import Cruise
import random
import time
import threading
import tkinter as tk
import sys
import keyboard

# Global variables for distances and driving modes
distances = {'front': 0, 'back': 0, 'frontleft': 0, 'frontright': 0, 'backleft': 0, 'backright': 0}
modes = {'Drive': False, 'Reverse': False, 'Cruise': False, 'Park': False}
direction = None

# Debug mode flag
debug_mode = 1

# Create Tkinter windows
root = tk.Tk()
root.title("Sensor Data Debug")
root.geometry("300x200")

gear_window = tk.Tk()
gear_window.title("Current Gear")
gear_window.geometry("200x100")

# Sensor data labels
labels = {
    'front': tk.Label(root, text=""),
    'frontleft': tk.Label(root, text=""),
    'frontright': tk.Label(root, text=""),
    'backleft': tk.Label(root, text=""),
    'backright': tk.Label(root, text=""),
    'back': tk.Label(root, text="")
}

for key in labels.keys():
    labels[key].pack()

# Gear display label
gear_label = tk.Label(gear_window, text="Current Gear: N/A")
gear_label.pack()

# Battery percentage label
battery_label = tk.Label(root, text="Battery: N/A")
battery_label.pack()

def update_distance(key):
    global distances
    random_distance = random.randint(50, 100)
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
    global modes, direction
    while True:
        if keyboard.is_pressed('f'):
            modes.update({'Drive': True, 'Reverse': False, 'Park': False, 'Cruise': False})
        elif keyboard.is_pressed('p'):
            modes.update({'Drive': False, 'Reverse': False, 'Park': True, 'Cruise': False})
        elif keyboard.is_pressed('r'):
            modes.update({'Drive': False, 'Reverse': True, 'Park': False, 'Cruise': False})
        elif keyboard.is_pressed('c'):
            modes.update({'Drive': False, 'Reverse': False, 'Park': False, 'Cruise': True})

        # Check if gear is in Drive or Reverse and capture WASD keys
        if modes['Drive']:
            if keyboard.is_pressed('w'):
                direction = 'Forward'
            elif keyboard.is_pressed('s'):
                direction = 'Backward'
            elif keyboard.is_pressed('a'):
                direction = 'Left'
            elif keyboard.is_pressed('d'):
                direction = 'Right'
            else:
                direction = None
        elif modes['Reverse']:
            if keyboard.is_pressed('s'):
                direction = 'Backward'
            elif keyboard.is_pressed('a'):
                direction = 'Left'
            elif keyboard.is_pressed('d'):
                direction = 'Right'
            else:
                direction = None
        else:
            direction = None

        time.sleep(0.1)  # Short delay to avoid high CPU usage

def btcontroller():
    # Simulate a Bluetooth controller function that returns connection status and data
    return 1

# Print sensor data in the Tkinter window
def print_sensor_data():
    if debug_mode:
        for key in distances:
            labels[key].config(text=f"Distance from {key}: {distances[key]:.2f} cm")
        root.update_idletasks()

def update_gear_display():
    current_gear = next((gear for gear, active in modes.items() if active), 'N/A')
    gear_label.config(text=f"Current Gear: {current_gear}")
    gear_window.update_idletasks()

def update_battery_display():
    if modes['Park']:
        battery_level = Park.Park(distances['backleft'], distances['backright'])  # Get battery percentage from Park module
        battery_label.config(text=f"Battery: {battery_level:.1f}%")
    else:
        battery_label.config(text="Battery: N/A")
    root.update_idletasks()

def main():
    global modes
    if modes['Drive']:
        update_distances_threaded("drive")
        print_sensor_data()
        controller_value = btcontroller()  # Get the controller value
        Drive.Drive(distances['front'], distances['frontleft'], distances['frontright'], distances['backleft'], distances['backright'], controller_value, direction)
    if modes['Reverse']:
        update_distances_threaded("reverse")
        print_sensor_data()
        controller_value = btcontroller()
        Reverse.Reverse(distances['backleft'], distances['backright'], distances['back'], controller_value, direction)
    if modes['Park']:
        update_distances_threaded("park")
        print_sensor_data()
        Park.Park(distances['backleft'], distances['backright'])
    if modes['Cruise']:
        Cruise.Cruise()

def periodic_update():
    main()
    update_gear_display()
    update_battery_display()
    root.after(500, periodic_update)  # Schedule the next update

if __name__ == "__main__":
    # Start the key event handling in a separate thread
    key_event_thread = threading.Thread(target=handle_key_events, daemon=True)
    key_event_thread.start()

    # Start the periodic update
    periodic_update()

    # Start Tkinter main loop
    root.mainloop()
    gear_window.mainloop()
