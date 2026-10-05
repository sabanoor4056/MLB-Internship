print("================================")
print("      NUMBER ANALYSIS TOOL")
print("================================")

number = int(input("Enter a number: "))

# Check Even or Odd
if number % 2 == 0:
    even_odd = "Even"
else:
    even_odd = "Odd"

# Check Prime
if number < 2:
    is_prime = False
else:
    is_prime = True

    for i in range(2, number):
        if number % i == 0:
            is_prime = False
            break

# Count Digits
temp = abs(number)
digit_count = 0

if temp == 0:
    digit_count = 1
else:
    while temp > 0:
        temp = temp // 10
        digit_count = digit_count + 1

# Reverse Number
temp = abs(number)
reverse = 0

while temp > 0:
    digit = temp % 10
    reverse = reverse * 10 + digit
    temp = temp // 10

# Check Palindrome
if number >= 0 and number == reverse:
    palindrome = "Yes"
else:
    palindrome = "No"

# Display Results
print("\n========== RESULTS ==========")
print("Number       :", number)
print("Even / Odd   :", even_odd)

if is_prime:
    print("Prime        : Yes")
else:
    print("Prime        : No")

print("Digits       :", digit_count)
print("Reverse      :", reverse)
print("Palindrome   :", palindrome)
print("==============================")