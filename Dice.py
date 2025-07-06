import random

class Dice(object):
    """For the creation of a simple dice object"""
    def __init__(self, numSides=6):
        """
        Inputs:
            numSides: An integer representing the number of sides of the dice, default to 6
        Purpose: Initializes a Dice object with the number of sides given
        """
        self.numSides = numSides
        self.Sides = list(range(1, self.numSides+1))

    def toss(self):
        """
        Purpose: To model a 'random' toss of a self.numSides sided die
        OutPut: An Integer representing the number that the die 'landed on'
        """
        return random.choice(self.Sides)

    def test_prob(self, numTrials = 1000):
        """
        Input:
            numTrials: An integer that defaults to 1000, representing the number
                       of times to test rolling the Dice object
        Purpose:
            Tests the probability of each number coming out, using the numTrials
            given
        Output:
            A dictionary mapping each number to their experimentally determined
            probabilities of being landed on by the dice
        """
        rv = {i:0 for i in self.Sides}        #Initialize each side to 0 probability

        for test in range(numTrials):
            landed = self.toss()                #For each trial, add 1 to landed number
            rv[landed] += 1/float(numTrials)    #Divide each value by numTrials for probability

        for side in rv:                         #Round results to read easier
            rv[side] = round(rv[side], 4)

        return rv
    

class SimpleLoadedDice(Dice):
    """For the creation of a Dice object that is twice as likely to land on
    its highest value than any other number"""


    def toss(self):
        """
        Purpose: To model a 'random' toss of a self.numSides sided loaded die
        OutPut: An Integer representing the number that the loaded die 'landed on'
        """
        return random.choice(self.Sides + [self.numSides])
    

class UnknownLoadedDice(Dice):
    """For the creation of a Dice object that is three times as likely to land
    on one side, but the chosen side is random and unknown to user"""


    def __init__(self, numSides):
        """
        Inputs:
            numSides: An integer representing the number of sides of the dice
        Purpose:
            Initializes a loaded Dice object with the number of sides given and
            an unknown loaded side
        """
        super(UnknownLoadedDice, self).__init__(numSides)
        self.loadedSide = random.choice(self.Sides)


    def toss(self):
        """
        Purpose: To model a 'random' toss of a self.numSides sided loaded die
        OutPut: An Integer representing the number that the loaded die 'landed on'
        """
        return random.choice(self.Sides + 2*[self.loadedSide])
