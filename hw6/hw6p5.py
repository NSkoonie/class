#hw6p5
#Charge Account Validation
#Noah Schoonover

file = 'charge_accounts.txt'

def searchNumber(a):
    num = input("Search for a charge account number: ").strip()
    if num in a:
        print("The number you searched is a valid account.")
    else:
        print("The number you searched is not a valid account.")

try:
    with open(file, 'r') as f:
        accts = f.readlines()
except FileNotFoundError:
    print("charge_accounts.txt not found.")
else:
    accts = [x.strip() for x in accts]
    searchNumber(accts)
