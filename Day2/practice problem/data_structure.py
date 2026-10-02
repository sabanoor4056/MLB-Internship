# LISTS
# 1. Find the largest number in a list
numbers = [10, 25, 5, 40, 15]
largest = max(numbers)
print("1. Largest number:", largest)

# 2. Find the second largest number
numbers = [10, 25, 5, 40, 15]
unique_numbers = list(set(numbers))
unique_numbers.sort()
second_largest = unique_numbers[-2]
print("2. Second largest number:", second_largest)

# 3. Remove duplicate values from a list
numbers = [10, 20, 10, 30, 20, 40, 30]
without_duplicates = list(set(numbers))
print("3. List without duplicates:", without_duplicates)

# 4. Reverse a list without using reverse()
numbers = [10, 20, 30, 40, 50]
reversed_list = numbers[::-1]
print("4. Reversed list:", reversed_list)

# 5. Find common elements between two lists
list1 = [10, 20, 30, 40]
list2 = [30, 40, 50, 60]
common = list(set(list1) & set(list2))
print("5. Common elements:", common)

# TUPLES

# 6. Count occurrences of an element
numbers = (10, 20, 10, 30, 10, 40)
count = numbers.count(10)
print("6. Number of times 10 occurs:", count)

# 7. Convert a tuple into a list and vice versa
my_tuple = (10, 20, 30, 40)

# Tuple to list
my_list = list(my_tuple)
print("7. Tuple converted to list:", my_list)

# List to tuple
new_tuple = tuple(my_list)
print("List converted back to tuple:", new_tuple)

# SETS

# 8. Find unique values from a list
numbers = [10, 20, 10, 30, 20, 40, 30]
unique_values = set(numbers)
print("8. Unique values:", unique_values)

# 9. Perform union and intersection operations

set1 = {10, 20, 30, 40}
set2 = {30, 40, 50, 60}
union = set1.union(set2)
intersection = set1.intersection(set2)
print("9. Union:", union)
print("9. Intersection:", intersection)

# DICTIONARIES

# 10. Create a student record dictionary

student = {
    "name": "Saba",
    "age": 22,
    "department": "Information Technology",
    "semester": 7
}
print("10. Student record:", student)


# 11. Calculate average marks of students

marks = {
    "Math": 80,
    "English": 75,
    "Python": 90,
    "Database": 85
}
total = sum(marks.values())
average = total / len(marks)
print("11. Average marks:", average)

# 12. Count frequency of words in a sentence

sentence = "python is easy and python is powerful"
words = sentence.split()
frequency = {}
for word in words:
    if word in frequency:
        frequency[word] = frequency[word] + 1
    else:
        frequency[word] = 1

print("12. Word frequency:", frequency)