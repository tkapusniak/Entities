import random

attackRoll = 0
strMod = 3
melee = 5
size = 1
dieface = 6
die = 2
i = 0
rollOne = 0
rollTwo = 0

roll = random.randint(1, 20)
print("Roll " + str(roll))
attackRoll = (roll + strMod + size)
if roll == 1:
    print("Attack misses")

elif roll <= 19:
    while i < die:
        rollOne += random.randint(1, dieface)
        i += 1

    print(rollOne)
    damage = rollOne + melee
    print(damage)

elif roll == 20:
    while i < die:
        rollOne += random.randint(1, dieface)
        i += 1

    i = 0
    print(rollOne)
    damage = rollOne + melee
    print(damage)
    while i < die:
        rollTwo += random.randint(1, dieface)
        i += 1

    print(rollTwo)
    damageCrit = rollTwo + melee
    print(damageCrit)

