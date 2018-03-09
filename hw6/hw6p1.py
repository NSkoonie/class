#hw6p1
#Total Sales
#Noah Schoonover

print("Enter store's sales for the week.")
sales = [input("Monday: "),
         input("Tuesday: "),
         input("Wednesday: "),
         input("Thursday: "),
         input("Friday: "),
         input("Saturday: "),
         input("Sunday: ")]

sales = [x.replace('$','') for x in sales]
try:
    sales = [float(x.strip()) for x in sales]
except ValueError:
    print("Sales must be integers or floats.")
else:
    print("The total of this week's sales is:", sum(sales))
    
