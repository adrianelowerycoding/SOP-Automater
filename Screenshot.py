from pynput import mouse, keyboard
# Using Listener and Button
from threading import Event
import mss
import mss.tools
import numpy
import cv2

sct_folder = None
sct_file = None

top_left_corner=[]
bottom_right_corner=[]
rectDrawn = False
image = cv2.imread(r"C:\Users\adria\Documents\Coding\Python\Big Projects\SOP Automater\SOP-Automater\Screenshots\test_1.png")
tempImage = image.copy()


def get_sct_path(): 
    global sct_file
    global sct_folder
    sct_file = input("Screenshot Naming Convention: ").strip()
    sct_folder = r'C:\Users\adria\Documents\Coding\Python\Big Projects\SOP Automater\SOP-Automater\Screenshots'

# mss functions: 

def sct_fullscreen(increment):
    print("Sct. key detected. Taking screenshot.")
    with mss.MSS() as screenshot: 
        screenshots_folder_file = rf'{sct_folder}\{sct_file}_{increment}.png'
        screenshot.shot(output=screenshots_folder_file)


# cv2 Functions:

def drawRectangle(action, x, y, flags, *userdata):
  # Referencing global variables; making them accesible inside this function
  global top_left_corner, bottom_right_corner
  global rectDrawn

  # Mark the top left corner when left mouse button is pressed
  if rectDrawn == False and action == cv2.EVENT_LBUTTONDOWN:
    top_left_corner = [(x,y)]
    # When left mouse button is released, mark bottom right corner
  elif rectDrawn == False and action == cv2.EVENT_LBUTTONUP:
    rectDrawn = True
    bottom_right_corner = [(x,y)]   
    # Draw the rectangle; it applies the drawing to the image IN MEMORY; changes not seen because changed image not yet uploaded
    # to window.
    cv2.rectangle(image, top_left_corner[0], bottom_right_corner[0], (0,255,0),2, 8)
    # Window is recreated and new changed image is uploaded into it and therefore displayed on screen.
    cv2.imshow("Window",image)

def window_creation(): 
  # Creating the Window the screenshot sits in. 
  cv2.namedWindow("Window", cv2.WINDOW_NORMAL) # cv2.WINDOW_NORMAL allows the window to be resizable
  # Setting the window's size to full screen. 
  cv2.setWindowProperty("Window", cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)

def mouse_listener(): 
  # Starts listener for left button mouse press and release inside created window; calls 'drawRectangle()' when event detected
  cv2.setMouseCallback("Window", drawRectangle)









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


# -----
# Old Key and Mouse combo: 

# targetKey = keyboard.Key.shift
# targetKeyPressed = False

# def targetKeyPress(keyPressed): 
#     global targetKeyPressed
#     if keyPressed == targetKey:
#         targetKeyPressed = True
#         print("Target key pressed")
#     return False

# def mouse_click(x, y, button, pressed): 
#     if pressed and targetKeyPressed and button == mouse.Button.left:
#         print("Combo detected. Capturing screenshot")

#         with mss.MSS() as screenshot: 
#             screenshot.shot(output=screenshotsFolderFile)
#     return False


# with keyboard.Listener(on_press=targetKeyPress) as targetKeyPressListener: 
#     targetKeyPressListener.join()

# with mouse.Listener(on_click=mouse_click) as mouseClickListener: 
#     mouseClickListener.join()






