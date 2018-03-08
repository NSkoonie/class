#lab6p12
#Prime Number Generation
#Noah Schoonover

def isPrime(num):
    for x in range(2, int(num**.5)+1):
        if num % x == 0:
            return False
    return True   

def getPrimes(r):
    print("The prime numbers between from 2 to {} are:".format(r))
    nums = range(2,r+1)
    for x in nums:
        if isPrime(x):
            print(x)

while True:
    r = input("Up to what range (>1) do you want the primes for? ").strip()
    try:
        r = int(r)
    except ValueError:
        print("Range can be whole numbers only.")
    else:
        if r > 1:
            getPrimes(r)
        else:
            print("Range must be greater than 1.")
