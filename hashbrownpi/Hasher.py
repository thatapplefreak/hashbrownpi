import hashlib


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

    def get_available_algorithms(self):
        """
        Available algorithms to test (abstraction to hashlib)
        """
        return hashlib.algorithms_available

    def next_hash(self):
        """
        Takes the data and adds a nonce, hashes and returns results
        :return: hex results
        """
        if self.data is None:
            raise Exception("No data to hash")
        self.nonce += 1
        return self.algorithm(
            self.data + self.nonce
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
