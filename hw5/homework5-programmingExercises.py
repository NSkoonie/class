#homework 5
#Even numbers problems in chapter 6: 4, 6, 8, 10, 12
#Noah Schoonover

from random import randint

def itemCounter():
    file = 'names.txt'
    x = 0
    try:
        with open(file, 'r') as f:
            for line in f:
                x = x + 1
    except FileNotFoundError:
        print("names.txt not found.")
    else:
        print("There are {} names in names.txt.".format(x))

def averageOfNumbers():
    file = 'numbers.txt'
    try:
        with open(file, 'r') as f:
            numbers = f.readlines()
    except FileNotFoundError:
        print("numbers.txt not found.")
    else:
        try:
            numbers = [int(x.strip()) for x in numbers]
            average =  sum(numbers) / len(numbers)
        except TypeError:
            print("Invalid values in numbers.txt")
        else:
            print("The average of the numbers in numbers.txt is {}".format(average))

def randomNumberFileWriter():
    file = 'randomNumbers.txt'
    try:
        count = int(input("How many random numbers do you want? "))
    except ValueError:
        print("Only whole numbers.")
    with open(file, 'w') as f:
        for x in range(count):
            r = randint(0,500)
            f.write("{}\n".format(r))

def randomNumberFileReader():
    file = 'randomNumbers.txt'
    try:
        with open(file, 'r') as f:
            numbers = f.readlines()
    except FileNotFoundError:
        print("randomNumbers.txt not found.")
    else:
        try:
            numbers = [int(x.strip()) for x in numbers]
        except ValueError:
            print("Invalid values in randomNumbers.txt")
        else:
            print("There were {} numbers in the file.\nThe sum of the numbers is {}".format(len(numbers), sum(numbers)))

def golfScores():
    file = 'golf.txt'
    do = input("Read or write to file? (r or w): ").lower()
    if do == "w":
        with open(file, 'w') as f:
            try:
                num = int(input("How many records would you like to enter? "))
            except ValueError:
                print("Invalid entry.")
            else:
                for x in range(num):
                    name = input("Name: ")
                    score = input("Score: ")
                    f.write(name + "\n")
                    f.write(score + "\n")
                    print()
    elif do == "r":
        try:
            with open(file, 'r') as f:
                n = f.readline().strip()
                while n != '':
                    s = f.readline().strip()
                    print("Name:", n)
                    print("Score:", s)
                    print()
                    n = f.readline().strip()
                    
        except FileNotFoundError:
            print("golf.txt does not exist. Try writing to file first.")

    else:
        print("Input 'r' or 'w' only.")

def averageStepsTaken():
    file = 'steps.txt'
    index = 0
    z = 0
    months = [
        "January",
        "February",
        "March",
        "April",
        "May",
        "June",
        "July",
        "August",
        "September",
        "October",
        "November",
        "December"]
    daysPerMonth = [
        31, #Jan
        28, #Feb
        31, #Mar
        30, #Apr
        31, #May
        30, #Jun
        31, #Jul
        31, #Aug
        30, #Sep
        31, #Oct
        30, #Nov
        31] #Dec
    try:
        with open(file, 'r') as f:
            stepsStr = f.readlines()
    except FileNotFoundError:
        print("File not found.")
    else:
        stepsInt = [int(x.strip()) for x in stepsStr]
        for month in daysPerMonth:
            average = sum(stepsInt[index : index + month]) / month
            index = index + month
            print("Average steps for {}: {:.2f}".format(months[z], average))    
            z = z + 1
            
while True:
    print("""\n\nWhich exercise do you want to see?
        1) Item Counter
        2) Average Of Numbers
        3) Random Number File Writer
        4) Random Number File Reader
        5) Golf Scores
        6) Average Steps Taken""")
    i = input(": ")
    print("\n\n")
    if i == '1':
        itemCounter()
    elif i == '2':
        averageOfNumbers()
    elif i == '3':
        randomNumberFileWriter()
    elif i == '4':
        randomNumberFileReader()
    elif i == '5':
        golfScores()
    elif i == '6':
        averageStepsTaken()
    else:
        print("Error. 1 - 6 only.")
