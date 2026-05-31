
from pynput import mouse, keyboard
import keyboard as kb
# Using Listener and Button
from threading import Event
import mss
import mss.tools
import os
import time 


increment = 0
sctFile = input("Screenshot Naming Convention: ").strip()
sctFolder = r'C:\Users\adria\Documents\Coding\Python\Big Projects\SOP Automater\SOP-Automater\Screenshots'
sctEvent = Event()
sctKey = None # Store user's key choice here
sctKeyPressed = False # Flag

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
    global sctKey
    print("Program a screenshot key:")
    print(key)
    sctKey = key
    print(key)
    keyString = str(key)[4:]
    print(type(keyString))
    print(f"Selected Key: {keyString}")
    kb.block_key(keyString)
    for key in BEGINNING_DISABLED_KEYS:
        if keyString != key: # I'm primarily doing this for if the user doesn't choose "windows" buttons 
            kb.unblock_key(key)
            # I stopped here. 
    if keyString not in BEGINNING_DISABLED_KEYS: 
        user_disabled_keys.append(keyString)
    return False # Stops listener 

def sct_key_press(keyPressed): 
    global sctKeyPressed
    if keyPressed == sctKey:
        sctEvent.set()
        sctKeyPressed = True
        print("Screenshot key pressed")

# 1st sct loop
def sct_loop(sct_method): 
    while True: 
        sctEvent.wait()
        increment += 1
        print(f"{increment}")

        if sctKeyPressed == True: 
            print("Sct. key detected. Taking screenshot.")
            # Make this a method in screenshot class. Pipe it into this class to keep sepration of concerns. 
            with mss.MSS() as screenshot: 
                screenshotsFolderFile = rf'{sctFolder}\{sctFile}_{increment}.png'
                screenshot.shot(output=screenshotsFolderFile)
                
        sctKeyPressed = False
        sctEvent.clear()

# 2nd sct loop








    



