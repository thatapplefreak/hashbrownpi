import hashlib
import json
import time
import base64
try:
    import RPi.GPIO as GPIO
except:
    print("Cannot import RPi.GPIO. Importing FakeRPi")
    try:
        import FakeRPi.GPIO as GPIO
    except:
        print("Cannot import FakeRPI")


class App:


    """
    Run 1..n cycles based on user input.
    Pass in the config file for the coinbase data, and the hardware controller for manipulating the LEDs
    """
    def runSimulation(self, config, hardware):
        cycles = self.getCycles()
        difficulty = self.getDifficulty()
        algorithm = self.getAlgorithm()

        for i in range(1, cycles + 1):
            hasher = Hasher(algorithm)
            hasher.set_data(config.get_coinbase() + ''.join(config.get_trasactions()))
            startTime = time.time()
            valid = False
            while not valid:
                hash = str(hasher.next_hash())
                hashbinary = base64.b16decode(hash)
                hashdiff = #calculate this (number of 0s in hashbinary string until hit a 1)
                if hashdiff >= difficulty:
                    valid = True
                    elapsed = time.time() - startTime
                    #lights
                else:
                    #check level of hash
                    #lights
                    pass
            #end timer and record

    """
    Prompt the user for cycles
    Cycles == 1 : n
    """
    def getCycles(self):
        while True:
            cycles = input("Number of times to run simulation (cycles): ")
            try:
                cycles = int(cycles)
                if cycles > 0:
                    return cycles
                else:
                    print("\tPlease enter an integer greater than 0")
            except ValueError:
                print("\tPlease enter an integer between [1 : n]")

    """
    Prompt the user for a difficulty setting for the hash. Difficulty has a direct correlation with the number of
      leading zeroes in a generated hash. Ex: 0x00ff15 has a difficulty of 2, since it has 2 leading zeroes.
    Difficulty == 1 : 16
    """
    def getDifficulty(self):
        while True:
            difficulty = input("Enter a difficulty [1 : 16]: ")
            try:
                difficulty = int(difficulty)
                if difficulty >= 1 and difficulty <= 16:
                    return difficulty
                else:
                    print("\tPlease enter an integer between [1 : 16]")
            except ValueError:
                print("\tPlease enter an integer between [1 : 16]")

    """
    Prompt the user for a hashing algorithm recognized by the python hashing library
    Algorithm == item in hashlib.algorithms_available
    """
    def getAlgorithm(self):
        while True:
            algorithm = input("Enter an algorithm, or type \"help\" for a list of algorithms: ")
            if algorithm == "help":
                print("Algorithms: ")
                for item in hashlib.algorithms_available:
                    print("\t" + item)
            elif algorithm in hashlib.algorithms_available:
                return algorithm
            else:
                print("Unknown algorithm, try again!")


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


class Hasher:
    """
    The "miner" responsible for hashing the data
    """

    algorithm = None
    nonce = 0
    data = None

    def __init__(self, algorithm):
        """
        Forms a hashing "miner"
        :param algorithm: algorithm to use when hashing
        """
        if algorithm not in hashlib.algorithms_available:
            raise Exception("invalid algorithm")
        self.algorithm = getattr(hashlib, algorithm)

    def next_hash(self):
        """
        Takes the data and adds a nonce, hashes and returns results
        :return: hex results
        """
        if self.data is None:
            raise Exception("No data to hash")
        self.nonce += 1
        return self.algorithm(
            str(self.data + str(self.nonce)).encode('utf-8')
        ).hexdigest()

    def reset(self):
        """
        Remove data and reset nonce
        """
        self.nonce = 0
        self.data = None

    def set_data(self, data):
        """
        Set the data
        :param data: the data
        """
        self.data = data


class Config:

    config_file = None  # file reference to config file
    config_dict = None  # dict of config

    def __init__(self):
        pass

    def load(self, config_file):
        self.config_file = config_file
        self.config_dict = json.load(config_file)

    def get_led_pins(self):
        """
        :return: List of the GPIO pins that are connected to LEDs, in order
        """
        return self.config_dict["led_pins"]

    def get_coinbase(self):
        """
        Dummy data for header of block
        :return: dummy data
        """
        return self.config_dict["coinbase"]

    def get_trasactions(self):
        """
        Gets a list of transactions
        :return: list of transactions to put in block
        """
        return self.config_dict["txs"]


if __name__ == '__main__':
    # Import config file, and close it after getting all necessary data
    config = Config()
    config_file = open("config.json")
    config.load(config_file)

    # Initiate hardware controller
    hardware = HardwareController(config.get_led_pins())

    # Introduce user to the application
    print("Welcome to HashbrownPi\n"
          "Copyright 2017 Byron Zaharako & Robert Nill")

    app = App()
    # Run the first simulation. Continue to run sims until the user quits
    var_continue = "y"
    while var_continue is "y":
        app.runSimulation(config, hardware)
        var_continue = input("Run another simulation? (y/n): ")
        while var_continue is not "y" and var_continue is not "n":
            var_continue = input("Please enter \"y\" or \"n\"\n"
                                 "Run another simulation? (y/n): ")