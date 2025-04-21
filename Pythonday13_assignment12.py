# Create a list of odd numbers from 1 to 20 using list comprehension.
a=[i for i in range(1,21) if i%2!=0]
print(a)
# a=[i%2!=0 for i in range(1,21)]
# print(a)

# Generate a list of squares of numbers from 1 to 10.
a=[i*i for i in range(1,11)]
print(a)

# Given a list [1, 2, 3, 4, 5], create a new list where each element is multiplied by 3.
a=[1,2,3,4,5]
new_list=[i*3 for i in a]
print(new_list)

# Given a list ["apple", "banana", "cherry"], create a new list with each word reversed
a=["apple", "banana", "cherry"]
new_list=[i[::-1] for i in a]
print(new_list)