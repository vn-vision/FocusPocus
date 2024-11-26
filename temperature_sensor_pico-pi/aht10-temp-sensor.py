from ahtx0 import AHT10

from machine import Pin, I2C
from time import sleep

# Set up the I2C protocol on I2C controller 1 (there's also 0)
# I2C controller 1 is connected to GPIO 15 (SCL) and 14 (SDA)
# Refer to your Pico pinout for the I2C pins and controller numbers
i2c = I2C(1, scl=Pin(15), sda=Pin(14))

# Create our sensor object from the ahtx0 library using i2c
sensor = AHT10(i2c)

while True:
    print(sensor.temperature) # also try sensor.relative_humdity
    sleep(1)

