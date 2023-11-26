# Single Inheritance
class Animal:
    def __init__(self, species):
        self.species = species

    def display_species(self):
        print(f"Species is {self.species}")

class Dog(Animal):
    def __init__(self, species, breed):
        super().__init__(species)
        self.breed = breed

    def display_breed(self):
        print(f"Breed is {self.breed}")


# Multiple Inheritance
class Bird:
    def __init__(self, species):
        self.species = species

    def fly(self):
        print(f"{self.species} can fly")

class Penguin:
    def swim(self):
        print("Penguin can swim")

class FlyingPenguin(Bird, Penguin):
    def __init__(self, species):
        super().__init__(species)


# Multilevel Inheritance
class Vehicle:
    def __init__(self, brand):
        self.brand = brand

    def display_brand(self):
        print(f"This is a {self.brand} vehicle")

class Car(Vehicle):
    def __init__(self, brand, model):
        super().__init__(brand)
        self.model = model

    def display_model(self):
        print(f"This car belongs to the {self.model} model")

class SportsCar(Car):
    def __init__(self, brand, model, top_speed):
        super().__init__(brand, model)
        self.top_speed = top_speed

    def display_top_speed(self):
        print(f"The top speed of this sports car is {self.top_speed} mph")


# Eg. of Single Inheritance
dog = Dog("Canis", "Labrador")
dog.display_species()
dog.display_breed()

# Eg. of Multiple Inheritance
flying_penguin = FlyingPenguin("Flying Penguin")
flying_penguin.fly()
flying_penguin.swim()

# Eg. of Multilevel Inheritance
sports_car = SportsCar("Ferrari", "F458", 200)
sports_car.display_brand()
sports_car.display_model()
sports_car.display_top_speed()
