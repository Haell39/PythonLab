class Car:
    def __init__(self, brand: str, horsepower: int) -> None:
        self.brand = brand
        self.horsepower = horsepower

    def run(self) -> None:
        print(f'{self.brand} is running')
    
    def get_info(self) -> None:
        print(f'{self.brand} with {self.horsepower}hp')

# self refers to the instance

volvo: Car = Car('Volvo', 250)
volvo.run()
volvo.get_info()