
import time
from pynput import keyboard

def on_release(key):
    print('release:', key)

def on_press(key):
    print('press:', key)


keyboard_listener = keyboard.Listener(on_press=on_press, on_release=on_release)
keyboard_listener.start()

while True:
    time.sleep(1)
