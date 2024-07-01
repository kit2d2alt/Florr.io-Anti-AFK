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
    step = 4  # pixel skip area
    avoid_area = (100, 100, 300, 300)  
    
    for x in range(0, width, step):
        for y in range(0, height, step):
            # if ngz NA
            if (avoid_area[0] <= x <= avoid_area[2] and avoid_area[1] <= y <= avoid_area[3]):
                continue  # skips pixels
            
            if screen.getpixel((x, y)) == color:
                pyautogui.click(x, y)
                return

try:
    while True:
        for color in target_colors_rgb:
            click_on_color(color)
            time.sleep(0.01)
            print("Scanning")

        if keyboard.is_pressed('='):
            print("Script Stopping : Join https://discord.gg/MqvmBu5tWa")
            break

except KeyboardInterrupt:
    print("Script terminated : Join https://discord.gg/MqvmBu5tWa")
