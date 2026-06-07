
from pynput import mouse, keyboard
import keyboard as kb
# Using Listener and Button
from threading import Event
import mss
import mss.tools
import os
import time 


sctEvent = Event()
sct_key = None # Store user's key choice here
sct_select_key = None

BEGINNING_DISABLED_KEYS = [
    "left windows",
    "right windows",
    "f1", "f2", "f3", "f4",
    "f5", "f6", "f7", "f8",
    "f9", "f10", "f11", "f12",
]

user_disabled_keys = [] # Whatever buttons the user types in are added to this list. 

# Disables the keys in the BEGINNING_DISBALED_KEYS array
for key in BEGINNING_DISABLED_KEYS: 
    kb.block_key(key)


def sct_pick_key(key): 
    global sct_key
    #print("Program a screenshot key:")
    print(key)
    sct_key = key
    print(sct_key)
    key_string = str(key)[4:]
    print(type(key_string))
    print(f"Selected Key: {key_string}")
    kb.block_key(key_string)
    for key in BEGINNING_DISABLED_KEYS:
        if key_string != key: # I'm primarily doing this for if the user doesn't choose "windows" buttons 
            kb.unblock_key(key)
            # I stopped here. 
    if key_string not in BEGINNING_DISABLED_KEYS: 
        user_disabled_keys.append(key_string)
    return False # Stops listener

def sct_select_pick_key(key): 
    global sct_select_key
    #print("Program a screenshot selection key:")
    print(key)
    sct_select_key = key
    print(sct_select_key)
    key_string = str(key)[4:]
    print(type(key_string))
    print(f"Selected Key: {key_string}")
    kb.block_key(key_string)
    for key in BEGINNING_DISABLED_KEYS:
        if key_string != key: # I'm primarily doing this for if the user doesn't choose "windows" buttons 
            kb.unblock_key(key)
            # I stopped here. 
    if key_string not in BEGINNING_DISABLED_KEYS: 
        user_disabled_keys.append(key_string)
    return False # Stops listener

def key_press(key_pressed): 
    if key_pressed == sct_key:
        print("Screenshot key pressed")
        sctEvent.set()
    if key_pressed == sct_select_key:
        print("sct select key pressed")

# 1st sct loop
def sct_loop(sct_method): 
    increment = 0

    while True: 
        sctEvent.wait()
        increment += 1
        print(f"{increment}")

        sct_method(increment) # calling sct_fullscreen() method and passing increment to it
                
        sctEvent.clear()

# 2nd sct loop


# Create one large loop for all screenshot methods. This loop is called an "Event Dispatcher"








    



