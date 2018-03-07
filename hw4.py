#Homework 4
#Noah Schoonover

def distanceTraveled():
    mph = input("What is the speed of the vehicle in mph? ")
    hours = input("How many hours has it traveled? ")
    try:
        mph = int(mph)
        hours = int(hours)
        print("Hours\tDistance")
        for x in range(1, hours):
            distance = mph * x
            print(x, '\t', distance)
    except ValueError:
        print("Only whole numbers.")
    

def population():
    num = input("Starting number of organisms: ")
    increase = input("Average daily increase: ")
    days = input("Number of days to multiply: ")
    try:
        num = int(num)
        increase = int(increase)
        days = int(days)
        percent = increase / 100
        print("Day\tPopulation")
        print("1\t", num)
        for x in range(2, days + 1):
            num = num + num * percent
            print(x, '\t', round(num, 2))
    except ValueError:
        print("Only whole numbers.")

def drawPattern1():
    size = 7
    k = size
    for x in range(size):
        for x in range(k):
            print('*', end='')
        print()
        k = k - 1

def drawPattern2():
    size = 7
    for x in range(size):
        print('#', end='')
        for k in range(x):
            print(' ', end='')
        print('#', end='')
        print()

while True:
    print("""

Which exercise do you want to see?
1) Exercise 4: Distance Traveled
2) Exercise 13: Population
3) Exercise 14: Draw Pattern 1
4) Exercise 16: Draw Pattern 2

""")
    
    u = input(": ")
    if u == "1":
        distanceTraveled()
    elif u == "2":
        population()
    elif u == "3":
        drawPattern1()
    elif u == "4":
        drawPattern2()
    else: #if user enters something stupid
        print("1-4")
