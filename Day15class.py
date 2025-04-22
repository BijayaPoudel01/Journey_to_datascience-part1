#fundamentals of oop
#1.Inheritance:class that inherits another class and share all attributes and methods.
#1.single inheritance:
class A:
    def single(self):
        print("i am single")
class B(A):
    def double(self):
        print("i am double")
ob=B()
ob.single()
ob.double()

#2.multilevel
class A:
    def single(self):
        print("i am single")
class B(A):
    def double(self):
        print("i am double")
class C(B):
    def triple(self):
        print("i am triple")
ob=C()
ob.single()
ob.double()
ob.triple()

#3.multiple:
class A:
    def single(self):
        print("i am single")
class B:
    def double(self):
        print("i am double")
class C(A,B):
    def triple(self):
        print("i am triple")
ob=C()
ob.single()
ob.double()
ob.triple()

#4.Hierarchical:
class A:
    def single(self):
        print("i am single")
class B(A):
    def double(self):
        print("i am double")
class C(A):
    def triple(self):
        print("i am triple")
ob=B()
ob.single()
ob.double()
ob=C()
ob.triple()

#5. Hybrid Inheritance: combination of all.
class A:
    def single(self):
        print("i am single")
class B(A):
    def double(self):
        print("i am double")
class C(B):
    def triple(self):
        print("i am triple")
class D():
    def fourth(self):
        print("i am four")
class E(D,C):
    def five(self):
        print("i am five")
class F(D):
    def sixth(self):
        print("i am six")
class G(D):
    def seven(self):
        print("i am seven")
ob=E()
ob.fourth()
ob.double()
ob.triple()
ob.single()
ob.five()
ob=F()
ob.sixth()
ob=G()
ob.seven()

#Polymorphism:one thing behave in different way.
class MyClass:
    def show(self):
        print("hello sipalaya")
    def show(self,a,b):
        print(a+b)
ram=MyClass()
ram.show(4,5)


#method overiding:
class A:
    def show(self):
        print("i am parent class")
class B(A):
    def show(self):
        super().show()
        print("i am child class")
ob=B()
ob.show()

#super()=method that access parent class method.
#operator overloading:
class MyClass:
    def __init__(self,a):
        self.a=a
    def __add__(self,other):
        return self.a + other.b
class YourClass:
    def __init__(self,b):
        self.b=b
a=MyClass(5)
b=YourClass(8)
print(a+b)
