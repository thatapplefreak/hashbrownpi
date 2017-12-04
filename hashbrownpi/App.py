import hashlib

class App:
    def main(self):
        # Import config file

        # Introduce user to the application
        print("Welcome to HashbrownPi\n"
              "Copyright 2017 Byron Zaharako & Robert Nill")

        # Run the first simulation. Continue to run sims until the user quits
        var_continue = "y"
        while var_continue is "y":
            self.runSimulation()
            var_continue = input("Run another simulation? (y/n): ")
            while var_continue is not "y" and var_continue is not "n":
                var_continue = input("Please enter \"y\" or \"n\"\n"
                                     "Run another simulation? (y/n): ")

    """
    Run 1..n cycles based on user input.
    """
    def runSimulation(self):
        cycles = self.getCycles()
        difficulty = self.getDifficulty()
        algorithm = self.getAlgorithm()
        # Run the simulation

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


App().main()