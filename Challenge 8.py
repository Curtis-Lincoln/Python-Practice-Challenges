#Curtis Lincoln
#Challenge 8

import random

def DiceRoll(Num_Dice, Sides):

    Rolls = []

    for x in range(Num_Dice):
        Die_Roll = random.randint(1,Sides)
        Rolls.append(Die_Roll)

    return Rolls
    
    
