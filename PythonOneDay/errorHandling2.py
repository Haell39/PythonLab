# Python Exception Handling Examples

# 1. IOError: Handling file-related errors
try:
    print("\n[IOError Example]")
    file = open('nonexistent_file.txt', 'r')
except IOError:
    print("Error: File not found or cannot be opened")

# 2. ImportError: Handling module import errors
try:
    print("\n[ImportError Example]")
    import nonexistent_module
except ImportError:
    print("Error: Module not found")

# 3. IndexError: Handling index out of range errors
try:
    print("\n[IndexError Example]")
    numbers = [1, 2, 3]
    print(numbers[5])
except IndexError:
    print("Error: Index out of range")

# 4. KeyError: Handling missing dictionary keys
try:
    print("\n[KeyError Example]")
    my_dict = {'name': 'Alice'}
    print(my_dict['age'])
except KeyError:
    print("Error: Key not found in dictionary")

# 5. NameError: Handling undefined variable names
try:
    print("\n[NameError Example]")
    print(nonexistent_variable)
except NameError:
    print("Error: Variable not defined")

# 6. TypeError: Handling incorrect data type operations
try:
    print("\n[TypeError Example]")
    result = 'Hello' + 5
except TypeError:
    print("Error: Incompatible types")

# 7. ZeroDivisionError: Handling division by zero
try:
    print("\n[ZeroDivisionError Example]")
    a = int(input("Enter a number: "))
    b = int(input("Enter another number: "))
    print(f"The result of {a} / {b} is: {a / b}")
except ZeroDivisionError:
    print("Error: Cannot divide by zero")
except ValueError:
    print("Error: You need to enter a valid number")

# 8. General Exception Handling (Catch-All)
try:
    print("\n[General Exception Handling Example]")
    with open("missing.txt", "r") as file:
        content = file.read()
except Exception as e:
    print(f"Unknown error occurred: {e}")

# Final message to show that the program has ended
print("\nProgram finished executing. Thank you for using the exception handling demo!")