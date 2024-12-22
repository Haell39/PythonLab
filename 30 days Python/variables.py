# ^^ Variables in python

firstName = "Rafael"
lastName = "Andrade"
age = 24
city = "Sao Paulo"
isMarried = False
isProgrammer = True
skills = ["Python", "Java", "C++", "C#"]
personInfo = {
    'firstname':'Rafael',
    'lastname':'Andrade',
    'age':24,
    'city':'Sao Paulo'
}

# ^^ Printing the values stored in the variables

print(firstName)
print(lastName)
print(age)
print(city)
print(isMarried)
print(isProgrammer)
print(skills)
print(personInfo, '\n')
print('Person information', personInfo)

# ^^ Declaring multiple variables in one line
print('\n' + '-----------------------------------------------------------')
first_name, last_name, country, age, is_married = 'Rael', 'Saint', 'Brazil', 27, True

print(first_name, last_name, country, age, is_married)