newText = 'Hello World!'.replace("World", "Python")
print(newText)

# Defininf your own function

def isPrime(n):
    if n < 2:
        return False
    for x in range(2, int(n ** 0.5) + 1):
        if n % x == 0:
            return False
    return True
    
 
answer = isPrime(27)
print(answer)

# Variable scope

"""
Firstly, any variable declared inside a function is only accessible within
the function. These are known as local variables. Any variable declared
outside a function is known as a global variable and is accessible
anywhere in the program.

"""

message1 = "Gloabal Variable"

def myFunction():
    message2 = "Local Variable"
    print(message1)
    print(message2)

myFunction()
print(message1) # ^^ message2 is not accessible outside the function

"""
The second concept to understand about variable scope is that if a local
variable shares the same name as a global variable, any code inside the
function is accessing the local variable. Any code outside is accessing
the global variable.
"""

test1 = 'global variable'

def testFunction():
    test1 = 'local variable'
    print(test1)

testFunction()
print(test1)
