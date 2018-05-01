#hw9p2
#ShiftSupervisor Class
#Noah Schoonover

#---------------------------------------- Employee Class

class Employee():
    def __init__(self, name, idNum):
        self.name = name
        self.idNum = idNum
    def __str__(self):
        return('\t{}\n\t{}'.format(self.name, self.idNum))


#---------------------------------------- ShiftSupervisor Class

class ShiftSupervisor(Employee):
    def __init__(self, name, idNum, salary, bonus):
        super().__init__(name, idNum)
        self.salary = salary
        self.bonus = bonus
    def __str__(self):
        return(super().__str__() + '\n\t{}\n\t{}'.format(self.salary, self.bonus))

#---------------------------------------- Test objects

employees = []
employees.append(Employee('Elon Musk', 12345))
employees.append(ShiftSupervisor('Noah Schoonover', 54321, 110000, 8000))

for employee in employees:
    print(employee, '\n')
