#for loop:
for i in range(10):
    print(i)

for i in range(1,16,2):
    print(i,end=" ")

a=["sita", "gita","hari"]
for i in a:
    print(i)
    for j in i: #nested loop
     print(j)

a=2
for i in range(1,11,1):
    print(f"{a}*{i}={a*i}")

b=int(input("enter any number"))  #multiplication
for i in range(1,11,1):
    print(f"{b}*{i}={b*i}")

#while loop
    i=1
    while i<=7:
        print(i)
        i+=1

b=int(input("enter any number"))
i=1
while i<=10:
    print(f"{b}*{i}={b*i}")
    i+=1

#control statement:pass, break, continue
#pass:it secure space for future use.
for i in range(10):
    pass

print("hello")

#break:loop terminates whenever break keyword is encountered.
i=0
while i<5:
    print(i)
    if i ==2:
        break
    i+=1

#continue= it terminates the current situation or condition and executes next situation.
for i in range(1,12,1):
    if i%2==0:
        continue
    print(i)