

# Python Operators Demonstration
```python

# 1. Arithmetic Operators
print("=== Arithmetic Operators ===")
a = 10
b = 3

# Addition
print(f"{a} + {b} = {a + b}")  # Output: 13

# Subtraction
print(f"{a} - {b} = {a - b}")  # Output: 7

# Multiplication
print(f"{a} * {b} = {a * b}")  # Output: 30

# Division
print(f"{a} / {b} = {a / b}")  # Output: 3.333...

# Floor Division
print(f"{a} // {b} = {a // b}")  # Output: 3

# Modulus (Remainder)
print(f"{a} % {b} = {a % b}")  # Output: 1

# Exponentiation
print(f"{a} ** {b} = {a ** b}")  # Output: 1000


# 2. Comparison Operators
print("\n=== Comparison Operators ===")
x = 5
y = 10

# Equal to
print(f"{x} == {y}: {x == y}")  # Output: False

# Not equal to
print(f"{x} != {y}: {x != y}")  # Output: True

# Greater than
print(f"{x} > {y}: {x > y}")    # Output: False

# Less than
print(f"{x} < {y}: {x < y}")    # Output: True

# Greater than or equal to
print(f"{x} >= {y}: {x >= y}")  # Output: False

# Less than or equal to
print(f"{x} <= {y}: {x <= y}")  # Output: True


# 3. Logical Operators
print("\n=== Logical Operators ===")
p = True
q = False

# Logical AND
print(f"p and q: {p and q}")      # Output: False

# Logical OR
print(f"p or q: {p or q}")        # Output: True

# Logical NOT
print(f"not p: {not p}")          # Output: False


# 4. Assignment Operators
print("\n=== Assignment Operators ===")
num = 5

# Assign value
num += 2   # Equivalent to num = num + 2
print(f"num after += 2: {num}")   # Output: 7

num -= 1   # Equivalent to num = num - 1
print(f"num after -= 1: {num}")   # Output: 6

num *= 3   # Equivalent to num = num * 3
print(f"num after *= 3: {num}")   # Output: 18

num /= 2   # Equivalent to num = num / 2
print(f"num after /= 2: {num}")   # Output: 9.0


# 5. Bitwise Operators
print("\n=== Bitwise Operators ===")
m = 5    # Binary: 0101
n = 3    # Binary: 0011

# Bitwise AND
print(f"{m} & {n} = {m & n}")     # Output: 1 (Binary: 0001)

# Bitwise OR
print(f"{m} | {n} = {m | n}")     # Output: 7 (Binary: 0111)

# Bitwise XOR (Exclusive OR)
print(f"{m} ^ {n} = {m ^ n}")     # Output: 6 (Binary: 0110)

# Bitwise NOT (Inverts bits)
print(f"~{m} = {-m -1}")           # Output: -6 (Inverts bits)

# Left Shift (Shift bits left)
print(f"{m} << 1 = {m << 1}")     # Output: 10 (Binary: 1010)

# Right Shift (Shift bits right)
print(f"{m} >> 1 = {m >> 1}")     # Output: 2 (Binary: 0010)
```

### Explanation of the Code:

- **Arithmetic Operators** perform basic mathematical operations.
- **Comparison Operators** compare two values and return a boolean result.
- **Logical Operators** are used for combining conditional statements.
- **Assignment Operators** assign values to variables with shorthand notation.
- **Bitwise Operators** operate on binary representations of integers.

Feel free to run this code in your Python environment to see how each operator works! If you have any questions or need further explanations, let me know!