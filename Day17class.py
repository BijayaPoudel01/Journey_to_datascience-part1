#module:a file where python code is stored such as function,variable,class.
#syntax: from file_name import function.
import random

from Day16class import Student
a=Student()
a.show()

#shuffle:
a=[5,7,3,1,2]
random.shuffle(a)
print(a)

#calender
import calendar
a=calendar.month(2025,2)
print(a)

#time
import time
a=time.ctime()
a=time.localtime()
print(a)

import datetime
a = datetime.datetime.now()
print(a)

#math
import math
a=math.sqrt(36)
print(a)
c=math.radians(30)
b=math.sin(c)
print(b)
h=math.floor(45.88)
print(h)

#we can also import at begining.
from math import sqrt
a=sqrt(36)
print(a)

#exception handelling:handelling error that occur in python code,try,except,finally.
# def show():
#     return 5
# print("hello")
# print(show())

def show():
    try:
        print(2+"2")
    except:
        print("this is error")
        return
    finally:
        print("hello")
show()