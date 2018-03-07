#Lab 4
#Noah Schoonover

def dayOfTheWeek():
    u = input("Input a number 1-7: ")
    if u == "1":
        print("MONDAY")
    elif u == "2":
        print("TUESDAY")
    elif u == "3":
        print("WEDNESDAY")
    elif u == "4":
        print("THURSDAY")
    elif u == "5":
        print("FRIDAY")
    elif u == "6":
        print("SATURDAY")
    elif u == "7":
        print("SUNDAY")
    else:
        print("only 1-7")

def massAndWeight():
    m = input("Mass of object: ")
    try:
        m = float(m)
        w = m * 9.8
        print("Weight of object:", w, "N")
        if w < 100:
            print("The object is too light.")
        if w > 500:
            print("The object is too heavy.")
    except ValueError:
        print("Only numbers.")

def rouletteWheelColors():
    c = input("Pocket number (0-36): ")
    if c == "0":
        color = "green"
        print(color)
    else:
        try:
            c = int(c)
            
            if (c >= 1 and c <= 10) or (c >= 19 and c <= 28):
                if c % 2 == 0:
                    color = "black"
                else:
                    color = "red"
            if (c >= 11 and c <= 18) or (c >=29 and c <= 36):
                if c % 2 == 0:
                    color = "red"
                else:
                    color = "black"
            else:
                color = "error. 1-36 only."

            print(color)
        
        except ValueError:
            print("error. 1-36 only.")

def februaryDays():
    y = input("Enter a year: ")
    leapYear = False
    
    try:
        y = int(y)
        if y % 100 == 0:
            if y % 400 == 0:
                leapYear = True
        else:
            if y % 4 == 0:
                leapYear = True

        if leapYear:
            print("In", y, "February has 29 days.")
        else:
            print("In", y, "February has 28 days.")
            
    except ValueError:
        print("Only whole numbers.")
    

while True:
    print("""

Which exercise do you want to see?
1) Exercise 1: Day of the Week
2) Exercise 5: Mass and Weight
3) Exercise 9: Roulette Wheel Colors
4) Exercise 16: February Days

""")
    
    u = input(": ")
    if u == "1":
        dayOfTheWeek()
    elif u == "2":
        massAndWeight()
    elif u == "3":
        rouletteWheelColors()
    elif u == "4":
        februaryDays()
    else: #if user enters something stupid
        print("1-4")
