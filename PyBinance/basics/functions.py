import math

def func():
    msg = 'Re-Learning functions in Python 2'
    return msg

print(func())

def mult(x1, x2):
    return  x1 * x2

print(mult(45, 7))

def square(n):
    x = n ** 2
    print(x)

square(78)

def sqrt(e):
    p = math.sqrt(e)
    print(p)

sqrt(64)

def sqrtB(k):
    return math.sqrt(k)

print(f'A raiz quadrade de 225 é: {sqrtB(225)}')


def find_mean(a, b, c):
    return (a + b + c) / 3

print(f'A media inteira dos 3 valores é: {round(find_mean(50,30,90))}')

# or if its wanted the decimal cases:

def findMean(j,k,l):
    return (j + k + l) / 3

media = findMean(50,30,90)
print(f'A media com decimal é: {media:.2f}')



















