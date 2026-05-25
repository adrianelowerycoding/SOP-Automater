"""

This was supposed to be the initial commit. It's the functional programming version. The 
initial version before everything got screwed up with OOP. 

"""


import cv2

top_left_corner=[]
bottom_right_corner=[]

image = cv2.imread(r"C:\Users\adria\Documents\Coding\Python\Big Projects\SOP Automater\SOP-Automater\Screenshots\test.png")
tempImage = image.copy()
 
# function which will be called on mouse input
def drawRectangle(action, x, y, flags, *userdata):
  # Referencing global variables; making them accesible inside this function
  global top_left_corner, bottom_right_corner
  # Mark the top left corner when left mouse button is pressed
  if action == cv2.EVENT_LBUTTONDOWN:
    top_left_corner = [(x,y)]
    # When left mouse button is released, mark bottom right corner
  elif action == cv2.EVENT_LBUTTONUP:
    bottom_right_corner = [(x,y)]   
    # Draw the rectangle; it applies the drawing to the image IN MEMORY; changes not seen because changed image not yet uploaded
    # to window.
    cv2.rectangle(image, top_left_corner[0], bottom_right_corner[0], (0,255,0),2, 8)
    # Window is recreated and new changed image is uploaded into it and therefore displayed on screen.
    cv2.imshow("Window",image)

# Creating the Window the screenshot sits in. 
# cv2.WINDOW_NORMAL allows the window to be resizable
cv2.namedWindow("Window", cv2.WINDOW_NORMAL)
# Setting the window's size to full screen. 
cv2.setWindowProperty("Window", cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
# Starts listener for left button mouse press and release
cv2.setMouseCallback("Window", drawRectangle)

k=0
# After all above stuff has been loaded into memory, we jump into while loop to get program running.
while k!=113: #q quits the loop and the program
    # Actually running/showing/opening the Window we created
    cv2.imshow("Window", image)
    k = cv2.waitKey(0) # Stops loop and waits for a key to be pressed. Mouse listener is not stopped and is still listening.

    if (k == 99): #c replaces original image w/ copy, "wiping" the board clean
        image = tempImage.copy() # Must be COPY because it willl only clear one time if not 
        cv2.imshow("Window", image)

cv2.destroyAllWindows()


# Make user choose screenshot naming convention. 
# Make screenshot names increment. 
# Choose selection created by rectangle. 
# Create 's' command to save screenshot. 


