#hw6p2
#Lottery Number Generator
#Noah Schoonover

from random import randint

num = [randint(0,9),
       randint(0,9),
       randint(0,9),
       randint(0,9),
       randint(0,9),
       randint(0,9),
       randint(0,9)]

print("The lottery numbers are:")
for x in num:
    print(x,' ', end='')
