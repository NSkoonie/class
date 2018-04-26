#hw8p7
#Noah Schoonover

import pickle

employees = {}

#---------------------------------- Employee management functions

def listEmployees():
    for e in employees:
        print(employees[e])

def addEmployee():
    try:
        n = input('New employee name: ')
        i = int(input('New employee ID: '))
        d = input('New employee department: ')
        t = input('New employee title: ')
    except ValueError:
        print('ID must be digits only. Employee creation unsuccessful.')
    else:
        employees[i] = Employee(n, i, d, t) #adds employee without variable, key is object identifier
        
def delEmployee(employee):
    try:
        employee = int(employee)
    except ValueError:
        print('Employee ID must be digits only.')
    else:
        if employee in employees:
            del employees[employee]
        else:
            print('Employee not found.')

def search(query, quiet):
    if quiet:
        u = '2'
    else:
        u = input('Search by:\n'
              '1) Name\n'
              '2) ID Number\n'
              '3) Department\n'
              '4) Title\n\n'
              ': ').strip()
    
    if u == '1':
        f = False
        for e in employees:
            if query in employees[e].name:
                print(employees[e])
                f = True
                return True
        if not f:
            print('Name {} not found.'.format(query))
            return False

    elif u == '2':
        try:
            query = int(query)
        except ValueError:
            print('Employee ID must be digits only.')
            return False
        else:
            if query in employees:
                print(employees[query])
                return True
            else:
                print('Employee not found.')
                return False

    elif u == '3':
        f = False
        for e in employees:
            if query in employees[e].dept:
                print(employees[e])
                f = True
                return True
        if not f:
            print('Department {} not found.'.format(query))
            return False

    elif u == '4':
        f = False
        for e in employees:
            if query in employees[e].title:
                print(employees[e])
                f = True
                return True
        if not f:
            print('Title {} not found.'.format(query))
            return False
        
def editEmployee():
    e = input('Employee ID to edit: ')
    try:
        e = int(e)
    except ValueError:
        print('Employee ID must be digits only.')
    else:
        if search(e, True):
            u = input('Which do you want to edit?\n'
                      '1) Name\n'
                      '2) ID Number\n'
                      '3) Department\n'
                      '4) Title\n'
                      ': ').strip()
            
            if u == '1':
                employees[e].name = input('Enter new name: ')
            elif u == '2':
                try:
                    newID = int(input('Enter new ID: '))
                except ValueError:
                    print('Employee ID should be digits only.')
                else:
                    employees[e].idNum = newID      #set idNum var inside object
                    employees[newID] = employees[e] #copy employee to new ID
                    del employees[e]                #delete old employee 
                    
            elif u == '3':
                employees[e].dept = input('Enter new department: ')
            elif u == '4':
                employees[e].name = input('Enter new name: ')
            else:
                print('Enter digits 1-4 only.')

#---------------------------------- Exit Function

def dumpExit():
    with open('employees.dat', 'wb') as f:
        for e in employees:
            pickle.dump(employees[e], f)
    exit()

#---------------------------------- Menu Function

def menu():
    while True:
        i = input('\n1) Search Employee\n'
                  '2) Add Employee\n'
                  '3) Delete Employee\n'
                  '4) Edit Employee\n'
                  '5) List All Employees\n'
                  '6) Save and exit\n\n'
                  ': ').strip()
        
        if i == '1':
            search(input('Enter name, ID, department or title to search: ').strip() , False)
        elif i == '2':
            addEmployee()
        elif i == '3':
            delEmployee(input('Enter employee ID to delete: '))
        elif i == '4':
            editEmployee()
        elif i == '5':
            listEmployees()
        elif i == '6':
            dumpExit()

#---------------------------------- Employee Class

class Employee():

    def __init__(self, name, idNum, dept, title):
        self.name = name
        self.idNum = idNum
        self.dept = dept
        self.title = title

    def __str__(self):
        return('\t{}\n\t{}\n\t{}\n\t{}\n'.format(self.name, self.idNum, self.dept, self.title))

#---------------------------------- Employee Objects
    
#employees[47899] = Employee('Susan Meyers', 47899, 'Accounting', 'Vice President')
#employees[39119] = Employee('Mark Jones', 39119, 'IT', 'Programmer')
#employees[81774] = Employee('Joy Rogers', 81774, 'Manufacturing', 'Engineer')

#---------------------------------- Run

print('Employee Manager v1.01\n')

try:
    with open('employees.dat', 'rb') as f:
        end_of_file = False
        while not end_of_file:
            try:
                employee = pickle.load(f)
                employees[employee.idNum] = employee
            except EOFError:
                end_of_file = True
        print('Employee data loaded.')
            
except FileNotFoundError:
    print('file.dat not found, no employees loaded.')

menu()
