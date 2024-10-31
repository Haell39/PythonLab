
class Microwave:
    def __init__(self, brand: str, power_rating: str) -> None:
        '''
        `self` represents the current instance, so when you create the `bosch` object, `self` refers to the `bosch` instance inside the `__init__` method.

        So, in each instance (`smeg` or `bosch`), `self` adapts to refer to that specific object.

        obs: You can change self to whatever you want like: this, instance, etc.
        '''
        self.brand = brand
        self.power_rating = power_rating

smeg: Microwave = Microwave('Smeg', 'A')
print(smeg)
print(smeg.brand)
print(smeg.power_rating)

bosch: Microwave = Microwave('Bosch', 'B')
print("\n")
print(bosch)
print(bosch.brand)
print(bosch.power_rating)



'''
For example:

class Microwave:
    def __init__(bosch, brand: str, power_rating: str) -> None:
        bosch.brand = brand
        bosch.power_rating = power_rating

'''