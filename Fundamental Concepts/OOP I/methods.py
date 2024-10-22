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

# Testing the class
smeg: Microwave = Microwave('Smeg', 'A')
smeg.turn_on()
smeg.turn_on()
smeg.run(10)
smeg.turn_off()
smeg.run(10)
print("\n")

bosch: Microwave = Microwave('Bosch', 'B')
bosch.turn_on()
bosch.turn_off()
bosch.run(10)
