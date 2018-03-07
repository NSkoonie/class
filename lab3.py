import math

def salesPrediction():
    sales = input("Projected Sales: $")
    try:
        sales = float(sales)
        profit = sales * .23
        print("Projected Profit: $" + str(profit))
    except ValueError:
        print("You must input an integer or float.")

def landCalculation():
    sqFeet = input("Square Feet: ")
    try:
        sqFeet = float(sqFeet)
        acres = sqFeet / 43560
        print("Acres:", acres)
    except ValueError:
        print("You must input an integer or float.")

def distanceTraveled():
    print("A car traveling 70 mph will go:")
    d = 70 * 6
    print(d, "miles in 6 hours,")
    d = 70 * 10
    print(d, "miles in 10 hours,")
    d = 70 * 15
    print("and", d, "miles in 15 hours.")

def tipTaxTotal():
    m = input("Meal total: $")
    try:
        m = float(m)
        tip = m * .18
        tax = m * .07
        total = m + tip + tax
        print("Meal:", m)
        print("Tip:", tip)
        print("Tax:", tax)
        print("\nTOTAL:", total)
    except ValueError:
        print("You have to input an integer or float.")

def ingredientAdjuster():
    n = input("How many cookies do you want to make? ")
    try:
        n = int(n)
        ratio = n / 48
        sugar = 1.5 * ratio
        butter = 1 * ratio
        flour = 2.75 * ratio
        print("For", n, "cookies:")
        print("Sugar:", str(round(sugar,2)), "cups")
        print("Butter:", str(round(butter,2)), "cups")
        print("Flour:", str(round(flour,2)), "cups")
        
    except ValueError:
        print("Only whole numbers of cookies, please.")

def plantingGrapevines():
    r = input("Length of row in feet: ")
    e = input("Space of endpost in feet: ")
    s = input("Space between vines in feet: ")
    try:
        r = float(r)
        e = float(e)
        s = float(s)
        v = (r - 2 * e) / s
        print("Number of grapevines per row:", math.floor(v))
    except ValueError:
        print("Integer or float only.")
    
    
while True:
    u = input("""
Pick an exercise.

1) Exercise 2: Sales Prediction
2) Exercise 3: Land Calculation
3) Exercise 5: Distance Traveled
4) Exercise 8: Tip, Tax, and Total
5) Exercise 10: Ingredient Adjuster
6) Exercise 13: Planting Grapevines

:""")

    if u == "1":
        salesPrediction()
    elif u == "2":
        landCalculation()
    elif u == "3":
        distanceTraveled()
    elif u == "4":
        tipTaxTotal()
    elif u == "5":
        ingredientAdjuster()
    elif u == "6":
        plantingGrapevines()
    else:
        print("You have to enter a number. 1-6.")
