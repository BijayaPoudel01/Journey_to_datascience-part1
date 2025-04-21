# Create a class Student with the following attributes:
# name (string)
# age (integer)
# grade (float)
# Write a method display_details() to print the student's information.
class Student:
    def __init__(self):
        self.name="Bijaya"
        self.age=24
        self.grade=3.25
    def display_details(self):
        print(f"My name is {self.name}")
        print(f"My age is {self.age}")
        print(f"My grade is {self.grade}")
hi= Student()
hi.display_details()

# or,
class Student:
    def __init__(self,name,age,grade):
        self.name=name
        self.age=age
        self.grade=grade
    def display_details(self):
        print(f"My name is {self.name}")
        print(f"My age is {self.age}")
        print(f"My grade is {self.grade}")
hi= Student("bijaya",24,3.25)
hi.display_details()

# Create a class Car with the following attributes:
# brand (string)
# model (string)
# year (integer)
# Write a method show_info() to print the car’s details
class Car:
    def __init__(self,brand,model,year):
        self.brand=brand
        self.mod=model
        self.year=year
    def show_info(self):
        print(f"The brand is {self.brand}")
        print(f"The model is {self.mod}")
        print(f"The year is {self.year}")
hello=Car("BMW", "XYZ", 1920)
hello.show_info()

# Create a Python class called Book that has the following attributes:
# title (string)
# author (string)
# pages (integer)
# Write a method called display_info() that prints the book's title, author, and the number of pages.
class Book:
    def __init__(self,title,author,pages):
        self.ti=title
        self.aut=author
        self.pages=pages
    def display_info(self):
        print(f"The title of the book is {self.ti}")
        print(f"The author is {self.aut}")
        print(f"The pages is {self.pages}")
hello=Book("rich dad poor dad", "ABC", 560)
hello.display_info()

# Create a class BankAccount with the following attributes:
# account_holder (string)
# balance (float)
# Write a method deposit(amount) to add money to the balance and a method
#withdraw(amount) to subtract money from the balance.
# Also, create a method display_balance() to show the current
class BankAccount:
    def __init__(self,account_holder,balance):
        self.acc=account_holder
        self.bl=balance
    def deposit(self,amount):
        self.bl+=amount
        print(amount)
    def withdraw(self,amount):
        if amount<self.bl:
            self.bl-=amount
            print(amount)
        else:
            print("insufficient amount")
    def display_balance(self):
        print(self.acc)
        print(self.bl)
my_account=BankAccount("bijaya",500)
my_account.deposit(500)
my_account.withdraw(100)
my_account.display_balance()