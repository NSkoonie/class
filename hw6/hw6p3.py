#hw6p3
#Rainfall Statistics
#Noah Schoonover

def calculateData(r):
    total = sum(r.values())
    average = total / len(r)
    lowest = "January"
    highest = "January"
    for month in r:
        if r[month] < r[lowest]:
            lowest = month
        if r[month] > r[highest]:
            highest = month
    print("Total rainfall:", total)
    print("Average rainfall:", round(average,2))
    print("{} had the most rainfall, with {} units of rain.".format(highest, r[highest]))
    print("{} had the least rainfall, with {} units of rain.".format(lowest, r[lowest]))

print("Enter the total rainfall for each month.")
rainfall = {
        "January" : input("January: "),
        "February" : input("February: "),
        "March" : input("March: "),
        "April" : input("April: "),
        "May" : input("May: "),
        "June" : input("June: "),
        "July" : input("July: "),
        "August" : input("August: "),
        "September" : input("September: "),
        "October" : input("October: "),
        "November" : input("November: "),
        "December" : input("December: ")
        }

for x in rainfall:
    if rainfall[x] == '':
        rainfall[x] = 0
        
try:
    for x in rainfall:
        rainfall[x] = float(rainfall[x])
except ValueError:
    print("Rainfall must be integers or floats.")
else:
    calculateData(rainfall)
    
