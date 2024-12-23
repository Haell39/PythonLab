
#lists = multiple values in a single variable

#negative index --> -3  -2  -1
letters = ['a', 'b', 'c']
#positive index --> 0   1   2

print(letters[1])
print(letters[-2])

x = ['a', 'b', 'c', 'd', 'e', 'f', 'g']

x.append("A") #adds to the end of the list
print(x)

x.insert(-1, "B")
print(x)

x.remove('c')
print(x)

x.pop()
print(x)

x.pop(0)
print(x)

# extending lists

y = [1,2,3]
x.extend(y)
print(x)







