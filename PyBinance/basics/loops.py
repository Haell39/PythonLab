#If-else:

print('If-else:')

def func(n):
    if n % 2 == 0:
        return 'even'
    else:
        return 'odd'

numero = func(5)
print(f'The chosen number is {numero}')

# While loop:

n = int(input('Enter a number fella: '))
while n > 0:
    print(n)
    n -= 1
    input("Press enter to continue...") # the input is just to pause the loop until the user presses enter
    print('Countdown finished')

    
