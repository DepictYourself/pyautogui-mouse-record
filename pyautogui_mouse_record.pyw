import logging
import os
from pynput.mouse import Listener

desktop = os.path.expanduser("~/Desktop")

logging.basicConfig(filename="{0}/mouse_log.txt".format(desktop), level=logging.DEBUG, format="%(asctime)s: %(message)s")

def on_move(x, y):
    logging.info("pyautogui.moveTo(" + str(x) + ", " + str(y) + ")")

def on_click(x, y, button, pressed):
    logging.info("pyautogui.mouseDown(button='" + str(button)[7:] + "')" if pressed 
        else "pyautogui.mouseUp(button='" + str(button)[7:] + "')")


#def on_scroll(x, y, dx, dy):
#    print ("Mouse scrolled")

with Listener(on_move=on_move, on_click=on_click ) as listener:
    listener.join()