import pyautogui
import time

time.sleep(5)

# Get the current mouse position
mouse_x, mouse_y = pyautogui.position()

# Print the mouse position
print(f"Mouse position - X: {mouse_x}, Y: {mouse_y}")