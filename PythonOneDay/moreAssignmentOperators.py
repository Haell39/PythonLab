# Initializing variables
x = 10
y = 20

# Incrementing the value of x by 2
x += 2  # This is equivalent to x = x + 2
print(x)  # Output: 12

# Incrementing y using a different syntax
y += 2  # Another way to increment y
print(y)  # Output: 22

"""
The following are common assignment operators in Python:
- += : Addition assignment
- -= : Subtraction assignment
- *= : Multiplication assignment
- /= : Division assignment
- %= : Modulus assignment
- **= : Exponentiation assignment
- //= : Floor division assignment
"""

# Using an assignment operator within a loop
i = 0
while i < 10:
    i += 2  # Incrementing i by 2 in each iteration
    print(i)  # Outputs: 2, 4, 6, 8, 10