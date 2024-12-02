# writing code for dice in game

from random import *
class Dice:
    def __init__(self,sides):
        self.sides=sides

    def roll_dice(self):
        if self.sides < 1 or self.sides> 6:
            return 'invalid number'
        else:
            return randint(1,self.sides)

a=int(input('enter a number on dice from 1 to 6 : '))
d=Dice(a)
print(d.roll_dice())

