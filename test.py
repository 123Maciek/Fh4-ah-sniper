color = (150, 180, 200)  # Replace with your actual color
threshold_color = (220, 220, 220)

def is_color_greater_than(color, threshold):
    return all(c > t for c, t in zip(color, threshold))

# Check if each component of the color is greater than the corresponding component of the threshold color
if is_color_greater_than(color, threshold_color):
    print("Color is greater than (220, 220, 220)")
else:
    print("Color is not greater than (220, 220, 220)")