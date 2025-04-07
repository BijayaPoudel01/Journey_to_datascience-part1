# Create a function  that takes two numbers as input and returns their sum.
def sum_num():
    a=int(input("enter 1st number"))
    b=int(input("enter 2nd number"))
    return a+b
result=sum_num()
print(f"the sum of num is:{result}")

#another method practise:
def sum_num(a,b):
    return a+b
result=sum_num(5,7)
print(result)

# Define a function  that checks whether a given string is a palindrome.
def check():
    a=(input("give one word"))
    c=a[::-1]
    print(c)
    if c==a:
        print("it is palindrome")
    else:
        print("not palindrome")
check()

# Write a function max_of_three that takes three numbers and returns the largest of the three.

def maximum():
    a=int(input("first no"))
    b=int(input("sec no"))
    c=int(input("third no"))
    if a>b and a>c:
        return a
    elif b>c:
        return b
    else:
        return c

result=maximum()
print(result)

#another practise
def maximum(a,b,c):
    if a>b and a>c:
        return a
    elif b>c:
        return b
    else:
        return c
result=maximum(3,4,5)
print(result)

# Create a function that takes a number as input and returns True if the number is prime, otherwise False.
def hello(n):
    if n <= 1:
        return False
    for i in range(2,n):
        if n%i==0:
            return False
    else:
        return True
num=int(input("enter a number"))
if  hello(num):
    print(f"{num} is a prime number")
else:
    print(f"{num}is not a prime number")
# Define a function count_vowels that takes a string as input and counts the number of vowels in the string.

def count_vowels(n):
    vowel = "aeiouAeiou"
    count=0
    for i in n:
        if i in vowel:
            count+=1
    return count

word=input("enter a word")
result=count_vowels(word)
print(result)


# Write a function  that takes a list and returns a new list with duplicates removed.
def remove_duplicates(a):
    return list(set(a))
my_list = [1, 2, 3, 2, 4, 5, 5]
new_list = remove_duplicates(my_list)
print(new_list)

# Write a function  that takes a string and returns the reversed string.
def hi():
    a=input("enter your string")
    return a[::-1]
print(hi())

# Write a function sort_list that takes a list of numbers and returns the list sorted in ascending order.
def sort_list(b):
    b.sort()
    return b

b=input("enter the list:",) .split(",")
b = [int(x.strip()) for x in b]
print(sort_list(b))

# find prime number between certain range using function
def hello(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


start = int(input("Enter the starting number: "))
end = int(input("Enter the ending number: "))


for num in range(start, end + 1):
    if hello(num):
        print(f"{num} is a prime number")

# make calculator using function
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Error! Division by zero."

def calculator():
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")


    choice = input("Enter choice (1/2/3/4): ")

    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    if choice == '1':
        print(f"The result is: {add(num1, num2)}")
    elif choice == '2':
        print(f"The result is: {subtract(num1, num2)}")
    elif choice == '3':
        print(f"The result is: {multiply(num1, num2)}")
    elif choice == '4':
        print(f"The result is: {divide(num1, num2)}")
    else:
        print("Invalid input! Please choose a valid operation.")

calculator()

