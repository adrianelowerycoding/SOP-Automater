"""
    I have split the Clicker module into 2 different modules: ClickerListeners and ClickerHandlers. The Listener module houses all
    the listeners and Handlers the callback functions for those listeners. I am able to wire these methods together in main.py
    which makes my code much more readable and easier to add onto. The methods are all static so I've placed
    them in modules, NOT classes. 

    Future Changes: 5 - 31 - 26 

        - Organize functions for cv2Test (cv2 handles the selection screenshot) to make it a module. 
          
"""

from pynput import mouse, keyboard
import keyboard as kb
# Using Listener and Button
from threading import Event
import mss
import mss.tools
import os
import time 


mouseLeftClicked = False
comboEvent = Event()


# There should be some locked-buttons for program commands. Ex. 'q' or 'esc' should stop everything.

# There will be 3 pick key functions. 1. One Button Screenshot, 2. Screenshot Selection Combo, 3. Window Screenshot Combo
# 1. Whatever button you want 
# 2. Whatever two buttons you want
#   - The actual screenshot body is coming from the 'cv2Test.py' file. Aka the screenshot class. 
# 3. Whatever two buttons you want

# When the user selected a screenshot button the key runs the same you choose it. That means the annoying Windows key bind 
# runs the same time you choose the key to replace the Windows key bind. So I had to create an array of those keys and shut
# them down pre-emptively to avoid this behavior.
BEGINNING_DISABLED_KEYS = [
    "left windows",
    "right windows",
    "f1", "f2", "f3", "f4",
    "f5", "f6", "f7", "f8",
    "f9", "f10", "f11", "f12",
]

user_disabled_keys = [] # Whatever buttons the user types in are added to this list. 

# Disables the keys in the array
for key in BEGINNING_DISABLED_KEYS: 
    kb.block_key(key)

# User chooses their screenshots naming convention
screenshotsFile = input("Screenshot Naming Convention: ").strip()

def bindingScreenshotKey(): 

    increment = 0
    screenshotsFolder = r'C:\Users\adria\Documents\Coding\Python\Big Projects\SOP Automater\SOP-Automater\Screenshots'
    screenshotEvent = Event()
    screenshotKey = None # Store user's key choice here
    screenshotKeyPressed = False # Flag
    
    # User chooses their screenshot key
    print("Program a key:")

    def pick_key(key): # make this for full screen
        nonlocal screenshotKey
        print(key)
        screenshotKey = key
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
    
    # See if user's screenshot button has been pressed
    def screenshotKeyPress(keyPressed): 
        nonlocal screenshotKeyPressed
        if keyPressed == screenshotKey:
            screenshotEvent.set()
            screenshotKeyPressed = True
            print("Screenshot key pressed")

    # STEP 1: Listener for picking key / stops when key is picked
    # BLOCKING. This listener blocks all other code from running until a key is picked. 
    with keyboard.Listener(on_press=pick_key) as pickKeyListener: 
        pickKeyListener.join()

    # STEP 2: Listener for screenshot key
    screenshotKeyPressListener = keyboard.Listener(on_press=screenshotKeyPress)
    screenshotKeyPressListener.start()

# STEP 3: Function that only runs if both target key and mouse were clicked.
# We enter this infinite loop and can't escape it. It doesn't matter because the listeners are running in the background on a different
# thread and they're constantly updating var values based on keyboard and mouse events. If the "if" condition is met in the While loop
# the body will execute. 
# We don't want the loop to stop until the user tells it to. It allows the user to keep using their key binds and taking screenshots.
    while True: 
        screenshotEvent.wait()
        increment += 1
        print(f"{increment}")

        if screenshotKeyPressed == True: 
            print("Sct. key detected. Taking screenshot.")
            # Make this a method in screenshot class. Pipe it into this class to keep sepration of concerns. 
            with mss.MSS() as screenshot: 
                screenshotsFolderFile = rf'{screenshotsFolder}\{screenshotsFile}_{increment}.png'
                screenshot.shot(output=screenshotsFolderFile)
                
        screenshotKeyPressed = False
        screenshotEvent.clear()


    # input("Type your chosen key:") # This was a test for alphabet chars. If you blocked a key you can't type it or use it in
                                        # any other context than what you assigned it for. 


bindingScreenshotKey()
       

    


# Listening for a mouse click
# Only records mouse click if user key was pressed first
# def on_click(x, y, button, pressed):
#     global mouseLeftClicked 
#     if pressed and targetKeyPressed and button == mouse.Button.left:
#         mouseLeftClicked = True
#         print ("Left click detected")

# Listens for button and mouse combo to be pressed
# def on_click(x, y, button, pressed): 
#     if pressed and targetKeyPressed and button == mouse.Button.left:
#         comboEvent.set()

# mouseListener = mouse.Listener(on_click=on_click)
# mouseListener.start()




    # if targetKeyPressed and mouseLeftClicked: 
    #     print("Combo has been clicked")

    #     with mss.MSS() as screenshot: 
    #         monitor = screenshot.monitors[3] # primary screen
    #         img = screenshot.grab(monitor)

    #         mss.tools.to_png(img.rgb, img.size, output=screenshotsFolderFile)
        
    #     targetKeyPressed = False
    #     mouseLeftClicked = False


# First Method: screenshot.grab and .to_png
# The dif. is that .grab captures raw data, .to_png takes that raw data and can edit color, size, and file name. 
# .shot only quickly captures the entire screen and saves it. 

# with mss.MSS() as screenshot: 
#         monitor = screenshot.monitors[3] # primary screen
#         img = screenshot.grab(monitor)

#         mss.tools.to_png(img.rgb, img.size, output=screenshotsFolderFile)


# Second Method: shot() 
# This is really only for taking really quick screenshots and saving them, not editing them. 
# It automatically takes screenshot of the default primary screen.
# with mss.MSS() as screenshot: 
#     screenshot.shot(output=screenshotsFolderFile)

    

# I want the program to do something (screenshot and output to document) then reset the targetKeyPressed and mouseLeftClicked values and 
# continue listening. 

# When the if statement happens once it just won't stop. I want it to happen ONCE then reset the values and continue the listening loop
# until the user decides to end it w/ a command. I should hardcode a button to end the program, like `esc`. 

# IDEAS: 
# I could just make a loop and just give it a crazy high number of loops so you could never run out. You then choose to exit the loop. 


       
     


        




# # Custom screenshot function




# When you do a screenshot, create a timestamp for it. This timestamp connects it with the timestamp of the 
# audio chunk. 

# Then when you're doing the transcription, once an image's timestamp comes up in the audio chunk, you tell the clicker
# file to output the particular screenshot to the document. And then also signal that right after that the audio
# text must be inserted/output. 

# ----------

# Creates a background event listener. It waits for your function/event to be triggered, then calls that function automatically when it happens. 
# .join() means "Keep the program running so the listener can keep listening until the event happens"

# listener for key press 
# with keyboard.Listener(on_press=targetKeyPress) as listener: 
#     listener.join()

# listener for mouse click 
# with mouse.Listener(on_click=on_click) as listener: 
#     listener.join()



