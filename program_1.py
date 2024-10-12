import random

def randDice():
    dice1 = random.randint(1,6)
    dice2 = random.randint(1,6)
    return dice1 + dice2

rolls = []
for i in range(100):
    rolls.append(randDice())

average_roll = round(sum(rolls) / len(rolls), 2)
print(f"The average of 100 rolls is: {average_roll}")

