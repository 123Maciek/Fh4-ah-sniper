import pyautogui
import time
from PIL import ImageGrab
import keyboard
import sys

def is_color_greater_than(color, threshold):
    return all(c > t for c, t in zip(color, threshold))

def buyout():
    print("buyout")
    screen_width, screen_height = pyautogui.size()
    screen = ImageGrab.grab(bbox=(0, 0, screen_width, screen_height))
    target_color = (255, 255, 255)
    pixel_color = screen.getpixel((158, 412))
    pixel_color2 = screen.getpixel((158, 631))
    pixel_color3 = screen.getpixel((158, 803))
    pixel_color4 = screen.getpixel((158, 1001))
    
    if pixel_color == target_color and pixel_color2 == target_color and pixel_color3 == target_color and pixel_color4 == target_color:
        sys.exit()
    print(f"{pixel_color}, {pixel_color2}, {pixel_color3}, {pixel_color4};")

    while True:
        screen = ImageGrab.grab(bbox=(0, 0, screen_width, screen_height))
        pix = screen.getpixel((475, 544))
        tar = (1, 177, 141)
        if pix == tar:
            break
    
    time.sleep(1.5)
    pyautogui.press('y')
    time.sleep(0.5)
    pyautogui.press('down')
    time.sleep(0.05)
    pyautogui.press('enter')
    time.sleep(0.2)
    pyautogui.press('enter')
    time.sleep(7)

    screen = ImageGrab.grab(bbox=(0, 0, screen_width, screen_height))
    pixel_clr = screen.getpixel((1279, 937))
    if pixel_clr == (23, 23, 23):
        for i in range(7):
            pyautogui.press('down')
            time.sleep(0.05)
        pyautogui.press('enter')
        for i in range(3):
            pyautogui.press('esc')
            time.sleep(0.3)
    else:
        pyautogui.press('enter')
        time.sleep(1)
        pyautogui.press('esc')
        time.sleep(3)
        pyautogui.press('esc')
        time.sleep(0.2)


#########MAIN###############

time.sleep(3)

while True:
    time.sleep(1.8)
    pyautogui.press("enter")
    time.sleep(0.18)
    pyautogui.press("x")
    time.sleep(0.18)
    pyautogui.press("enter")
    time.sleep(0.1)

    # Get the screen resolution
    screen_width, screen_height = pyautogui.size()

    # Capture the screen
    while True:
        screen = ImageGrab.grab(bbox=(0, 0, screen_width, screen_height))
        px = screen.getpixel((209, 229))
        if px == (0, 181, 146):
            time.sleep(0.1)
            break

    while True:
        # Capture the screen
        screen_width, screen_height = pyautogui.size()
        screen2 = ImageGrab.grab()

        pixel = screen2.getpixel((1471, 743))
        pixel2 = screen2.getpixel((1474, 368))
        target = (220, 220, 220)
        target2 = (0, 181, 146)

        if target2 == pixel2:
            buyout()
            break

        if all(c > threshold for c, threshold in zip(pixel, target)):
            time.sleep(0.5)
            screenshot = ImageGrab.grab()
            pixel2 = screen.getpixel((1474, 368))
            if target2 == pixel2:
                buyout()
            else:
                pyautogui.press('esc')
            break

    if keyboard.is_pressed('m'):
        sys.exit()
