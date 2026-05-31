# import cv2Test as cv2T
import ClickerHandlers as ch
import ClickerListeners as cl
import Screenshot as sct


# Ask for screenshot naming convention, file name, and sct folder. Put them all in 

increment = 0

sct_file = input("Screenshot Naming Convention: ").strip()
sct_folder = r'C:\Users\adria\Documents\Coding\Python\Big Projects\SOP Automater\SOP-Automater\Screenshots'

print("Program a screenshot key:")
cl.sct_pick_key_listener(ch.sct_pick_key) # Stops program until sct key chosen
cl.sct_key_press_listener(ch.sct_key_press) # Starts listening for sct key press

ch.sct_loop(lambda inc: sct.sct_fullscreen(sct_file, sct_folder, inc)) # how to access increment_update? 















