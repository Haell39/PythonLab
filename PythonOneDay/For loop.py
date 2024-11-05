"""
For an in iterable:
    return (a)
"""

pets = ['cats', 'dogs', 'rabbits', 'hamsters']

for myPets in pets:
    print(myPets)

# Is also possible to display the index:
print('\n')
for index, myPets in enumerate(pets):
    print(index,myPets)

message = 'Hello, World!'

for i in message:
    print(i)

# built-in range function:

for i in range(7):
    print(i)