import random as r

x = r.randrange(1, 100)
print(x)

from random import randrange, randint

# << OBS: random is a module, randrange and randint are functions(built-in)

a = randrange(1, 10)
b = randint(1, 100)

print(f'A result = {a} \nB result = {b}')
print(a, b, sep= '\n')

# ^^ Creating your own modules

import primemodule
answer = primemodule.isPrime(27)