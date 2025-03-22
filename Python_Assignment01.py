#1.How would you extract the first 5 characters of the string "HelloWorld" using slicing?
a = "HelloWorld"
print(a[0:6:1])

#2.Given the string "PythonProgramming", how would you slice and extract the last 4 characters?
course = "PythonProgramming"
print(course[13:17:1])

#3.For the string "abcdefg", how can you slice the string to get every second character starting from first?
a="abcdefg"
print(a[0:7:2])

#4.How can you reverse the string "Palindrome"using slicing?
reverse="Palindrome"
print(reverse[10::-1])

#5.What will be the result of the slicing operation s[3:] if s= "DataScience"?
#-> the result will be aScience.
s= "DataScience"
print(s[3:])

#6.How would you extract every second character in reverse order from the string"abcdefgh"?
b="abcdefgh"
print(b[7:0:-2])

#7. For the string "ArtificialIntelligence", how would you extract the substring "intelli"using slicing?
a="ArtificialIntelligence"
#print(a[10:17:1])
b=(a.lower()[10:17:1])
print(b)

#8.Given two strings str1 = "Hello" and str2 = "World", concatenate them to form a new string "HelloWorld".
str1="Hello"
str2="World"
combined=str1 +str2
print("New string is:", combined)

#9.Extract the substring "lowor"from the string str ="helloWorld" using slicing.
print(combined)
print(combined[3:8:1]) #completed.
