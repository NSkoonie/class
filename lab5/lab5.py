#Lab 5
#Programming Exercises in Chapter 6: odd exercises: 5, 9, 11
#Noah Schoonover

def sumOfNumbers():
    file = 'numbers.txt'

    try:
        with open(file, 'r') as f:
            numbers = f.readlines()
    except FileNotFoundError:
        print("numbers.txt does not exist")
    else:
        try:
            numbers = [float(x.strip()) for x in numbers]
        except ValueError:
            print("invalid values in numbers.txt")
        else:
            print("sum of numbers: ", sum(numbers))

def exceptionHandling():
    try:
        sumOfNumbers()
    except:
        print("an error occurred")

def personalWebPage():
    file = 'webPage.html'
    name = input("Enter your name: ")
    description = input("Describe yourself: ")
    with open(file, 'w') as f:
        f.write("""
            <html>
            <head>
            </head>
            <body>
                <center>
                <h1>{}</h1>
                </center>
                <hr/>
                {}
                <hr/>
            </body>
            </html>""".format(name, description))
        
while True:
    print("""Which exercise do you want to see?
        1) Sum of Numbers
        2) Exception Handling
        3) Personal Web Page""")
    k = input(": ")
    if k == '1':
        sumOfNumbers()
    elif k == '2':
        exceptionHandling()
    elif k == '3':
        personalWebPage()
