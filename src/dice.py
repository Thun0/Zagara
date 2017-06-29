import random

class Dice:

    @staticmethod
    def roll(sides):
        return random.randint(1, sides)
