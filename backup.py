screen = ImageGrab.grab(bbox=(0, 0, screen_width, screen_height))
    target_color = (255, 255, 255)
    target_color2 = (0, 181, 146)
    pixel_color = screen.getpixel((1474, 368))
    pixel_color2 = screen.getpixel((158, 631))
    pixel_color3 = screen.getpixel((158, 803))
    pixel_color4 = screen.getpixel((158, 1001))
    
    if pixel_color == target_color and pixel_color2 == target_color and pixel_color3 == target_color and pixel_color4 == target_color:
        sys.exit()

    if pixel_color == target_color2:
        pyautogui.press('y')
        time.sleep(0.5)

        screen = ImageGrab.grab(bbox=(0, 0, screen_width, screen_height))

        pixel_clr = screen.getpixel((1255, 919))
        if pixel_clr != target_color:
            pyautogui.press('esc')
            time.sleep(1)
            pyautogui.press('esc')
            print("lol")

        pyautogui.press('down')
        time.sleep(0.05)
        pyautogui.press('enter')
        time.sleep(0.2)
        pyautogui.press('enter')
        time.sleep(7)
        pyautogui.press('enter')
        time.sleep(1)
        pyautogui.press('esc')
        time.sleep(3)
        pyautogui.press('esc')
        time.sleep(0.2)
    else:
        pyautogui.press("esc")
    if keyboard.is_pressed('m'):
        sys.exit()
