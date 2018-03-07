#This program calculates area and perimeter or slope and angle based on user input.
#Written by Noah Schoonover

import math

def getWidthAndHeight(): #asks user for width and height
    gotNumbers = False
    while not gotNumbers:
        userWidth = input("\n\n\twidth: ")
        userHeight = input("\theight: ")
        try: #attempts to convert user answers, catches exceptions
            width = float(userWidth)
            height = float(userHeight)
            gotNumbers = True
            calculateAreaAndPerimeter(width, height)
        except ValueError:
            print("\nEntries must be integers or floats.")

def calculateAreaAndPerimeter(w, h): #calculates area and perimter
    print("\n\tArea:", (w * h))
    print("\tPerimeter:", (2 * (w + h)))
    print("\n")

def getCoords(): #asks user for coordinate points
    gotNumbers = False
    while not gotNumbers:
        userX1 = input("\n\n\tx1: ")
        userY1 = input("\ty1: ")
        userX2 = input("\tx2: ")
        userY2 = input("\ty2: ")
        try: #attempts to convert user answers, catches exceptions
            x1 = float(userX1)
            y1 = float(userY1)
            x2 = float(userX2)
            y2 = float(userY2)
            gotNumbers = True
            calculateSlopeAndAngle(x1, y1, x2, y2)
        except ValueError:
            print("\nEntries must be integers or floats.")

def calculateSlopeAndAngle(x1, y1, x2, y2):
    try:
        slope = ((y2 - y1)/(x2 - x1))
        angle = math.degrees(math.atan(slope)) #calculates tan-1 and casts to degrees
        print("\n\tSlope:", slope)
        print("\tAngle:", angle)
    except ZeroDivisionError: #catches division by zero
        print("\n\tThe slope is infinite!")
    print("\n")
        
while True: #repeats forever
    print("Would you like to calculate:\n1. area and perimeter\nOR\n2. slope and angle?")
    userAnswer = input("""Type '1' or '2': """)
    if userAnswer == "1":
        getWidthAndHeight()
    elif userAnswer == "2":
        getCoords()
