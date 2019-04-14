"""
    compass.py
    Creates a compass.
    The user will need to calibrate the compass first. The compass uses the
    built-in clock images to display the position of the needle.

"""
from microbit import *

while True:
    sleep(100)
    needle = ((15 - compass.heading()) // 30) % 12
    display.show(Image.ALL_CLOCKS[needle])