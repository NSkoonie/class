#hw9p3
#Person and Customer classes
#Noah Schoonover

#---------------------------------------- Person Class

class Person():
    def __init__(self, name, address, phone):
        self.name = name
        self.address = address
        self.phone = phone

    def __str__(self):
        return('\t{}\n\t{}\n\t{}'.format(self.name, self.address, self.phone))

#---------------------------------------- Customer Class

class Customer(Person):
    def __init__(self, name, address, phone, customerNum, mail):
        super().__init__(name, address, phone)
        self.customerNum = customerNum
        self.mail = mail

    def __str__(self):
        return(super().__str__() + '\n\t{}\n\t{}'.format(self.customerNum, self.mail))

#---------------------------------------- Test Objects

people = []
people.append(Person('Noah Schoonover', '42 Hey St', '575-444-8423'))
people.append(Customer('Steve Jobs', 'Apple Blvd', '555-555-5555', 12345, True))

for person in people:
    print(person, '\n')
