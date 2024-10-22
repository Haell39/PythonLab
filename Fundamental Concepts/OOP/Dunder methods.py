class Microwave:
    def __init__(self, brand: str, power_rating: str) -> None:
        self.brand = brand
        self.power_rating = power_rating
        self.is_on = False  # Changed from turnON to is_on to avoid conflict

    def turn_on(self) -> None:  # Changed method name to turn_on
        if self.is_on:
            print(f"The microwave ({self.brand}) is already on!")
        else:
            self.is_on = True
            print(f'The microwave ({self.brand}) is now on!')

    def turn_off(self) -> None:  # Changed method name to turn_off
        if self.is_on:
            self.is_on = False
            print(f'The microwave ({self.brand}) is now off!')
        else:
            print(f"The microwave ({self.brand}) is already off!")

    def run(self, seconds: int) -> None:
        if self.is_on:
            print(f'Running ({self.brand}) for {seconds} seconds')
        else:
            print(f'Turn on your microwave ({self.brand}) first!')

    def __add__(self, other):
        return f'{self.brand} + {other.brand}'
    
    def __mul__(self, other):
        return f'{self.brand} * {other.brand}'
    
    def __str__(self) -> str:
        return f'{self.brand} (Rating: {self.power_rating})'
    
    def __repr__(self) -> str:
        return f'Microwave(brand = "{self.brand})", power_rating = "{self.power_rating}")'

# Testing the class
smeg: Microwave = Microwave('Smeg', 'A')

print("\n")

bosch: Microwave = Microwave('Bosch', 'B')

print(smeg + bosch) # this will throw an error because if __add__ method is not defined

print(smeg * bosch)
print("\n")

print(repr(smeg))
print(repr(bosch))

print("\n")

print(smeg)
print(bosch)
