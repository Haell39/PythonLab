from typing import Self

class Car:
    def __init__(self, brand: str, horsepower: int) -> None:
        self.brand = brand
        self.horsepower = horsepower

    def __str__(self):
        return f'{self.brand} with {self.horsepower}hp'
    
    def __add__(self, other: Self) -> str:
        return f"{self.brand} & {other.brand}"

volvo: Car = Car("Volvo", 250)
print(volvo) # This will print the address of the object, not the object itself if __str__ is not defined(dunder method)

BMW: Car = Car("BMW", 330)

print(volvo + BMW)


