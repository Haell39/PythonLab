# Condition Statement:

"""
Not equals: 5 != 2
Greater than: 5>2
Smaller than: 2<5
Greater than or equals to: 5>=2
5>=5
Smaller than or equals to: 2 <= 5
2 <= 2
"""

'''
Logical operators: and, or, not
'''

'''
== -> Python will check if two values are equal
= -> Assignment operator
'''

# if statement

print("Discover if your number is even or odd: ")

age = int(input("Enter your age: "))
if age % 2 == 0:
    print("Your age is Even!")
else:
    print("Your age is Odd!")

# Inline if

myInt = 5
num1 = 12 if myInt == 10 else 13
print(num1)

#Exp 2:
print("This is task A" if myInt == 5 else "This is task B")













