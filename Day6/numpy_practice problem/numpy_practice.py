import numpy as np
# =========================
# NUMPY PRACTICE
# =========================

print("===== NUMPY =====")

# 1. Create a 1D array
array_1d = np.array([10, 20, 30, 40, 50])
print("\n1D Array:")
print(array_1d)

# 2. Create a 2D array
array_2d = np.array([
    [1, 2, 3],
    [4, 5, 6]
])
print("\n2D Array:")
print(array_2d)

# 3. Arithmetic operations
print("\nArithmetic Operations:")
print("Addition:", array_1d + 5)
print("Subtraction:", array_1d - 5)
print("Multiplication:", array_1d * 2)
print("Division:", array_1d / 2)

# 4. Maximum, Minimum, Mean and Sum
print("\nArray Statistics:")
print("Maximum:", np.max(array_1d))
print("Minimum:", np.min(array_1d))
print("Mean:", np.mean(array_1d))
print("Sum:", np.sum(array_1d))

# 5. Reshape array
numbers = np.array([1, 2, 3, 4, 5, 6])
reshaped_array = numbers.reshape(2, 3)
print("\nReshaped Array:")
print(reshaped_array)

# 6. Indexing
print("\nIndexing:")
print("First element:", array_1d[0])
print("Third element:", array_1d[2])

# 7. Slicing
print("\nSlicing:")
print("First three elements:", array_1d[:3])
print("Elements from index 1 to 3:", array_1d[1:4])