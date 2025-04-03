# Write a program to print the squares of numbers from 1 to 10 using a for loop.
for i in range (1,11,1):
    print(f"{i}*{i}={i*i}")
# Write a program to print all even numbers between 1 and 20 using a for loop.
for i in range(1,21):
    if i%2==0:
      print(i)
#alternative:
for i in range(2,21,2):
    print(i)

# Write a program to calculate the sum of numbers from 1 to 50 using a for loop.
total=0
for i in range(1, 51):
    total+=i
print(f"sum of numbers from 1 to 50 ={total}")


# Write a program to calculate the sum of all odd numbers between 1 and 100 using a for loop.
total=0
for i in  range(1,101,2):
    total+=i
print(i)
print(f"sum of odd numbers from 1 to 100 ={total}")

# Write a program to find the largest number in a list [2, 8, 1, 16, 5, 23, 7] using a for loop
a= [2, 8, 1, 16, 5, 23, 7]
largest=a[0]
for i in a:
    if i>largest:
        largest=i
print(f"the largest number in the list is:{largest}")

#while loop
# Write a program that uses a while loop to print numbers from 1 to 10.
i=1
while i<=100:
    print(i)
    i+=1

# Write a program that prints all even numbers between 1 and 20 using a while loop.
a=2
while a<=20:
    print(a)
    a+=2


# Write a program that uses a while loop to print numbers from 10 to 1 in reverse order.
a=10
while a>=1:
    print(a)
    a-=1

for i in range(0,10,-1):
    print(i)
# Write a program that keeps taking input from the user and stops only when the user types "stop".
while True:
    a = input("enter the number")
    if a=="stops":
       break
# Write a program to print the multiplication table of 5 using a while loop.
a=5
i=1
while i<=10:
    print(f"{a}*{i}={a*i}")
    i+=1


# Write a program to print the square of numbers from 1 to 10 using a while loop.
i=1
while i<=10:
    print((f"the square of {i}={i*i}"))
    i+=1

# Write a program to calculate the sum of all odd numbers between 1 and 30 using a while loop.
total = 0
i = 1
while i <= 30:
    total += i
    i += 2
print(f"Sum of all odd numbers from 1 to 30 = {total}")
