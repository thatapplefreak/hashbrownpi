try:
    import RPi.GPIO as GPIO
except:
    print("Cannot import RPi.GPIO. Importing FakeRPi")
    try:
        import FakeRPi.GPIO as GPIO
    except:
        print("Cannot import FakeRPI")



class HardwareController:

    led_pins = None  # ordered list of pins LEDs are connected to

    def __init__(self, led_pins):
        """
        Inits the hardware controller
        :param led_pins: Array list of GPIO pins for the LEDs in order
        """
        self.led_pins = led_pins
        GPIO.setmode(GPIO.BOARD)


    def reset_leds(self):
        """
        Resets all LEDs to off
        """
        for i in range(0, len(self.led_pins) - 1):
            self.turn_off_led(i)

    def turn_on_led(self, index):
        """
        Turns on led at the specified index in the array
        :param index: position of led
        """
        GPIO.output(self.led_pins[index], True)

    def turn_off_led(self, index):
        """
        Turns off the led at the specified index in the array
        :param index: position of the led
        """
        GPIO.output(self.led_pins[index], False)
