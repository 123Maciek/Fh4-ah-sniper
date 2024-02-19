import pyautogui
import time
from PIL import ImageGrab
import keyboard
import sys

time.sleep(5)


screen_width, screen_height = pyautogui.size()

screen = ImageGrab.grab(bbox=(0, 0, screen_width, screen_height))
pixel_color = screen.getpixel((209, 229))

print(f"Color: {pixel_color}")