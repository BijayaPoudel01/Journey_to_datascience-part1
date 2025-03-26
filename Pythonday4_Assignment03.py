#assignment
# #1)list a=["hello",45,67,89.90,45,45,"apple","orange"]
# i)add value 34 to the list
a=["hello",45,67,89.90,45,45,"apple","orange"]
a.append(34)
print(a)
# ii)add multiple value to the list
a.extend([40,"ram", 44.5])
print(a)
# iii)using slicing extract  app from given list
print(a[6][0:3:1])
# iv)remove random value from list (e.g=45)
a.remove(45)
print(a)
# v)remove all data from list
a.clear()
print(a)
# vi)given two list a and b (creat list yourself) and add these two list in third list and print third list
a=["bijaya",1,2,3]
b=["poudel",4,5,6]
c= a+b  # + operator concatenates.
print(c)

# Given two tuples tuple1  and tuple2 , concatenate them to form a new tuple.
a=(1,2,3,"amisha","mam")
b=("is","nice",4,5,6)
c=a+b
print(c)
# Given the tuple my_tuple = (10, 20, 30, 40, 50), slice the tuple to get the last three elements.
my_tuple = (10, 20, 30, 40, 50)
a=my_tuple[2::]
print(a)
# Find the length of the tuple my_tuple = ('a','b','c','d').
my_tuple = ('a','b','c','d')
print(len(my_tuple))

# Given a list a=[3,5,32,4,52,13,4,6,71] sort in ascending and descending order using both method
a=[3,5,32,4,52,13,4,6,71]
a.sort()
print(a)
a.sort(reverse=True)
print(a)

#next sorted function
a=[3,5,32,4,52,13,4,6,71]
b=sorted(a)
print(b)
b=sorted(a,reverse=True)
print(b)