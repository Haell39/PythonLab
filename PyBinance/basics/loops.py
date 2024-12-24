#If-else:

print('=============If-else statement============')

def func(n):
    if n % 2 == 0:
        return 'even'
    else:
        return 'odd'

numero = int(input('Enter a number: '))
print(f'The chosen number is {func(numero)}')

# While loop:
print('=============While loop============')

n = int(input('Enter a number fella: '))
while n > 0:
    print(n)
    n -= 1
    input("Press enter to continue...") # the input is just to pause the loop until the user presses enter
    if n == 5:
        break
    print('Countdown finished')

#while loop with continue:

print('=============While loop with continue============')
k = int(input('Enter any number: '))
while k >= -1:
    if k % 2 == 0: # Check if the number is even
        k = k - 1 # Decrement the number
        continue # Skip to the next
    print(k) # Print the number if it's odd
    input('hit enter to continue...') # Wait for user input
    k -= 1 # Decrement again after printing

# For loop:

p = int(input('Give us a number: '))
summ = 0 # Step 2: Initialize the sum variable
for i in range(1, p + 1):  # Step 3: Loop from 1 to p (inclusive)
    summ = summ + i # Step 4: Add the current number to the sum
print(f'The total is {summ}')


names = []
for i in range(1, 5):
    name = input('Enter a name: ')
    names.append(name)
    print(names)


dict = {
    'color': 'blue',
    'brand': 'Fors',
    'Year': 2200
}

for a in dict.keys():
    print(a)
print('')
for a in dict.values():
    print(a)










