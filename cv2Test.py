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
        self.image = cv2.imread(image_path)
        self.tempImage = self.image.copy()
        
        # function which will be called on mouse input
    def drawRectangle(self, action, x, y, flags, *userdata):
        # Mark the top left corner when left mouse button is pressed
        if action == cv2.EVENT_LBUTTONDOWN:
            self.top_left_corner = [(x,y)]
            # When left mouse button is released, mark bottom right corner
        elif action == cv2.EVENT_LBUTTONUP:
            self.bottom_right_corner = [(x,y)]   
            # Draw the rectangle
            cv2.rectangle(self.image, self.top_left_corner[0], self.bottom_right_corner[0], (0,255,0),2, 8)
            # This updates the screen immediately after drawing
            cv2.imshow("Window", self.image)


    def run(self):
        # Creating the Window the screenshot sits in. 
        # cv2.WINDOW_NORMAL allows the window to be resizable
        cv2.namedWindow("Window", cv2.WINDOW_NORMAL)
        # Setting the window's size to full screen.
        cv2.setWindowProperty("Window", cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
        # Calls/loads the drawRectangle method and starts listening for the mouse event. Immediately after loading 
        # it runs the while loop below. 
        cv2.setMouseCallback("Window", self.drawRectangle)

        k=0

        while k!=113 : # q and s keys end the loop
            self.increase = 0
            # Initially running/showing/opening the Window we created
            cv2.imshow("Window", self.image)
            k = cv2.waitKey(0)

            if (k == 99): # c key clears the current selection and replaces it with copy image
                tempImage = self.tempImage.copy()
                cv2.imshow("Window", tempImage)

            if (k == 115): # s saves the selection
                self.increment = self.increase + 1
                x1, y1 = self.top_left_corner[0]
                x2, y2 = self.bottom_right_corner[0]

                cv2.imwrite(rf"C:\Users\adria\Documents\Coding\Python\Big Projects\SOP Automater\SOP-Automater\Screenshots\screenshot{self.increment}.png",
                             self.tempImage[min(y1,y2):max(y1,y2), min(x1,x2):max(x1,x2)]
                             )
                print("Saved screenshot selection")

        cv2.destroyAllWindows()

# This is better than hardcoding ASCII
# while True:
#     k = cv2.waitKey(0) & 0xFF
#     if k == ord('q'):

test = ScreenshotDraw(
    r"C:\Users\adria\Documents\Coding\Python\Big Projects\SOP Automater\SOP-Automater\Screenshots\test.png"
    )

test.run()



