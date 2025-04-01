#1.Write a program to check if a person is eligible to vote. The eligibility age is 18 or above.
age=int(input("Enter your age if you want to vote"))
if age>=18:
    print("You are eligible to vote")
else:
    print("sorry! you are not eligible to vote")

#2.Write a program that takes three numbers as input and prints the largest among them.
num1=int(input("enter 1st no:"))
num2=int(input("enter 2nd no:"))
num3=int(input("enter 3rd no:"))
if num1>num2 and num1>num3:
    print("num1 is greater")
elif num2>num3:
    print("num2 is greater")
else:
    print("num3 is greater")

#3.Write a program to check if a given year is a leap year or not. A year is a leap year if:
# It is divisible by 4 but not divisible by 100, OR
# It is divisible by 40
a=int(input("enter a year"))
if (a%4==0 and a%100!=0)or (a %40==0) :
    print("it is a leap year")
else:
    print("it is not leap year")

#4.Write a program to implement a simple calculator. The program should:
# Ask the user for two numbers.
# Ask the user to choose an operation (add, subtract, multiply, divide).
# Perform the chosen operation and print the result
a=int(input("enter 1st no"))
b=int(input("enter 2nd no"))
c=input("enter operation")
if c==("+"):
    print(a+b)
elif c=="-":
    print(a-b)
elif c=="*":
    print(a*b)
elif c=="/":
    print(a/b)
else:
    print("invalid")

#5.Write a program to print numbers from 1 to 100.
for a in range (1,101):
 if a<=100:
    print(a)

#6.If a number is divisible by 3, print "Fizz".
# If divisible by 5, print "Buzz".
# If divisible by both, print "FizzBuzz".
# Otherwise, print the number itself
a=int(input("enter a number"))
if a%3==0:
    print("Fizz")
elif a%5==0:
    print("Buzz")
elif a % 3 == 0 and a%5==0:
    print("FizzBuzz")
else:
    print(a)


#7.Given two variables x = 15 and y = 20,
# use conditional statements to print which variable is larger, or if they are equal.
x=15
y=20
if x>y:
    print("x is greater")
elif x<y:
    print("y is greater")
elif (x==y):
    print("this is equal")
else:
    print("invalid")

#8.Given a variable num = 7,
# use a conditional statement to check if the number is even or odd and print the result.
num=7
print("even")if num%2==0 else print("odd")

#9.Write a Python Program to Check weather a candidate Eligible for Vote or not.
age=int(input("Enter your age if you want to vote"))
if age>=18:
    print("You are eligible to vote")
else:
    print("sorry! you are not eligible to vote")

#10.Write a Python program to check weather Given Number is Divisible by 7 or Not.
num=int(input("enter you number"))
print("divisible by 7")if num%7==0 else print("not divisible")

#11.Check if the value 10 is not present in the tuple t = (5, 15, 20, 25).
t = (5, 15, 20, 25)
if 10 in t:
    print("yes")
else:
    print("no")

#12. Determine if the value 25 is present in the list
# list = [10, 20, 30, 40, 50] using a simple conditional statement
list = [10, 20, 30, 40, 50]
if 25 in list:
    print("yes")
else:
    print("no")
#13.Check if the value 100 exists in the set s = {50,75,100,125}.
s = {50,75,100,125}
print("yes")if 100 in s else print("no")

