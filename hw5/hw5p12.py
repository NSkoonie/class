def averageStepsTaken():
    file = 'steps.txt'
    index = 0
    months = {
        "January"   : 31,
        "February"  : 28,
        "March"     : 31,
        "April"     : 30,
        "May"       : 31,
        "June"      : 30,
        "July"      : 31,
        "August"    : 31,
        "September" : 30,
        "October"   : 31,
        "November"  : 30,
        "December"  : 31}
    try:
        with open(file, 'r') as f:
            stepsStr = f.readlines()
    except FileNotFoundError:
        print("\"steps.txt\" not found.")
    else:
        stepsInt = [int(x.strip()) for x in stepsStr]
        for m in months:
            average = sum(stepsInt[index : index + months[m]]) / months[m]
            index = index + months[m]
            print("Average steps for {:10} {:.2f}".format(m + ':', average))    

averageStepsTaken()
