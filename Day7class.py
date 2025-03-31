#Type conversion:Python interpreter convert one datatype to another.
#type casting:developer convert one data type to another.
a=23
b=30.5
c=a+b
print(c)  #type conversion

a=23
b=30.5
c=(int(a+b))
print(c) #type casting

a=bool(1)
print(a)

#input()
name=(input("enter your name:"))
print(name)

#operators:
#1. arithmetic operators
a=float(input("enter first number"))
b=float(input("enter second number"))
print(a+b)
print(a-b)
print(a/b)
print(a%b)
print(a//b)
print(a*b)
print(a**b)

#2.Relational/Comparison operators:gives output in true or false
a=45
b=23
print(a<b)
print(a>b)
print(a==b)
print(a!=b)
print(a<=b)

#3.Assignment operators:(=)
a=20
a+=5
a-=5
a*=2
a/=2
a%=5
a//=1
print(a)

#4. Logical operator:
a=True
b=False
print(a and b)
print(a or b)
print(not(a))

#5.membership operator:(in, not in)
a="my name is bijaya"
print("my" in a)
print("My"in a)

#6.#identity operator(is, isnot)
a=20
b=20
print(a is b)
print(a == b) # is le memory address herxa ra == le value herxa.

#7. bitwise Operator:(and&,or|,negation~, xor exclusive or(^)
a=12
b=13
a=(~a)
print(a)  #a=-(a+1)
a=12
b=13
print(a^b)
