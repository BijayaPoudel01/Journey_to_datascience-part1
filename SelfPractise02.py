#loops:while and for loop practising.
a=[1,2,3,4,2,1]
#  b=a.copy()
a.reverse()
print(a)
if a==a.reverse():
    print("palindrome")
else:
    print("no")

count=1
while count<5:
    print("hi biju")
    count+=1

n=int(input("n="))
i=1
while i<=10:
    print(f"{n}*{i}={n*i}") #multiply
    i+=1

a=["ram","shyam","hari"]
i=0
while i<len(a):
    print(a[i])
    i+=1   #printing from list
    #using for loop
a=["ram","shyam","hari"]
for i in a:
    print(i)

#search for number x in this tuple(1,4,9,16,25,36,49,64,81,100) using loop
a = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 49)
x = 49
i = 0

while i < len(a):
    if a[i] == x:
        print("found at index", i)
    i += 1



# #using for loop
a = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 49)
index=0
x=49

for i in len(a):
    if i==x:
        print("element found in index",i)
        i+=1