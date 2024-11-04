# Dictionary is a collection of related data PAIRS

myDict = {'Peter':38, 'John':45, 'Jana':29}

# keys must be unique (within one dictionary)

myDict = {'Peter':38, 'John':45, 'Jana':29, 'Jana':30}  # Overwrites the previous value

# You can also do:

userNameandAge = dict(Peter = 38, Alvin = 45, Elvin = 29)
print(userNameandAge['Alvin'])

userNameandAge['Alvin'] = 27
print(userNameandAge['Alvin'])

userNameandAge['Joe'] = 33
print(userNameandAge)

# Is also possible to create an empty dictionary and add elements to it:
myDict = dict()
myDict['Peter'] = 38
myDict['John'] = 45
myDict['Jana'] = 29
print(myDict)

# You can also do things like these:

myDict2 = {'One':1.35, 2.5:'Two point five', 3:'+',7.9:2}
print(myDict2)

print(myDict2['One'])
print(myDict2[7.9])
myDict2[2.5] = 'Two and a half'
print(myDict2[2.5])

myDict2['New Item'] = 'New Value'
print(myDict2)

del myDict2['New Item']
print(myDict2)