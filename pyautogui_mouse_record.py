from pynput.mouse import Listener

def on_move(x, y):
    print ( "Mouse moved")

def on_click(x, y, button, pressed):
    print("Mouse clicked")

def on_scroll(x, y, dx, dy):
    print ("Mouse scrolled")

with Listener(on_move=on_move, on_click=on_click, on_scroll = on_scroll) as listener:
    listener.join()