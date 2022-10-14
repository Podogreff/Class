class Cat():
    breed = "pers"

    def set_value(self, value, age=0):
        self.name = value
        self.age = age

    def __int__(self, name, breed, age, colour):
        print("hello new object is", self, name, breed, age, colour)
