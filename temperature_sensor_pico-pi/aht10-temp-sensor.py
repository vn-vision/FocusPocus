from ahtx0 import AHT10
from machine import Pin, I2C
from time import sleep

# Initialize I2C for the AHT10 sensor
i2c = I2C(1, scl=Pin(15), sda=Pin(14))
sensor = AHT10(i2c)

# Define pins for LEDs and the button
blue_led = Pin(2, Pin.OUT)  # Blue LED for cooling
red_led = Pin(3, Pin.OUT)   # Red LED for heating
override_button = Pin(4, Pin.IN, Pin.PULL_DOWN)  # Button with pull-down resistor

# Initial state variables
automatic_mode = True  # Start in automatic mode

def handle_override(pin):
    """
    Toggle between automatic and manual control modes
    whenever the button is pressed.
    """
    global automatic_mode
    automatic_mode = not automatic_mode
    print("Override button pressed. Automatic mode:", automatic_mode)

# Attach interrupt to the button for handling mode toggle
override_button.irq(trigger=Pin.IRQ_RISING, handler=handle_override)

while True:
    if automatic_mode:
        temperature = sensor.temperature
        print("Temperature:", temperature)

        # Cooling mode
        if temperature > 28:
            blue_led.on()
            red_led.off()
            print("Cooling... (Blue LED ON)")

        # Heating mode
        elif temperature < 15:
            blue_led.off()
            red_led.on()
            print("Heating... (Red LED ON)")

        # Neutral mode
        else:
            blue_led.off()
            red_led.off()
            print("Temperature normal. Both LEDs OFF.")

    else:
        print("Manual override mode. No automatic control.")
        blue_led.off()
        red_led.off()

    sleep(1)
