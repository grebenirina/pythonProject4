class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self, new_speed):
        print(self.name, "poehala")
        self.speed = new_speed

    def stop(self):
        print(self.name, "ostanovilas")
        self.speed = 0

    def turn(self, direction):
        print(self.name, "povernula", direction)

    def show_speed(self):
        print(f"The current speed of the {self.color} {self.name} is {self.speed} km/h.")


class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            print("Previshenie skorosti!!!")
        else:
            print("Skorost ne previshina")


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            print("Previshenie skorosti!!!")
        else:
            print("Skorost ne previshina")


class PoliceCar(Car):
    pass


car1 = TownCar(70, "blue", "Toyota", False)
car1.show_speed()
car1.go(50)
car1.show_speed()
car1.turn("left")
car1.stop()

car2 = SportCar(100, "red", "Ferrari", False)
car2.show_speed()
car2.turn("right")
car2.stop()
car2.show_speed()
