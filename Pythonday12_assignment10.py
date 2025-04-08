#fibonacci series using loop.
def fibo(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    return fibo(n-1) + fibo(n-2)

for i in range(10):
    print(fibo(i))

#map,filter,reduce using lamda function.

a = lambda n: n * 2
b = map(a, (1, 2, 3, 4))  #map
print(tuple(b))

a= lambda n: n%2==0
b=filter(a,(1,2,3,4,5,6)) #filter
print(list(b))

from functools import reduce
a= lambda x,y: x+y
b=reduce(a,[1,2,3,4,5]) #reduce
print(b)