#lab6p6
#larger than n
#Noah Schoonover

def largerThanN(l, n):
    for val in l:
        if (type(val) == int) or (type(val) == float):
            if val > n:
                print(val)

list1 = [1, 2, 3, 4, 5, "j", 6, 7, 8]
n1 = 4

largerThanN(list1, n1)
