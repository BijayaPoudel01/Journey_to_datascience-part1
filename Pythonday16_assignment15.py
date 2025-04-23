# Create a class Student with private attributes __name and __grade and a method to display them.
# Add getter and setter methods for __grade in Student, validating the grade to be between 0 and 100.

class Student:
    def __init__(self, name, grade):
        self.__name = name
        self.__grade = None
        self.set_grade(grade)

    def display(self):
        print(f"Name: {self.__name}, Grade: {self.__grade}")

    def get_grade(self):
        return self.__grade

    def set_grade(self, grade):
        if 0 <= grade <= 100:
            self.__grade = grade
        else:
            print("Invalid grade. Must be between 0 and 100.")
s1 = Student("Bijaya", 85)
s1.display()

s1.set_grade(105)
s1.set_grade(95)
print(s1.get_grade())


# Create a class BankAccount with private __balance, and methods deposit(), withdraw(), and get_balance().
# Try accessing __balance directly from an object and observe the result
class BankAccount:
    def __init__(self, initial_balance):
        self.__balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited: {amount}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrawn: {amount}")
        else:
            print("Invalid amount or insufficient balance.")

    def get_balance(self):
        return self.__balance

acc = BankAccount(1000)

acc.deposit(500)
acc.withdraw(300)
print(acc.get_balance())

# Make a class Laptop with private __brand, __price, and ensure price cannot be negative.
class Laptop:
    def __init__(self,brand,price):
        self.__brand=brand
        self.__price=price
    def show(self):
        if self.__price>0:
            print(f"The brand is {self.__brand}and the price is {self.__price}")
        else:
            print("the price cannot be negative")
ob=Laptop("acer", 6000)
ob.show()
# Create an abstract class Shape with an abstract method area() and a concrete method describe().
# Inherit Shape in Circle and implement area() using radius passed in the constructor.
# Create another subclass Rectangle from Shape with attributes length and width, and implement area().
from abc import ABC, abstractmethod  # Importing abstract base class tools

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass  # Subclasses must override this

    def describe(self):
        print("This is a shape.")  # A regular method that works for all shapes


# Circle subclass
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14159 * self.radius * self.radius


# Rectangle subclass
class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width
c = Circle(5)
c.describe()                       # Output: This is a shape.
print("Circle Area:", c.area())    # Output: Circle Area: 78.53975

r = Rectangle(4, 6)
r.describe()                       # Output: This is a shape.
print("Rectangle Area:", r.area()) # Output: Rectangle Area: 24


# Create an abstract class Vehicle with an abstract method start_engine() and implement it in Car and Motorbike

# a=["ram"]
# a=["shyam"]
a=["hari"]
a[0]="bijaya"
print(a)

a="hari"
b=a.replace("hari","biju")
print(b)