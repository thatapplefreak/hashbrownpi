import json


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
