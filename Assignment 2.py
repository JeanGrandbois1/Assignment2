import keyboard
import sys

def close_window(event):
    keyboard.unhook_all()  # Unhook all keyboard events
    sys.exit()  # Close the script

keyboard.on_press(close_window)  # Register the close_window function to be called on key press

print("Hello! I'm glad to be taking Advanced Python!")

while True:
    pass  # Keep the script running until a key press event occurs