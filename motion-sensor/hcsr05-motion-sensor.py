from machine import Pin
from time import sleep

pir = Pin(15, Pin.IN, Pin.PULL_DOWN)
 
# Give the sensor a moment to initalize
sleep(1)

print('Ready')
 
while True:
     if pir.value():
        print('Motion Detected')
        sleep(1)

