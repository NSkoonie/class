#hw8p1
#Noah Schoonover

class Pet():

    def __init__(self):
        self.__name = ''
        self.__animal_type = ''
        self.__age = int()

    def set_name(self, name):
        self.__name = name

    def set_animal_type(self, animal_type):
        self.__animal_type = animal_type

    def set_age(self, age):
        self.__age = age

    def get_name(self):
        return self.__name

    def get_animal_type(self):
        return self.__animal_type

    def get_age(self):
        return self.__age

newPet = Pet()
newPet.set_name(input('Name your new pet: '))
newPet.set_animal_type(input('What is the type of your animal? '))
newPet.set_age(input('How old is your animal? '))
