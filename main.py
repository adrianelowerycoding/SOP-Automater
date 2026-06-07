"""
This version of the project will be MODULAR, NON-CLASS. 

The global vars will stay in the modules they pertain to, not a 'global state' module. 

This version of the project will also be NON-LAMBDA. I will have increment be the only value passed into sct_fullscreen(). It will 
pick it up from sct_loop(). I'll put sctFile nad sctFolder in the screenshot.py module. This removes the need for lambda but puts
the proj. into global state. It simplifies the project bc. Lambda complicates it.


Current Update: 6 - 6 - 26 10:24pm 

I'm trying to put all of cv2Test's code into Screenshot.py. But first I have to add a screenshot selection key listener and handler 
to Clicker. There's a big bug I think in the body of sct_select_pick_key() because I just copy and pasted sct_pick_key()'s body 
into it w/ no modifications. Bug doesn't happen when cl.pick_key_listener(ch.sct_select_pick_key) isn't ran in main.py

I made the listeners reusable for all keys selected by the user. This was necessary I believe to make the code concise and easier
to understand. No problems for this so far I believe. 

I've also determined that an Event Dispatcher loop is going to need to be created in ClickerHandlers.py to dispatch functions when
certain screenshot buttons are pressed. 

"""


# import cv2Test as cv2T
import ClickerHandlers as ch
import ClickerListeners as cl
import Screenshot as sct


sct.get_sct_path() # Gathering file and folder info

print("Program a screenshot key:")
cl.pick_key_listener(ch.sct_pick_key) # Stops program until sct key chosen
cl.key_press_listener(ch.key_press) # Starts listening for sct key press

# print("Program a screenshot selection key:")
# cl.pick_key_listener(ch.sct_select_pick_key)
# cl.key_press_listener(ch.key_press)

#ch.sct_loop(sct.sct_fullscreen) 
















