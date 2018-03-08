#lab6p9
#Population Data
#Noah Schoonover

file = 'USPopulation.txt'
    
def populationData(p):
    firstYear = 1950
    p = [int(x.strip()) for x in p]
    average = sum(p) / len(p)
    
    smallestDif = p[1] - p[0]
    largestDif = p[1] - p[0]
    smallestYear = 0
    largestYear = 0
    
    for x in range(len(p) - 1):
        dif = p[x+1] - p[x]
        if dif  < smallestDif:
            smallestDif = dif
            smallestYear = firstYear + x
        if dif > largestDif:
            largestDif = dif
            largestYear = firstYear + x
            
    print("The average population from 1950 to 1990 was approx. {:,.0f}".format(average*1000))
    print(smallestYear, "is the year with the smallest population increase.")
    print(largestYear, "is the year with the largest population increase.")
    
try:
    with open(file, 'r') as f:
        popData = f.readlines()
except FileNotFoundError:
    print("USPopulation.txt not found.")
else:
    populationData(popData)
