class Human:
    def __init__(self, name, birth_year):
        self.name = name
        self.birth_year = birth_year

    def display_info(self):
        age = 2023 - self.birth_year
        print("Name: ", self.name)
        print("Age: ", age)

    def is_adult(self):
        age = 2023 - self.birth_year
        if age >= 18:
            print(self.name, "is adult")
        else:
            print(self.name, "is not adult")


person1 = Human("Irina", 2005)
person1.display_info()
person1.is_adult()
person2 = Human("Nikita", 2009)
person2.display_info()
person2.is_adult()
