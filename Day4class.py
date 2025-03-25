thislist=["banana", "apple", "cheery", "orange", "kiwi"]
thislist[1:3]="walnut","mango" #replacing apple and cherry
print(thislist)

#list inbuit methods
#adding methods.
#1.append()
a=[12,40,66.70,"ram"]
a.append("hari")
print(a)

#2.extend()
a.extend(["sita", 4,77])
print(a)

#3. insert()
a.insert(2,"rita")
print(a)

#deleting methods.
#1. pop()
a=[1,2,3,"ram"]
a.pop(2)
print(a)

#2.remove()
a.remove("ram")
print(a)

#3.clear()
a.clear()
print(a)

del a

#sort(mutable) and sorted(immutable)
a=[1,5,4,7,9]
a.sort() #ascending order
print(a)

a.sort(reverse=True) #descending order
print(a)

#sorted
a=[10,7,2,6]
b=sorted(a)
print(b)

b=sorted(a,reverse=True)
print(b)

c=["ram", "bijaya", "sitaram"]
c.sort(key=len)
print(c)
