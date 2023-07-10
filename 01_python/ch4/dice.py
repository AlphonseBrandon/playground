'''
Author: Alphonse Brandon
Date Created: 10-07-2023
Subject: Ch9 - Working with clases and intances of classes
'''
import random
class Dice:
    def __init__(self, sides=6) -> None:
        self.sides = sides

    def roll_die(self) -> None:
        """Print a random number between 1 and the sides a die has"""

        random_num = random.randint(1, self.sides)
        print(random_num)

six_sided = Dice()
six_sided.roll_die()

ten_sided = Dice(10)
ten_sided.roll_die()