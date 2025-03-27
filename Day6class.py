std={
    'name':"biju",
'age':23
}
print(std.keys())
print(std.values())
print(std.items())

#adding single values.
std['surname']="poudel"
print(std)

b={
    'email':"biju@gmail.com",
    'telephone': 98621
}
std.update(b) # adding multiple values
print(std)

#deleting methods.
del std['age']
print(std)

std.pop('surname')
print(std)

std.popitem()
print(std)

std.clear()
print(std)

#nested dictionary
grade={
    'emp1':{
        'name':"ram",
        'subject':"science"
    },
    'emp2':{
        'name':"sita",
        'subject':"math"
    }
}
print(grade)

#accessing values
print(grade['emp1']['name'])

#value replacing
grade['emp2']['subject']="computer"
print(grade)

del(grade['emp2']['subject'])
print(grade)

#make a dictionary named student where add subjects with its marks and find the average marks of all.
student={
'computer':98,
'math':99,
'science':80,
'neplai':78
}
#average formula:total/4
total=sum(student.values())
print(total)
avg=total/4
print(f"the average marks is {avg}") #fstring is used mostly.
print("the average marks is:", avg)

a={
    'name':"rama",
    'age':66
}
b=a.copy()
print(b)

#Binary datatype:bytes and bytearray.
#bytes:immutable
a=bytes([1,2,3,4,5,9])
print(type(a))
print(a)

#bytearray:mutuable
a=bytearray([6,7,8,9,2])
print(a)

a[0]=99
print(a)


#boolean datatype true:1,false=0
a=True
print(type(0))

#none datatype=absence of data
a=None
print(a)



