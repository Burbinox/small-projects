from enum import Enum
import random

#Program used to chose Champion for Game for my younger brother.

class Champion(Enum):
    Kled = 0
    Irelia = 1
    Fiora = 2
    Jax = 3
    Renekton = 4
    Ganplank = 5
    Temmo = 6
    Vladimir = 7
    Camile = 8
    Riven = 9
    Yasuo = 10

for x in range(1):
    x=random.randint(0,10)

print(Champion(x))
input()


print





