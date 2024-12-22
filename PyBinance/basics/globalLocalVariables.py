x = 6 # --> Global variable

def func():
    x = 10
    print(x) # --> Local variable

func() # --> local variable
print(x) # --> Global variable


def globalVar():
    global y
    y = 'Now I m global'
    print(y)

globalVar()
print(y)  # both will print now, because og the global keyword

k = 8
def funcA():
    global k
    k = 7
    print(k)

# the output continues to be 7
funcA()
print(k)
