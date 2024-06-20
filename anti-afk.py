import pyautogui
import keyboard
import time

target_colors = [
    '#7AF074', '#FEE663', '#5051E5', '#8821DC',
    '#EB2025', '#01EEFE', '#FC2C74', '#2AF79E'
]

def hex_to_rgb(hex_color):
    hex_color = hex_color.lstrip('#')
    return tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))

target_colors_rgb = [hex_to_rgb(color) for color in target_colors]

def click_on_color(color):
    screen = pyautogui.screenshot()
    width, height = screen.size
    for x in range(width):
        for y in range(height):
            if screen.getpixel((x, y)) == color:
                pyautogui.click(x, y)
                return

try:
    while True:
        for color in target_colors_rgb:
            click_on_color(color)
            time.sleep(0.01)
            print("https://discord.gg/MqvmBu5tWa")

        if keyboard.is_pressed('='):
            print("Script Stopping : https://discord.gg/MqvmBu5tWa")
            break

except KeyboardInterrupt:
    print("Script terminated : https://discord.gg/MqvmBu5tWa")
