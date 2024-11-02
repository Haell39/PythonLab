# ^^ Tuples are an essential data type in Python that represent an ordered, immutable collection of items.

# 1. Creating Tuples
my_tuple = (1, 2, 3, 4, 5, 10)  # A tuple with multiple items
single_item_tuple = (5,)  # A single-item tuple (notice the trailing comma)
empty_tuple = ()  # An empty tuple

# 2. Accessing Tuple Elements
print("Accessing Tuple Elements:")
print(my_tuple[0])    # Output: '1'
print(my_tuple[1:3])  # Output: (2, 3)
print(my_tuple[0:5:2]) # 2 is the step
print(my_tuple[-1]) # last elemnt

# 3. Immutability of Tuples
print("\nImmutability of Tuples:")
# Once created, you cannot modify a tuple.
# Uncommenting the next line will raise a TypeError
# my_tuple[0] = 5  

# 4. Tuple Packing and Unpacking
print("\nTuple Packing and Unpacking:")
my_tuple = ("Alice", 25, "Engineer")  # Packing values into a tuple
name, age, profession = my_tuple      # Unpacking values into variables
print(name)        # Output: "Alice"
print(profession)  # Output: "Engineer"
print(f'My teacher {name} is also an {profession}')

# 5. Using Tuples for Multiple Returns
print("\nUsing Tuples for Multiple Returns:")
def get_user_info():
    return "Alice", 25, "Engineer"  # Returning multiple values as a tuple

user_info = get_user_info()
print(user_info)  # Output: ('Alice', 25, 'Engineer')

# 6. Common Tuple Operations
print("\nCommon Tuple Operations:")
another_tuple = (4, 5)
print("Length:", len(my_tuple))                   # Length of the tuple
print("Concatenation:", my_tuple + another_tuple) # Concatenation of two tuples
print("Repetition:", my_tuple * 2)                # Repeating the tuple
print("Membership:", 'a' in my_tuple)            # Checking membership (will return False)

# 7. Using Tuples as Dictionary Keys
print("\nUsing Tuples as Dictionary Keys:")
location = {(40.7128, -74.0060): "New York"}      # Tuple as a dictionary key
print(location[(40.7128, -74.0060)])              # Output: "New York"

""" 
Summary of Key Points:

- Immutable: Tuples cannot be changed after creation.
- Ordered: Tuples maintain the order of elements.
- Packing/Unpacking: Efficient ways to group or distribute values.
- Useful in Function Returns: Great for returning multiple values.

Conclusion:
Tuples are a powerful tool in Python, especially when working with data that should remain constant. 
"""