#lab6p10
#World Series Champions
#Noah Schoonover

file = 'WorldSeriesWinners.txt'

def searchTeam(w):
    w = [x.strip() for x in w]
    search = input("Search for a World Series winning team: ").strip()
    if search in w:
        x = 0
        for winner in w:
            if winner == search:
                x += 1
        if x > 1:
            print("That team has won the World Series {} times.".format(x))
        else:
            print("That team has won the World Series {} time.".format(x))
    else:
        print("That team has never won the World Series.")
    

try:
    with open(file, 'r') as f:
        winners = f.readlines()
except FileNotFoundError:
    print("WorldSeriesWinners.txt not found.")
else:
    while True:
        searchTeam(winners)
