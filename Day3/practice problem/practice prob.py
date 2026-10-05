# positive , negative or zero

number = int(input("Enter a number: "))
if number > 0:
    print("Positive number")
elif number < 0:
    print("Negative number")
else:
    print("Zero")

# even or odd  

number = int(input("Enter a number: "))
if number % 2 == 0:
    print("Even number")
else:
    print("Odd number")

# create grade claculator 

marks = int(input("Enter your marks: "))
if marks < 0 or marks > 100:
    print("Invalid marks")
elif marks >= 80:
    print("Grade A")
elif marks >= 70:
    print("Grade B")
elif marks >= 60:
    print("Grade C")
else:
    print("Fail")

# find largest among 3 numbers

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

if a >= b and a >= c:
    print("Largest number:", a)
elif b >= a and b >= c:
    print("Largest number:", b)
else:
    print("Largest number:", c)

# leap year 

year = int(input("Enter a year: "))
if year % 400 == 0:
    print("Leap year")
elif year % 100 == 0:
    print("Not a leap year")
elif year % 4 == 0:
    print("Leap year")
else:
    print("Not a leap year")

# print number from 1 to 100

for i in range(1, 101):
    print(i)

# print all even number from 1 to 100

for i in range(1, 101):
    if i % 2 == 0:
        print(i)

# sum of numbers from 1 to N

n = int(input("Enter N: "))
total = 0
for i in range(1, n + 1):
    total = total + i
print("Sum:", total)

# multiplication table of a number

number = int(input("Enter a number: "))
for i in range(1, 11):
    print(number, "x", i, "=", number * i)

# count the number of digits in a number 
   
number = int(input("Enter a number: "))
number = abs(number)
count = 0
if number == 0:
    count = 1
else:
    while number > 0:
        number = number // 10
        count = count + 1
print("Number of digits:", count)

# logic building problem 
# reverse number 

number = int(input("Enter a number: "))
number = abs(number)
reverse = 0
while number > 0:
    digit = number % 10
    reverse = reverse * 10 + digit
    number = number // 10
print("Reversed number:", reverse)

# check whether is a number is palidrome

number = int(input("Enter a number: "))
original = number
temp = abs(number)
reverse = 0
while temp > 0:
    digit = temp % 10
    reverse = reverse * 10 + digit
    temp = temp // 10
if number >= 0 and original == reverse:
    print("Palindrome")
else:
    print("Not a palindrome")

# Fibonacci sequence

n = int(input("How many terms? "))
a = 0
b = 1
for i in range(n):
    print(a, end=" ")
    next_number = a + b
    a = b
    b = next_number

# check whether is a number is prime

number = int(input("Enter a number: "))
is_prime = True
if number < 2:
    is_prime = False
else:
    for i in range(2, number):
        if number % i == 0:
            is_prime = False
            break
if is_prime:
    print("Prime number")
else:
    print("Not a prime number")

# prime number between 1 and 100

for number in range(2, 101):
    is_prime = True
    for i in range(2, number):
        if number % i == 0:
            is_prime = False
            break
    if is_prime:
        print(number, end=" ")    