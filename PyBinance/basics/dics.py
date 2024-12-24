# Dics are an ordered collection of items

car = {
    'brand': 'Ford',
    'color': 'white',
    'year': 2020
}

print(car.keys())
print(car.values())

print(car['year'])

# adding a new key value pair

car['country'] = 'USA'
print(car)

car.pop('color')
print(car)