import pyautogui as gui
import keyboard
import time
import math

top, left, width, height = 293, 0, 700, 465

last = 0
total_time = 0

y_search_cactus, x_start, x_end = 350, 350, 380
y_search_bird = 275 


time.sleep(4)
while True:
    t1 = time.time()
    if keyboard.is_pressed('q'):  # Emergency Button
        break

    
    if math.floor(total_time) != last:
        x_end += 4
        if x_end >= width:
            x_end = width
        last = math.floor(total_time)

 
    screenshot = gui.screenshot(region=(left, top, width, height))
    pixels = screenshot.load()

    background_color = pixels[440, 30]

    for i in reversed(range(x_start, x_end)):
        if pixels[i, y_search_cactus] != background_color\
                or pixels[i, y_search_bird] != background_color:
            keyboard.press(' ')  # jump
            break

    t2 = time.time()-t1
    total_time += t2