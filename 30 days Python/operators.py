# << Arithmetic Operations in Python

# Integers

print('Adiction:', 2 + 55)
print('Subtraction:', 2 - 55)
print('Multiplication:', 2 * 55)
print('Floor Division:', 2 / 55) # Division in python gives floating number
print('Floor Division (2 decimal places):', format(2 / 55, '.2f')) # Division in python gives floating number
print(f'Floor Division Formated: {2 / 55:.2f}')
print('Modulus:', 2 % 55)
print('Exponentiation:', 2 ** 13)
print('Precedence:', 2 + 55 * 5)

print('\n')
# Floating nums

print('Floating num PI: ', 3.14159)
print('Floating num gravity', 9.81)

print('\n')
# Complex nums

print('Complex num: ', 1 +1j)
print('Multiply complex numbers: ', (1 + 1j) * (1 - 1j))

print('\n')
# Declaring the variable at the top first

a = 3 # a is the variable name and 3 is the variable value and type
b = 2 # b is the variable name and 2 is the variable value and type

print('\n')
# Arithmetic operations and assigning the result to a variable

total = a + b
diff = a - b
product = a * b
div = a / b
mod = a % b
exp = a ** b
floorDivision = a // b

# # I should have used sum instead of total but sum is a built-in function try to avoid overriding builtin functions

print(total) ## if you don't label your print with some string, you never know from where is  the result is coming
print('a - b = ', diff)
print('a * b = ', product)
print('a / b = ', div)
print('a % b = ', mod)
print('a ** b = ', exp)
print('a // b = ', floorDivision)

print('\n')
# Declaring values and organizing them together

num_one = 3
num_two = 4

# Arithmetic operations

total = num_one + num_two
diff = num_two - num_one
product = num_one * num_two
div = num_two / num_one
remainder = num_two % num_one

# Printing values with label

print('Total:', total)
print('difference: ', diff)
print('product: ', product)
print('division: ', div)
print('remainder: ', remainder)

# Calculating area of a circle
radius = 10
area_of_circle = 3.14 * radius ** 2
print('Area of a circle: ', area_of_circle)

print('\n')

# Calculating area of a rectangle
length = 10
width = 20
area_of_rectangle = length * width
print('Area of a rectangle: ', area_of_rectangle)

# Calculating a weight of an object
print('\n')

mass = 75
gravity = 9.81
weight = mass * gravity
print('Weight: ', weight, 'N')

print('\n')
# Boolean

print(3 > 2)
print(3 < 2)
print(3 == 2)
print(3 != 2)
print(3 >= 2)
print(3 <= 2)

print(len('mango') == len('avocado'))
print(len('mango') > len('avocado'))
print(len('mango') < len('avocado)'))
print(len('tomato') != len('meat'))
print(len('mango') >= len('meat'))
print(len('milk') <= len('potato'))
print(len('milk') == len('potato'))
print(len('python') == len('dragon'))

# Boolean comparison



