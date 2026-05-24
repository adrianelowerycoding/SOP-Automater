"""
I will use this CV2 solution as an easy solution/version of this app. 

CV2 is not the  best solution/library for this problem, it is the most basic. If I want to create a smoother application I will 
have to use PySide6 and Qt, but that is a massive learning curve. I think I would like to simply get a prototype working and 
then in the future I can perfect this app w/ other libraries. 

Future additions I want to make are: Selection drawing in real time and the freeze frame window being smooth. 

"""


import cv2

class ScreenshotDraw:

    def __init__(self, image_path):
        self.top_left_corner=[]
        self.bottom_right_corner=[]
        self.image_path = r"C:\Users\adria\Documents\Coding\Python\Big Projects\SOP Automater\SOP-Automater\Screenshots\test.png"

        self.image = cv2.imread(image_path)
        self.tempImage = image.copy()
 
# function which will be called on mouse input
def drawRectangle(action, x, y, flags, *userdata):
  # Referencing global variables
  global top_left_corner, bottom_right_corner
  # Mark the top left corner when left mouse button is pressed
  if action == cv2.EVENT_LBUTTONDOWN:
    top_left_corner = [(x,y)]
    # When left mouse button is released, mark bottom right corner
  elif action == cv2.EVENT_LBUTTONUP:
    bottom_right_corner = [(x,y)]   
    # Draw the rectangle
    cv2.rectangle(image, top_left_corner[0], bottom_right_corner[0], (0,255,0),2, 8)
    cv2.imshow("Window",image)

# Creating the Window the screenshot sits in. 
# cv2.WINDOW_NORMAL allows the window to be resizable
cv2.namedWindow("Window", cv2.WINDOW_NORMAL)
# Setting the window's size to full screen. 
cv2.setWindowProperty("Window", cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
# Listens for left button mouse press and release
cv2.setMouseCallback("Window", drawRectangle)

k=0

while k!=113: 
    # Actually running/showing/opening the Window we created
    cv2.imshow("Window", image)
    k = cv2.waitKey(0)

    if (k == 99):
        image = tempImage.copy()
        cv2.imshow("Window", image)

cv2.destroyAllWindows()

# This is better than hardcoding ASCII
# while True:
#     k = cv2.waitKey(0) & 0xFF
#     if k == ord('q'):

