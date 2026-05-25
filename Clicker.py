from pynput import mouse, keyboard
# Using Listener and Button
from threading import Event
import mss
import mss.tools
import os
import time 

# Store the user's key choice here. Can reuse this.
targetKey = None
targetKeyPressed = False # this was the "armed"
mouseLeftClicked = False
comboEvent = Event()
increment = 0
screenshotsFolder = r'C:\Users\adria\Documents\Coding\Python\Big Projects\SOP Automater\SOP-Automater\Screenshots'

# User chooses their screenshots naming convention
screenshotsFile = input("Screenshot Naming Convention: ").strip()


# User chooses their key
print("Program a key:")

def pick_key(key):
    global targetKey
    targetKey = key
    keyString = str(key)[4:]
    print(type(keyString))
    print(f"Selected Key: {keyString}")
    return False # Stops listener 

# See if user's button has been pressed
def targetKeyPress(keyPressed): 
    global targetKeyPressed
    if keyPressed == targetKey:
        targetKeyPressed = True
        print("Target key pressed")


# Listening for a mouse click
# Only records mouse click if user key was pressed first
# def on_click(x, y, button, pressed):
#     global mouseLeftClicked 
#     if pressed and targetKeyPressed and button == mouse.Button.left:
#         mouseLeftClicked = True
#         print ("Left click detected")

# Listens for combo to be pressed
def on_click(x, y, button, pressed): 
    if pressed and targetKeyPressed and button == mouse.Button.left:
        comboEvent.set()


# STEP 1: Listener for picking key / stops when key is picked
# BLOCKING. This listener blocks all other code from running until a key is picked. 
with keyboard.Listener(on_press=pick_key) as pickKeyListener: 
    pickKeyListener.join()

# STEP 2: Listener for BOTH key press and mouse click
targetKeyPressListener = keyboard.Listener(on_press=targetKeyPress)
mouseListener = mouse.Listener(on_click=on_click)

targetKeyPressListener.start()
mouseListener.start()

# STEP 3: Function that only runs if both target key and mouse were clicked.
# We enter this infinite loop and can't escape it. It doesn't matter because the listeners are running in the background on a different
# thread and they're constantly updating var values based on keyboard and mouse events. If the "if" condition is met in the While loop
# the body will execute. 
# We don't want the loop to stop until the user tells it to. It allows the user to keep using their key binds and taking screenshots.

while True: 
    comboEvent.wait()
    increment += 1
    print(f"{increment}")

    print("Combo detected. Taking screenshot.")
    
    with mss.MSS() as screenshot: 
        screenshotsFolderFile = rf'{screenshotsFolder}\{screenshotsFile}_{increment}.png'
        screenshot.shot(output=screenshotsFolderFile)
        
    targetKeyPressed = False
    comboEvent.clear()



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



