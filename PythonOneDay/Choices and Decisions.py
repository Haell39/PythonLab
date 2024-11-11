# << Condition Statement:

'''
Not equals: 5 != 2
Greater than: 5>2
Smaller than: 2<5
Greater than or equals to: 5>=2
5>=5
Smaller than or equals to: 2 <= 5
2 <= 2
'''

'''
Logical operators: and, or, not
'''

'''
== -> Python will check if two values are equal
= -> Assignment operator
'''

# ^^ if statement

userInput = int(input("Enter a number: "))
if userInput % 2 == 0:
    print("The number is even")
else:
    print("The number is odd")

# ^^ inline if statement

print("Even number") if userInput % 2 == 0 else print("Odd number")


myint = int(input("Enter a number: "))
num = 12 if myint == 0 else 13
print(num)