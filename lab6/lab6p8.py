#lab6p8
#name search
#Noah Schoonover

def nameSearch(girlNames, boyNames):
    girlNames = [x.strip() for x in girlNames]
    boyNames = [x.strip() for x in boyNames]

    search = input("Search for a name: ").strip()
    
    if search in girlNames and search in boyNames:
        print(search + " is a popular name for boys and girls!")
    elif search in girlNames:
        print(search + " is a popular name for girls!")
    elif search in boyNames:
        print(search + " is a popular name for boys!")
    else:
        print(search + " is not a popular name.")
        
try:
    with open('GirlNames.txt', 'r') as f:
        g = f.readlines()
    with open('BoyNames.txt', 'r') as f:
        b = f.readlines()
except FileNotFoundError:
    print("GirlNames.txt and/or BoyNames.txt not found.")
else:
    while True:
        nameSearch(g, b)
