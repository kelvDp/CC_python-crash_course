from random import randint

class Dice:

    def __init__(self,sides=6):
        self.sides = sides

    def roll_dice(self):
        print(randint(1,self.sides))

dice = Dice()
# 6 sided dice rolled ten times:
dice.roll_dice()
dice.roll_dice()
dice.roll_dice()
dice.roll_dice()
dice.roll_dice()
dice.roll_dice()
dice.roll_dice()
dice.roll_dice()
dice.roll_dice()
dice.roll_dice()


# 10 sided dice:
dice2 = Dice(10)
dice2.roll_dice()
dice2.roll_dice()
dice2.roll_dice()
dice2.roll_dice()
dice2.roll_dice()
dice2.roll_dice()
dice2.roll_dice()
dice2.roll_dice()
dice2.roll_dice()
dice2.roll_dice()

# 20 sided dice:
dice3 = Dice(20)
dice3.roll_dice()
dice3.roll_dice()
dice3.roll_dice()
dice3.roll_dice()
dice3.roll_dice()
dice3.roll_dice()
dice3.roll_dice()
dice3.roll_dice()
dice3.roll_dice()
dice3.roll_dice()