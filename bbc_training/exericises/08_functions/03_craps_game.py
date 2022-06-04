# Craps game

import random


def shuffleDice():
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    return dice1, dice2


def craps(dice1, dice2, previousScore=None):
    sum = dice1 + dice2
    print(f"You rolled {dice1} + {dice2} = {sum}")

    # If the sum is 2, 3, or 12 (called craps), you lose; if the sum is 7 or 11 (called natural), you win; if the sum is another value (i.e., 4, 5, 6, 8, 9, or 10), a point is established
    if previousScore == sum:
        print("You win")
        return 0
    if sum == 2 or sum == 3 or sum == 12:
        print("Craps: you lose")
        return 0
    elif sum == 7 or sum == 11:
        print("Natural: you win")
        return 0
    else:
        return sum


dice1, dice2 = shuffleDice()
score = craps(dice1, dice2)
while score > 0:
    score = craps(dice1, dice2, score)
