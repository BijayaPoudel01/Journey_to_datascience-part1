#Conditional statements
a="welcome to our bus"
print(a.center(70,"+"))
age=int(input("enter your age"))
if age<=12:
    print("you have to pay rs 20")
elif age<=18 and age>12:
    if age==15: #nested if
        print("you are luckky today,you dont have to pay")
    else:
      print("you have to apy rs 30")

else:
    print("you have to pay rs 80")

    #shorthand elsif:only one if and else
a=20
print("hi")if a==20 else print("bye")

# Classwork:write a program where user ask the input number and also ask operator and perform arithmetic operations.
a=int(input("Enter first number"))
b=int(input("Enter second number"))
operator=input("enter operator")
if operator=="+":
    print(a+b)
elif operator=="-":
    print(a-b)
elif operator=="*":
    print(a*b)
else:
    print("invalid")

    #find even or odd
a=int(input("enter any number"))
if a % 2==0:
    print("the number is even")
else:
    print("the number is odd")

# classwork:Write a program that takes a score as input and assigns a grade based on the following criteria:
# 90 and above: Grade A
# 80–89: Grade B
# 70–79: Grade C
# Below 70: Grade
score=int(input("enter your score"))
if (score>=90):
    print("grade A")
elif (score>=80 and score<=89):
    print("grade B")
elif (score >= 70 and score<= 79):
    print("grade c")
else:
    print("fail")

#game(rock,paper and sissor)
a="we are playng rock,paper and sissors game"
print(a.center(70,"+"))
print("rules: R>S, P>R, S>P")
user=input("enter your choice")
user=user.upper()
print(user)
import random
computer= random.choice(["S","R","P"])
print(computer)
if(user=="R" and computer== "S") or(user=="P" and computer== "S") or((user=="S" and computer== "P")):
    print("user won")
elif(user==computer):
    print("draw")
elif user not in ("S", "R","P"):
    print("enter only between 'S','R','P'")
else:
    print("user loose")


