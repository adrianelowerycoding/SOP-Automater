"""
NEXT CHANGE: 

I have multiple state vars. that are spread across multiple modules. I should group them into one module so they're easier
to keep track of and use. The states are: 

increment
sctKey
sctEvent #I'm not totally sure about this one

NEXT CHANGE: UPDATE: 6 - 6 - 26 

I will NOT make a global module for global variables. That makes no sense for this project; it makes more sense organizationally to 
put the global vars in the modules they pertain to since they only pertain to their certain modules. 

I will make two versions of this project: One w/ global modular variables (non-class), and a modular class version w/ no global vars. 
This will show that I am able to convert projects to OOP and will also help if I ever intend to scale this project in the future. 

"""

# Wouldn't it just be so much easier just to have increment be the only value passed into sct_fullscreen? It would pick it up from
# sct_loop. Put sctFile and sctFolder in the screenshot.py module. This would remove the need for lambda but would put me into global
# state. 
# One hand: It's important to know about lambda and learn about it. 
# 2nd hand: My code would be simplified w/o lambda. I could always use classes/config object to get rid of global state. BUT why? My
# program relies on user input and states don't change after being set; so I don't see why it would make sense to use classes unless
# I just want to simply encapsulate data in case I want to grow this project in the future or just show that i know OOP and convert the 
# code base into OOP to showcase that.


# import cv2Test as cv2T
import ClickerHandlers as ch
import ClickerListeners as cl
import Screenshot as sct


# Ask for screenshot naming convention, file name, and sct folder. Put them all in 

sct_file = input("Screenshot Naming Convention: ").strip()
sct_folder = r'C:\Users\adria\Documents\Coding\Python\Big Projects\SOP Automater\SOP-Automater\Screenshots'

print("Program a screenshot key:")
cl.sct_pick_key_listener(ch.sct_pick_key) # Stops program until sct key chosen
cl.sct_key_press_listener(ch.sct_key_press) # Starts listening for sct key press

ch.sct_loop(lambda increment: sct.sct_fullscreen(sct_file, sct_folder, increment)) 
# 1. while loop starts 
# 2. while loop is paused until event happens
# 3. Once event happens the sct_method is called and increment is passed to it 
# 4. 

# a function calling a function 
















