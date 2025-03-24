#  1)fruits = ["apple", "banana", "cherry", "date", "elderberry"]
# What is fruits[0]?
print("fruit [0] is apple")
# What is fruits[-1]?
print("fruit [-1] is elderberry")
# What is fruits[2]
print("fruit [2] is cherry")

# 2)numbers = [10, 20, 30, 40, 50, 60]
# Access the third element.
numbers = [10, 20, 30, 40, 50, 60]
third_element=(numbers[2])
print(third_element)
# Access the last element.
last_element=(numbers[-1])
print(last_element)
# Access the second-to-last element
print(numbers[1::])

# 3)colors = ["red", "green", "blue", "yellow", "purple", "orange"]
# Extract the first three elements.
colors = ["red", "green", "blue", "yellow", "purple", "orange"]
print(colors[:3:])
# Extract the last two elements.
print(colors[4::])
# Extract every second element.
print(colors[::2])
# Reverse the list using slicing.
print(colors[::-1])

# 4)letters = ["a", "b", "c", "d", "e", "f", "g", "h"]
# Extract ["c", "d", "e"]
letters = ["a", "b", "c", "d", "e", "f", "g", "h"]
print(letters[2:5])
# Extract ["a", "c", "e", "g"]
print(letters[::2])
# Extract ["h", "f", "d", "b"]
print(letters[::-2])

# 5)numbers = [1, 2, 3, 4, 5, 6]
# Change the third element to 99
numbers = [1, 2, 3, 4, 5, 6]
numbers[2]=99
print(numbers)

# 6)words = ["Python", "is", "a", "great", "programming", "language"]
# Extract the words "is a great" using slicing.
words = ["Python", "is", "a", "great", "programming", "language"]
a=(words[1:4])
print(a)
# Reverse the order of words
print(words[::-1])


