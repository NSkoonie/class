#Homework 3
#Noah Schoonover

def personalInformation():
    print("Noah Schoonover \
\n11 Caviness W Rd\
\nRaton, NM 87740\
\n(575) 447-8342\
\nI'm still in high school but I plan to major in Mechanical Engineering.")

def milesPerGallon():
    m = input("Miles driven: ")
    g = input("Gallons of gas used: ")
    try:
        m = float(m)
        g = float(g)
        mpg = m / g
        print("Miles per gallon:", mpg)
    except ValueError:
        print("Only numbers.")

def celsiusToFahrenheit():
    c = input("Temp in celsius: ")
    try:
        c = float(c)
        f = (9 / 5) * c + 32
        print("Temp in fahrenheit:", f)
    except ValueError:
        print("Only numbers.")

def stockTransaction():
    a = 40.00 * 2000
    print("Joe paid $", a, "for the stock.")
    b = a * .03
    print("Joe paid $", b, "to his stockbroker.")
    x = -a - -b
    print("Joe had $", x)
    c = 42.75 * 2000
    print("Joe sold the stock for $", c)
    d = c * .03
    print("Joe paid $", d, "to his stockbroker.")
    x = x + c + d
    print("Joe has $", x)
    print("Good job Joe.")

def compoundInterest():
    print("This program calculates compounded interest.")
    p = input("Principal deposit: ")
    r = input("Interest rate: ")
    n = input("Annual compoundings: ")
    t = input("Years: ")
    try:
        p = float(p)
        r = float(r)
        n = int(n)
        t = float(t)
        a = p * ((1 + (r / n)) ** (n * t))
        print("Amount:", a)
    except ValueError:
        print("Only numbers. Annual compoundings must be whole.")
    

while True:
    print("""

Which exercise do you want to see?
1) Exercise 1: Personal Information
2) Exercise 7: Miles-per-Gallon
3) Exercise 9: Celsius to Fahrenheit Temperature Converter
4) Exercise 12: Stock Transaction Program
5) Exercise 14: Compound Interest

""")
    
    u = input(": ")
    if u == "1":
        personalInformation()
    elif u == "2":
        milesPerGallon()
    elif u == "3":
        celsiusToFahrenheit()
    elif u == "4":
        stockTransaction()
    else: #even if user enters something stupid
        compoundInterest()
