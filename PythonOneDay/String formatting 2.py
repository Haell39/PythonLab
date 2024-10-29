# ^^ Basic Variables
name = 'Bob'
age = 25
height = 1.75  # in meters
occupation = 'Developer'

# ^^ Basic Print Statements
print("Basic Print Statements:")
print(name, age)
print("Hello, my name is", name, "and I am", age, "years old.")

# << String Concatenation
print("\nString Concatenation:")
print("Hello, my name is " + name + " and I am " + str(age) + " years old.")

# << Formatted String with f-Strings (Python 3.6+)
print("\nFormatted String with f-Strings:")
print(f"Hello, my name is {name} and I am {age} years old.")
print(f"My height is {height} meters.")
print(f"In five years, I will be {age + 5} years old.")

# << Formatted String with str.format()
print("\nFormatted String with str.format():")
print("Hello, my name is {} and I am {} years old.".format(name, age))
print("Hello, my name is {0} and I am {1} years old.".format(name, age))
print("In five years, I will be {} years old.".format(age + 5))
print("I am a {1} named {0}.".format(name, occupation))

# << Number Formatting Examples
print("\nNumber Formatting:")
pi = 3.14159
large_number = 1234567890

print("Pi rounded to 2 decimal places: {:.2f}".format(pi))
print(f"Pi rounded to 3 decimal places: {pi:.3f}")
print("Formatted large number without commas: {}".format(large_number))

# << Padding and Alignment with str.format()
print("\nPadding and Alignment:")
print("Name aligned to the left within 10 spaces: {:<10}".format(name))
print("Age aligned to the right within 5 spaces: {:>5}".format(age))
print("Center aligned height within 10 spaces: {:^10.2f}".format(height))

# << Using % Formatting (Older method)
print("\nUsing % Formatting (Legacy):")
print("Hello, my name is %s and I am %d years old." % (name, age))
print("Pi to 2 decimal places: %.2f" % pi)
print("Large number without commas: %d" % large_number)

# << Escape Characters
print("\nEscape Characters:")
print("Hello, my name is \"Bob\" and I am a \"Developer\".")
print("New line character example:\nThis is a new line.")
print("Tab character example:\tThis is tabbed.")

# << Multiline Strings with Triple Quotes
print("\nMultiline Strings:")
long_text = """
Hello! My name is Bob.
I am a Developer.
I am 25 years old and 1.75 meters tall.
"""
print(long_text)

# << Type Conversion Examples
print("\nType Conversion:")
age_str = str(age)  # Convert integer to string
height_int = int(height)  # Convert float to integer
print("String version of age:", age_str)
print("Integer version of height:", height_int)

# << Type Checking
print("\nType Checking:")
print("Type of age:", type(age))
print("Type of height:", type(height))
print("Type of name:", type(name))
