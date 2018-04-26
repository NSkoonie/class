#hw8p3
#Noah Schoonover

class Information():

    def __init__(self, name, address, age, phone_number):
        self.name = name
        self.address = address
        self.age = age
        self.phone_number = phone_number

    def get_name(self):
        return self.name
    
    def get_address(self):
        return self.address

    def get_age(self):
        return self.age

    def get_phone_number(self):
        return self.phone_number

    def set_name(self, name):
        self.name = name

    def set_address(self, address):
        self.address = address

    def set_age(self, age):
        self.age = age

    def set_phone_number(self, phone_number):
        self.phone_number = phone_number


me = Information('Noah Schoonover', '42 Pasta Place', 18, '877-CAS-HNOW')
friend1 = Information('Brian Jenkins', 'Boonies', 42, '123-234-3455')
friend2 = Information('Ethan Antonez', 'Out West', 5, '333-333-3333')
