#oop(object oriented programming)=code reuseability,code maintainability.
 #class and object
 #class syntax:
 #class ClassName:

#object syntax:
#object_name=classname()

#example:
class Student:
    def show(self):
        print("hello")
ram =Student()
ram.show()

#__init__ =dunder function or magic function
class Person:
    def __init__(self):
        print("hello")
ob=Person()

class Person:
    def __init__(self):
        self.a=12 #attributes
        self.b=45
    def show(self):
        print(f"my first value is {self.a} and my sec value is {self.b}")
ram= Person()
ram.show()

class Student:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def show(self):
        print(f"my name is {self.name} and my age is {self.age}")
ram=Student("bijaya",50)
ram.show()

class Student:
    def __init__(self):
        self.name="bijaya"
        self.age=50
    def show(self):
        print(f"my name is {self.name} and my age is {self.age}")
ram=Student()
ram.show()