# Tuples are lists that are immutable

months = ('January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December')

myTupple = (1,2,3)
singleItemTupple = (1,)
emptyTupple = ()

print(myTupple)

# Accessing tupple elements

my_tupple = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z')

print(my_tupple[0]) # will return a
print(my_tupple[-1]) # will return z
print(my_tupple[0:3]) # will return a, b, c, 3 is the end(exclusive)
print(my_tupple[0:6:2]) # will return a, c, e, 2 is the step

'''
Once created, you cannot modify a tuple (no adding, removing, or changing items).
This makes tuples useful for storing fixed data.
'''
#my_tupple[0] = 5  # This will raise a TypeError

# Packing and Unpacking

tuple = ('Alice', 25, "Engineer", True)
name, age, profession, is_active = tuple

print(name)
print(profession)
print(f'The age of {name} is {age} and her status is {is_active}.')

# Multiple Returns

def get_user_info():
    return ('Alice', 25, "Engineer", True)

user_info = get_user_info()
print(user_info)

# Tuple common operations

'''
Length: len(my_tuple)
Concatenation: my_tuple + another_tuple
Repetition: my_tuple * 3
Membership: 'a' in my_tuple
'''

# Tuples as keys in dictionaries

location = {(40.7128, -74.0060): "New York City"}
print(location[(40.7128, -74.0060)])

'''
Summary of Key Points:

Immutable: Tuples cannot be changed after creation.
Ordered: Tuples maintain the order of elements.
Packing/Unpacking: Efficient ways to group or distribute values.
Useful in Function Returns: Great for returning multiple values.
Tuples are a powerful tool in Python, especially when working with data that should remain constant. Let me know if you’d like more examples!
'''

