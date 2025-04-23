#encapsulation:binding attributes (data)and methods of class in a single unit so that no onecan access from outside class.
#encapsulation is achieved by suing access modifier:public,private,protected.
#private means attributes and methods access only within class.

class Student:
    def __init__(self):
        self.__name="rita"
        self.__age=56
    def show(self):
        print(f"my name is{self.__name}and my ages is{self.__age}")
a=Student()
# print(a.__name)
# print(a.__age)
a.show()

#protected:attributes and methods access only within class and its subclass.
#single underscore is used.

class Student:
    def __init__(self):
        self._name="bijaya"
        self._age=20
    def show(self):
        print(f"my name is {self._name}and my age is{self._age}")
a=Student()
print(a._name)
print(a._age)

class B(Student):
    def __init__(self):
        print(a._name)
b=B()

#Abstraction:Hiding complex data or methods of class.
#showing relevant data and hiding irrelevant data.
from abc import ABC, abstractmethod
class A(ABC):
    @abstractmethod
    def show(self):
        pass
    def hello(self):
        print("hi niraj")
class B(A):
    def show(self):
        print("bye niraj")
b=B()
b.show()