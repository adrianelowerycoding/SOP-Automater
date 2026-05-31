from pynput import mouse, keyboard
# Using Listener and Button
from threading import Event
import mss
import mss.tools
import numpy
import cv2

targetKey = keyboard.Key.shift
targetKeyPressed = False

screenshotsFolder = r'C:\Users\adria\Documents\Coding\Python\Big Projects\SOP Automater\SOP-Automater\Screenshots'

screenshotsFile = input("Screenshot Naming Convention: ").strip()
screenshotsFile = screenshotsFile + ".png"
screenshotsFolderFile = rf'{screenshotsFolder}\{screenshotsFile}'
print(screenshotsFolderFile)

def targetKeyPress(keyPressed): 
    global targetKeyPressed
    if keyPressed == targetKey:
        targetKeyPressed = True
        print("Target key pressed")
    return False

def mouse_click(x, y, button, pressed): 
    if pressed and targetKeyPressed and button == mouse.Button.left:
        print("Combo detected. Capturing screenshot")

        with mss.MSS() as screenshot: 
            screenshot.shot(output=screenshotsFolderFile)
    return False


with keyboard.Listener(on_press=targetKeyPress) as targetKeyPressListener: 
    targetKeyPressListener.join()

with mouse.Listener(on_click=mouse_click) as mouseClickListener: 
    mouseClickListener.join()


# First Method: screenshot.grab and .to_png
# The dif. is that .grab captures raw data, .to_png takes that raw data and can edit color, size, and file name. 
# .shot only quickly captures the entire screen and saves it. 

# with mss.MSS() as screenshot: 
#         monitor = screenshot.monitors[3] # primary screen
#         img = screenshot.grab(monitor)

#         mss.tools.to_png(img.rgb, img.size, output=screenshotsFolderFile)


# Second Method: shot() 
# This is really only for taking really quick screenshots and saving them, not editing them. 
# with mss.MSS() as screenshot: 
#     screenshot.shot(output=screenshotsFolderFile)


# Third Method: .grab() and using 





