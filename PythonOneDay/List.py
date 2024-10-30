
listName = ['apple', 'banana', 'cherry']
listName2 = [5, 6, 7]
print(listName, listName2, sep='\n')

# Understandin indexes:

userAge = [21, 22, 23, 24, 25]
print(userAge[0]) # indexes starts at 0
print(userAge[-1])  # -1 will print the last element and so on backwards -1, -2, -3, -4, -5 --> Outputs: 25, 24, 23, 22, 21

'''
You can assign a list, or part of it, to a variable. If you write userAge2 = userAge, the variable userAge2 becomes [21, 22, 23, 24, 25].

If you write userAge3 = userAge[2:4], you are assigning items with
index 2 to index 4-1 from the list userAge to the list userAge3. In other
words, userAge3 = [23, 24].

'''
print("Assigning a list, or part of it, to a variable:")
userAge2 = userAge
userAge3 = userAge[2:4]
print(userAge2, userAge3, sep='\n')
'''
Hence the notation 2:4 refers to items from index 2 to index 4-1 (i.e. index 3), which is why userAge3 = [23, 24]
and not [23, 24, 25].

'''

print("Slice notation and stepper:")

userAge = [21, 22, 23, 24, 25]
userAge4 = userAge[1:5:2]  # [start:stop:step]
print(userAge4) #we will get a sub list consisting of every second number from index 1 to index 5-1 because the stepper is 2!

'''

For instance, userAge[ :4] gives you values from index
0 to index 4-1 while userAge[1: ] gives you values from index 1 to
index 5-1 (since the size of userAge is 5, i.e. userAge has 5 items).

'''

print("Modifying, Adding and Deleting a list:")

userAge = [21, 22, 23, 24, 25]
userAge[0] = 20
print(userAge)

userAge.append(99)  # append will add 99 to the end of the list
print(userAge)

userAge.remove(23)  # remove will remove the item at index 2
del userAge[-1]
print(userAge)

print("Testing more things:")

listA = [1, 2, 3, 6, 12, 24, 36, 48, 60, 72, 84, 96]

listA.append("Text")  # append will add "Text" to the end of the list
print(listA[-1])





















