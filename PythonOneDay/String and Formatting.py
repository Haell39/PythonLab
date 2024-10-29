# Initializing string variables
name = 'rafael dutra'
print(name.upper())  # Converts the string to uppercase

name2 = 'test accounting'
name2 = name2.upper()  # Another way to convert to uppercase
print(name2)  # Output: TEST ACCOUNTING

# Demonstrating various string assignment and manipulation methods
name = "hello world"
name3 = "  hello world  "  # String with leading and trailing spaces
name4 = "hello world"
string1 = "hello, world!"

# Replacing substring and manipulating strings
name = name.replace("hello", "hi")  # Replaces 'hello' with 'hi'
name3 = name3.strip()  # Removes leading and trailing whitespace
name4 = name4.capitalize()  # Capitalizes the first letter
string1 = string1.title()  # Capitalizes the first letter of each word

# Printing the results of string manipulations
print(name)    # Output: hi world
print(name3)   # Output: hello world
print(name4)   # Output: Hello world
print(string1) # Output: Hello, World!

print("\n")

print(name, string1, name3, name4, sep="\n") #* Using only 1 print statement with arguments and a separator
