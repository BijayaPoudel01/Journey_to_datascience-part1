#functions:It is a block of code that is executed whenever it is called.
# two types:in built function, user defined function.
#1) print(), len(), list(), max()
print(max(-1.0,1))

#2)user defined=user itself should define,syntax:
# def function_name():
#block of code
# function_name()  #function calling

def show():
    print("hello")
show()

def sum():
    a=3
    b=4
    print(a+b)
sum()

#argument:formal(variable) and actual(values).
# def show(formal_argument):
#     #block of code
# show(actual_parameter)

def sum(a,b):
    print(a+b)
sum(3, 4)

#types of variable:local(inside function) and global(outside).
x="python" #global
def display():
    a="datascience"
    print(a)
print(x)
display()
#types of argument:positional,keyword argument,default,arbitary:arbitary position and arbitary keyword.
def show(name,age):
    print(f"my name is{name}")
    print(f"my age is{age}")
show("misha",89)
show(89,"misha") #wrong. #positional argument


#return function.
def hi():
    return 7
print(hi()) #we need to compulsory write print in return while caliing function.
