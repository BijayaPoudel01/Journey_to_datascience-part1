#These are the questions that i asked chatgpt to make for me,so that i can practise.

# String Slicing Questions:
# 	1.	Given s = "abcdefghij", extract every third character.
s = "abcdefghij"
print(s[::3])

# 	2.	Reverse the string "PythonIsAwesome" but keep only every second character in the reversed string.
a="PythonIsAwesome"
print(a[::-2])

# 	3.	Extract the substring "gramm" from "ProgrammingLanguage".
a="ProgrammingLanguage"
print(a[3:8])

# 	4.	Given s = "datascience", extract "science" without using negative indices.
s = "datascience"
print(s[4:])

# 	5.	Remove the first and last characters from the string "machinelearning".
a="machinelearning"
print(a[1:14])
#0r using string method:
print(a.removeprefix("m").removesuffix("g"))

# 	6.	Given s = "ABCDEFGHIJ", extract only the uppercase vowels using slicing.
s = "ABCDEFGHIJ"
print(s[::4])

# 	7.	Swap the first and second halves of "abcdefgh", so that it becomes "efghabcd".
a="abcdefgh"
b=(a[4:]+(a[0:4]))
print(b)

# 	8.	Extract characters at even indices from "NeuralNetworks" in reverse order.
b="NeuralNetworks"
print(b[::-1][::2])
#or
print(b[::-2])

# 	9.	Given s = "DeepLearningAI", extract the substring "Learning" using slicing.
s = "DeepLearningAI"
print(s[4:12])

# List Manipulation Questions:
# 	11.	Given numbers = [5, 10, 15, 20, 25, 30, 35, 40], extract every second element.
numbers = [5, 10, 15, 20, 25, 30, 35, 40]
print(numbers[1::2])

# 	12.	Reverse the list [1, 2, 3, 4, 5, 6, 7, 8] using slicing.
a=[1, 2, 3, 4, 5, 6, 7, 8]
print(a[::-1])

# 	13.	Given words = ["Python", "Machine", "Learning", "Deep", "AI"], extract "Machine" and "Learning".
words=["Python", "Machine", "Learning", "Deep", "AI"]
print(words[1:3])

# 	14.	Given colors = ["red", "green", "blue", "yellow", "purple", "orange"], extract only the last three colors.
colors = ["red", "green", "blue", "yellow", "purple", "orange"]
print(colors[5:2:-1])

# 	15.	Create a new list containing only the first and last elements from [100, 200, 300, 400, 500].
hi=[100, 200, 300, 400, 500]
print(hi[0:5:4])

# 	16.	Replace the middle element of [1, 2, 3, 4, 5] with "X".
a=[1, 2, 3, 4, 5]
a[2]="x"
print(a)

# 	17.	Extract every third element from [10, 20, 30, 40, 50, 60, 70, 80, 90].
a=[10, 20, 30, 40, 50, 60, 70, 80, 90]
print(a[2:9:3])

# 	18.	Duplicate the list [2, 4, 6] four times using list operations.
a=[2, 4, 6]
b=a*4
print(b)

# 	19.	Given nums = [8, 16, 24, 32, 40], change the second-last element to 99.
nums = [8, 16, 24, 32, 40]
nums[-2]=99
print(nums)

# 	20.	Remove the first three elements from [1, 3, 5, 7, 9, 11, 13, 15] using slicing.
s=[1, 3, 5, 7, 9, 11, 13, 15]
print(s[3:])