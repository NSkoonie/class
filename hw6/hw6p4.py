#hw6p4
#Number Analysis Program
#Noah Schoonover

print("Input 20 numbers.")
numbers = []

for x in range(20):
    numbers.append(input(": "))

try:
    numbers = [float(x.strip()) for x in numbers]
except ValueError:
    print("Numbers must be numbers")
else:
    lowest = min(numbers)
    highest = max(numbers)
    total = sum(numbers)
    average = total / len(numbers)
    print("Highest:", highest)
    print("Lowest:", lowest)
    print("Total:", total)
    print("Average:", round(average,2))
    
