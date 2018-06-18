import sys
import time
sys.path.append('/home/pi/Adafruit_Micropython_Blinka/src')
sys.path.append('/home/pi/Adafruit_Python_GPIO')

import board
import digitalio

print("hello blinka!")

led = digitalio.DigitalInOut(board.D4)
led.direction = digitalio.Direction.OUTPUT

button = digitalio.DigitalInOut(board.D18)
button.direction = digitalio.Direction.INPUT
button.pull = digitalio.Pull.DOWN

while True:
    led.value = button.value
    time.sleep(0.1)
