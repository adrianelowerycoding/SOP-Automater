
from pynput import mouse, keyboard
import keyboard as kb
# Using Listener and Button
from threading import Event
import mss
import mss.tools
import os
import time 


def sct_pick_key_listener(callback): # sct_pick_key method
    with keyboard.Listener(on_press=callback) as pickKeyListener: 
        pickKeyListener.join()

def sct_key_press_listener(callback): # sct_key_press method
    screenshotKeyPressListener = keyboard.Listener(on_press=callback)
    screenshotKeyPressListener.start()









