import Drive
import Reverse
import Park
import Cruise
import random
import time
import threading

# Global variables for distances and driving modes
distances = {'front': 0, 'back': 0, 'frontleft': 0, 'frontright': 0, 'backleft': 0, 'backright': 0}
modes = {'Drive': False, 'Reverse': False, 'Cruise': False, 'Park': False}

# Create a barrier for synchronization
#barrier = threading.Barrier(3)  # Number of threads to synchronize

def update_distance(key):
    global distances
    random_distance = random.randint(1, 100)
    distances[key] = random_distance
    #barrier.wait()  # Wait for all threads to reach this point

def update_distances_threaded(gear):
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

def Get_char():
    key = input().strip().upper()
    if key in ['D', 'P', 'R', 'C']:
        modes.update({mode: key == mode[0] for mode in modes})

def main():
    if modes['Drive']:
        update_distances_threaded("drive")
        Drive.Drive(distances['front'], distances['frontleft'], distances['frontright'], distances['backleft'], distances['backright'])
    if modes['Reverse']:
        update_distances_threaded("reverse")
        Reverse.Reverse(distances['backleft'], distances['backright'], distances['back'])
    if modes['Park']:
        update_distances_threaded("park")
        Park.Park(distances['backleft'], distances['backright'])
    if modes['Cruise']:
        Cruise.Cruise()

if __name__ == "__main__":
    Get_char()  # Get the driving mode input from the user

    while True:
        main()
        time.sleep(0.1)  # Adding a small delay to simulate real-time updates
