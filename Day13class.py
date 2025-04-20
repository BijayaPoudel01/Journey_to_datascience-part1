#decorator=function that modifies behaviour of another function or class.# decorators:function that modifies behaviour of another function or class. without changing its structure.
def outer():
    def inner():
        print("i am inner function")
    return inner
def show():
    print("i am outsdie function")

# Decorator function
def outer(func):
    def inner():
        print("Before the function runs")
        func()
        print("After the function runs")
    return inner

# Decorating the 'show' function
@outer
def show():
    print("I am the original show function")

# Call the decorated function
show()

#list comprehensive.
a=[1,2,3,4,5]
b=[]
[b.append(i+2)for i in a]
print(b)

a=["youtube.com","facebook.com","whatsapp.com"]
a=[i.strip(".com")for i in a]
print(a)
