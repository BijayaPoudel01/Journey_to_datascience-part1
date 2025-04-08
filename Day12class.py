# #lambda function=anynomous function ,which doesnot have identity,similar def function
# #syntax:  lambda argument:experssion
# #it takes less memory space
# #it has fast performance
# #it takes less time

a=lambda x:x+2
print(a(3))

b=lambda x,y,z:(x*y+z)/3
print(b(3,5,7))


# #recursion function=a function calling itself againa and again
# # #sys module(inbuilt module)
# import sys
# print(sys.setrecursionlimit(30))
# print(sys.getrecursionlimit())
#
# def show():
#     print("hello")
#     show()
# show()

# # reursion case and base case

def show(n):
    if n==10:  #base (stop) case
        return
    print("hello",n)
    show(n+1)  #recursion case
show(0)


# #recursence case
# #factorial = n*(n-1)! n!
# #5!=5*4*3*2*1*0!=120
# #1!=1
# #0!=1

def home(n):
    if n==1 or n==0:
        return 1
    return n*home(n-1)  #5*4*3*2*1


print(home(7))

# #fibonacii series
# #0 1 1 2 3 5 8 13 21
# a=0
# b=1
# a=1
# b=1
# a,b=b,a+b
def fibo(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    return fibo(n-1) + fibo(n-2)
print(fibo(4))


# iterator or iterable=object that contain countable numbers of value eg,list,tuple,set
# map(),filter(),reduce()

# def show(n):
#     return n+2
# n=[1,2,3,4]
# print(show(n))

# map()=inbuilt function(predefined or predined) that takes function and iterator
# and it applies function to each elemnent
# syntax:  map(function,iterator)
def show(n):
    return n * 2


n = (1, 2, 3, 4)
b = map(show, n)
print(tuple(b))


# filter()=inbuilt function,that takes function and iterator,and it process according to condition
# syntax: filter(function,iterator)


def home(n):
    if n % 2 == 0:
        return n


n = [1, 2, 3, 4]
b = filter(home, n)
print(list(b))

# reduce()=inbuilt function,that takes function and iterator
# [1,2,3,4]

from functools import reduce


def sum(x, y):
    return x + y


n = [1, 2, 3, 4, 5]  # x=1 y=2 x=3 y=3 x=6  y=4  x=10 y=5 15
a = reduce(sum, n)
print(a)
