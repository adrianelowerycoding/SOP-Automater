
from pynput import mouse, keyboard
import keyboard as kb
# Using Listener and Button
from threading import Event
import mss
import mss.tools
import os
import time 


def pick_key_listener(callback): 
    with keyboard.Listener(on_press=callback) as pick_key_listener: 
        pick_key_listener.join()


def key_press_listener(callback): 
    key_press_listener = keyboard.Listener(on_press=callback)
    key_press_listener.start()









