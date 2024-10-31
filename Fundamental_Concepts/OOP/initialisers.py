
class Microwave:
    def __init__(self, brand: str, power_rating: str) -> None:
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