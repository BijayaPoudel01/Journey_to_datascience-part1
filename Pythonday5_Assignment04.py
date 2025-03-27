# Create a set with the following elements: 10, 20, 30, 40, 50.
a={10,20,30,40,50}
print(type(a))
# Add the element 60 to the set.
a.add(60)
print(a)
# Remove the element 20 from the set.
a.remove(20)
print(a)
# Check if the element 30 is in the set.
print(30 in a)
#or
b=a.__contains__(30)
print(b)
# Find the length of the set
print(len(a))
# Create two sets: a = {1, 2, 3, 4} and b = {3, 4, 5, 6}.
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}
# Perform the following operations:
# Find the union of both sets.
c=a.union(b)
print(c)
# Find the intersection of both sets.
d=a.intersection(b)
print(d)
# Find the difference between:
difference=a.difference(b)
print(difference)

difference=b.difference(a)
print(difference)
# find the symettrical differnce:
symettrical_diff=a.symmetric_difference(b)
print(symettrical_diff)
# check if the set is subset,superset and disjoint
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}
c=a.issuperset(b)
print(c)

d=a.issubset(b)
print(d)

e=a.isdisjoint(b)
print(e)

# 1Create a dictionary with the following key-value pairs: (name , age, and city ).
var={'name':"bijaya", 'age':23, 'city':"dhankuta"}
print(type(var))
print(var)
#next process of creating dict:
var=dict(name="bijaya",age=23)
print(var)
#
# 2)Given the dictionary person = {'name': 'Bob', 'age': 30, 'city': 'Los Angeles', 'job': 'Doctor'}, access and
#  print the values associated with the keys 'name' and 'job'
person = {'name': 'Bob', 'age': 30, 'city': 'Los Angeles', 'job': 'Doctor'}
print(person.get('name'))
print(person.get('job'))