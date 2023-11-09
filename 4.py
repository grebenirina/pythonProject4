from datetime import date


class Dog:
    def __init__(self, name, age, level_of_food):
        self.name = name
        self.age = age
        self.level_of_food = level_of_food

    def feed_dog(self):
        while self.level_of_food < 5:
            self.level_of_food = self.level_of_food + 1
            print(f"{self.name} кушает")
        print(f"Уровень еды {self.name} полон")

    @classmethod
    def from_birth_year(cls, name, year, level_of_food):
        return cls(name, date.today().year - year, level_of_food)

    @staticmethod
    def is_hungry(level_of_food):
        return level_of_food < 5


dog1 = Dog("Марк", 5, 3)
dog2 = Dog("Рич", 3, 5)
dog3 = Dog.from_birth_year("Пур", 2021, 4)
dog1.feed_dog()
dog2.feed_dog()
Dog.is_hungry(2)

