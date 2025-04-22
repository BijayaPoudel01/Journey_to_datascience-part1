# Create a base class Animal with attributes name and sound.
# Add a method make_sound() that prints the sound of the animal.
class Animal:
    def __init__(self,name,sound):
        self.name=name
        self.sound=sound

    def make_sound(self):
        print(f"the sound of {self.name} is {self.sound}")

dog = Animal("Dog", "Bark")
dog.make_sound()

cat = Animal("Cat", "Meow")
cat.make_sound()

# Multi-level Inheritance:
# Create a base class Vehicle with attributes brand and fuel_type.
# Create a subclass Car that inherits from Vehicle and adds an attribute num_wheels = 4.
# Create another subclass ElectricCar that inherits from Car and overrides the fuel_type to "Electric".
class Vehicle:
    def  __init__(self,brand,fuel_type):
        self.brand=brand
        self.fuel_type=fuel_type

class Car(Vehicle):
    def __init__(self,brand,fuel_type):
        super().__init__(brand,fuel_type)
        self.num_wheels = 4

class ElectricCar(Car):
    def __init__(self, brand):
        super().__init__(brand, fuel_type="Electric")
tesla = ElectricCar("Tesla")
print(f"Brand: {tesla.brand}")
print(f"Fuel Type: {tesla.fuel_type}")
print(f"Number of Wheels: {tesla.num_wheels}")

# Multiple Inheritance:
# Create two classes, Swimmer (with a method swim()) and Flyer (with a method fly()).
# Create a class Duck that inherits from both Swimmer and Flyer. Implement a method quack() in the Duck class
class Swimmer:
    def swimmer(self):
        print("i can swim")
class Flyer:
    def fly(self):
        print("i can fly")

class Duck(Swimmer,Flyer):
    def quack(self):
        print("Quack, Quack")

d=Duck()
d.quack()
d.swimmer()
d.fly()

# Create a base class Shape with a method area() that returns 0.
# Create subclasses Circle and Rectangle that override the area() method to calculate and return the area of the respective shape.
# Write a function print_area(shape) that accepts any Shape object and prints its area.
class Shape:
    def area(self):
        return 0
class Circle(Shape):
    def __init__(self, r):
        self.r = r
    def area(self):
        return 3.14 * (self.r ** 2)

class Rectangle(Shape):
    def __init__(self, l, b):
        self.l = l
        self.b = b

    def area(self):
        return self.l * self.b

def print_area(shape):
    print(f"Area: {shape.area()}")


c = Circle(5)
r = Rectangle(4, 6)

print_area(c)
print_area(r)

# Create two classes, Car and Bicycle, each with a method start().
# Write a function start_vehicle(vehicle) that accepts any object with a start() method and calls it.
# Demonstrate duck typing by passing instances of Car and Bicycle to the start_vehicle() function.
# Class Car
class Car:
    def start(self):
        print("Car engine started")

class Bicycle:
    def start(self):
        print("Bicycle ride started ")

def start_vehicle(vehicle):
    vehicle.start()
my_car = Car()
my_bike = Bicycle()
start_vehicle(my_car)
start_vehicle(my_bike)
