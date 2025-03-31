# Write an expression using arithmetic operators (+, -, , /, %, //, *) with different numbers.
a= (25*2)+(5-2)/1%3//2**2
print(a)

# Use the assignment operator (+=, -=, =, /=, %=, //=, *=) to modify a variable.
a=20
a+=5
a-=5
a*=2
a/=2
a%=5
a//=1
print(a)

# Use a comparison operator (>, <, >=, <=, ==, !=) between two numbers.
a=50
b=40
print(a>b)
print(a<b)
print(a>=b)
print(a<=b)
print(a==b)
print(a!=b)

# Use logical operators (and, or, not) with boolean values.
a=7
b=9
print(a and b)
print(a or b)
print(not(a))
#
# Apply the is and == operators on two variables with the same value.
First_value=500
Second_value=500
print(First_value is Second_value)
print(First_value==Second_value)

# Perform a bitwise AND (&), OR (|), XOR (^), NOT (~), operation on two numbers.
a=15
b=10
print(a & b)
print(a | b)
print(a^b)
a=(~a)#-(a+1)
print(a)
#
# Create an expression using a combination of arithmetic, comparison, and logical operators.
a=50
b=40
c=10
result=(((a+b)>c) and ((c*b)/a)<a)
print(result)

# Use the identity operator (is not) and membership operator (in, not in) in a single line
a="ram"
b="rama"
print((a in b) is not (a not in b ))

# Convert an integer into a float and a string.
a=int(input("enter first number"))
b=int(input("enter second number"))
c=a+b
print(float(c))
print(str(c))

# Convert a float into an integer and a string.
a=40.80
print(int(a))
b=str(a)
print(b)
print(type(b))

# Convert a string into an integer (if possible).
a="50"
b="50"
c=a+b
d=int(a)+int(b)
print(c)
print(d)

# Convert a boolean (True or False) into an integer and a float.
x=True
y=False
print(int(x))
print(float(y))

# Convert an integer into a boolean and explain the result
x=1
y=20
print(bool(x))
print(bool(y)) #here both  x and y are true because they are non zero numbers. and every non zero numbers are considered true in python boolean.
               # (only zero is considered as false)