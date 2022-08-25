import utime
import math
import machine
from machine import Pin
from machine import I2C
from lcd_api import LcdApi
from pico_i2c_lcd import I2cLcd

I2C_ADDR     = 0x27 #Decimal 39
I2C_NUM_ROWS = 2
I2C_NUM_COLS = 16

SDA_PIN = 0
SCL_PIN = 1

PLAY_PIN = 2
RESET_PIN = 3

i2c = I2C(0, sda=machine.Pin(SDA_PIN), scl=machine.Pin(SCL_PIN), freq=400000)
lcd = I2cLcd(i2c, I2C_ADDR, I2C_NUM_ROWS, I2C_NUM_COLS)


button_play = Pin(PLAY_PIN, Pin.IN, Pin.PULL_UP)
button_reset = Pin(RESET_PIN, Pin.IN, Pin.PULL_UP)

lcd.putstr("Stopwatch")
utime.sleep(2)
lcd.clear()
lcd.hide_cursor()
timer = 0
running = False

lcd.clear()
lcd.putstr("Stopwatch")

while True:
    
    # If button pressed then toggle
    if (button_play.value()== False):
        running = not running
        print ("Status "+str(running))
        # sleep prevents single press causing multiple play /pause signals
        # this is a simple , but basic methos
        utime.sleep(0.5)
    if (button_reset.value()== False):
        print("Reset")
        timer=0
        lcd.clear()
        lcd.putstr("Stopwatch")
        utime.sleep(0.5)
        
    lcd.move_to(0,1)
    lcd.putstr(str(math.floor(timer)))
    
    if (running):
        timer +=0.1
        utime.sleep(0.1)
        
        