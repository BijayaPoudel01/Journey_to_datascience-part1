#1. Square all numbers in a list using map()
def square(n):
    return n*n
n=[1,2,3,4]
b=map(square,n)
print(list(b))

#now using lamda:
a=lambda n:n*n
b=map(a,[1,2,3,4])
print(list(b))

#2. Given a list nums = [1, 2, 3, 4, 5],
# use map() to return a list where each number is squared.
def square(n):
    return n * n
nums=[1, 2, 3, 4, 5]
b=map(square,nums)
print(list(b))

#using lamda:
a=lambda n:n*n
b=map(a,[1,2,3,4,5])
print(list(b))

#3. Convert all strings in a list to uppercase using map().
a=lambda b:b.upper()
b=map(a,["hi", "bijaya","Is", "my", "Name"])
print(list(b))

#using def function:
def a(b):
    return b.upper()
b=["hi", "bijaya","Is", "my", "Name"]
c=map(a,b)
print(list(c))

#4. Given a list words = ['python', 'map', 'function'], convert all words to uppercase.
def hello(words):
    return words.upper()
words = ['python', 'map', 'function']
upper_words=map(hello,words)
print(list(upper_words))


#using lambda
a = lambda word: word.upper()
words = map(a, ['python', 'map', 'function'])
print(list(words))

#5.Get the length of each word in a list using map()
a = lambda word: len(word)
words = map(a, ['python', 'map', 'function'])
print(list(words))

def length(words):   #using def
    return len(words)
words = ['python', 'map', 'function']
b=map(length,words)
print(list(b))

#6. Given a list words = ['hello', 'world', 'python'], return a list of word lengths.
def length(word):   #using def
    return len(word)
words = ['hello', 'world', 'python']
b=map(length,words)
print(list(b))

#7.Add corresponding elements of two lists using map()
a=lambda x,y:x+y
b=map(a,[1,2,3],[4,5,6])
print(list(b))

#8. Given two lists: a = [1, 2, 3] and b = [4, 5, 6], return a list containing the element-wise sum.
def hello(x,y):
    return x+y
a = [1, 2, 3]
b = [4, 5, 6]
c=map(hello,a,b)
print(list(c))

#9. 🚿 Filter() Practice Questions
# Filter out even numbers from a list using filter()
a= lambda n: n%2==0
b=filter(a,[1,2,3,4,5,6]) #filter
print(list(b))

#10.Given a list nums = [1, 2, 3, 4, 5, 6], filter and return only the even numbers.
def hi(nums):   #using def
    return nums%2==0
nums = [1,2,3,4,5,6]
b=filter(hi,nums)
print(list(b))

#11. Filter words that start with a vowel using filter()
a=lambda w: w[0] in "aeiouAEIOU"
b=filter(a,['apple', 'banana', 'orange', 'grape', 'umbrella'])
print(list(b))

#12. Given a list words = ['apple', 'banana', 'orange', 'grape', 'umbrella'], return only the words that start with a vowel.
def hi(w):
    return w[0] in "aeiouAEIOU"
w=['apple', 'banana', 'orange', 'grape', 'umbrella']
b=filter(hi,w)
print(list(b))

#13. Filter numbers greater than 10 using filter()
a=lambda n: n > 10
b=filter(a,[5,11,3,15,2])
print(list(b))

#14.Given a list nums = [5, 11, 3, 15, 2], return only the numbers greater than 10.
def hi(nums):
    return nums>10
nums=[5,11,3,15,2]
b=filter(hi,nums)
print(list(b))

#15. Filter out empty strings using filter()
a=lambda n: n != ''
b=filter(a,['hello', '', 'world', '', 'python'])
print(list(b))
# Given a list strings = ['hello', '', 'world', '', 'python'], return the list without empty strings.

# 🧮 Reduce() Practice Questions
#16. Find the product of all elements in a list using reduce()
from functools import reduce
a=lambda x,y: x*y
b=reduce(a,[1,2,3,4,5])
print(b)

# Given a list nums = [1, 2, 3, 4], calculate the product of all the elements.
from functools import reduce
def hello(x,y):
    return x*y
nums=[1,2,3,4,5]
b=reduce(hello,nums)
print(b)

# Find the maximum element using reduce()

from functools import reduce
a = lambda x, y: x if x > y else y
b = reduce(a, [1, 2, 3, 4, 5, 6, 7])
print(b)

# Given a list nums = [1, 7, 3, 9, 2], find the maximum value using reduce().
from functools import reduce
def hello(x,y):
    return x if x > y else y
nums=[1,2,3,4,5]
b=reduce(hello,nums)
print(b)

# Concatenate a list of strings using reduce()
a = lambda x, y: x+y
b = reduce(a, ['I', 'love' , 'Python'])
print(b)
# Given a list words = ['I', 'love', 'Python'], concatenate them into a single string.
from functools import reduce
def hello(x,y):
    return x+y
nums=['I', 'love', 'Python']
b=reduce(hello,nums)
print(b)
# Expected Output: 'IlovePython'

# Find the sum of squares using map() and reduce()
from functools import reduce

a = lambda x: (x*x + x*x)
b = map(a, [1, 2, 3])
result = reduce(lambda x, y: x + y, b)
print(result)


# Given a list nums = [1, 2, 3], calculate the sum of squares (1² + 2² + 3²).
from functools import reduce

nums = [1, 2, 3]
squares = map(lambda x: x*x + x*x , nums)
result = reduce(lambda x, y: x + y, squares)
print(result)

#  Recursion Practice Questions
# Write a recursive function to find the factorial of a number
def show(n):
    if n==10:  #base (stop) case
        return
    print("hello",n)
    show(n+1)  #recursion case
show(0)
# Write a recursive function to find the sum of digits of a number
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)
print(factorial(5))

# Write a recursive function to get the nth Fibonacci number
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
print(fibonacci(6))

# Write a recursive function to reverse a string
def reverse(s):
    if s == "":
        return s
    return reverse(s[1:]) + s[0]

print(reverse("biju"))

# Write a recursive function to check if a string is a palindrome
def is_palindrome(s):
    if len(s) <= 1:
        return True
    elif s[0] != s[-1]:
        return False
    else:
        return is_palindrome(s[1:-1])
print(is_palindrome("madam"))
print(is_palindrome("hello"))
print(is_palindrome("racecar"))

# Write a recursive function to find the sum of first n natural numbers
def sum_natural_numbers(n):
    if n == 0:
        return 0
    else:
        return n + sum_natural_numbers(n - 1)
print(sum_natural_numbers(5))
