# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/


# IF, ELIF and ELSE command
# even or odd using if and else
# even
x = 6
r = x % 2
if r == 0:
    print("Even")
else:
    print("Odd")

# odd
x = 5
r = x % 2
if r == 0:
    print("Even")
else:
    print("Odd")

# even or odd using if and elif
x = 5
r = x % 2
if r == 0:
    print("Even")
elif r==1:
    print("Odd")

# simple code using if, elif and else
x=3
if x==1:
    print("one")
elif x==2:
    print("two")
elif x==3:
    print("three")
else:
    print("no output")

# code to find positive or negative
# positive
a=2
x=a
if a==x:
    print("positive")
elif a!=x:
    print("negative")

# negative
a=2
x=-a
if a==x:
    print("positive")
elif a!=x:
    print("negative")

# greatest of all three numbers
num1=10
num2=20
num3=30
if num1>num2 and num1>num3:
    print("The Largest number is ",num1)
elif num2>num1 and num2>num3:
    print("The Largest number is ",num2)
else:
    print("The Largest number is ",num3)

# WHILE LOOP
# simple Ascending code
i=1
while i<=5:
     print(i)
     i=i+1

# simple Descending code
i=5
while i>=1:
     print(i)
     i=i-1

# write a code to print all the values from 1 to 100. skip the numbers which are divisible by 3 or 5.
i=1
j=1
while j<=100:
    if ((j%3 and j%5)==0):
        j=j+1
    else:
        print(j)
        j=j+1
    i=i+1

#(or)
for i in range(1,101,1):
    if i%3!=0 or i%5!=0:
       print(i)

#(or)
for i in range(1,101,1):
    if i%3==0 or i%5==0:
        continue
    else:
        print(i)

# write a code to print the pattern (# # # #)
a=1
while a<=4:
    print("# # # #")
    a=a+1

# FOR loop
x="LAVANYA"
for i in x:
    print(i)

for i in range(0,10,1):
    print(i)

# PROBLEMS
#1 print first 10 natural numbers using while loop
a=1
while a<=10:
    print(a)
    a=a+1

#2 print the following pattern using nested loops
b=1
if b<=5:
    print(b)
    c=b+1
if c<=5:
    print(b,c)
    d=c+1
if d<=5:
    print(b,c,d)
    e=d+1
if e<=5:
    print(b,c,d,e)
    f=e+1
if f<=5:
    print(b,c,d,e,f)
else:
    print(0)

#(or)
print("Number Pattern")
row=5
for i in range(1,row+1,1):
    for j in range(1,i+1):
        print(j,end='')
    print("")

#3 sum of all numbers
a=(2,4,6,8,10,12,14,16,18,20)
b=sum(a)
print(b)

#4 average of all numbers
a=(2,4,6,8,10,12,14,16,18,20)
b=sum(a)
c=b/10
print(c)
