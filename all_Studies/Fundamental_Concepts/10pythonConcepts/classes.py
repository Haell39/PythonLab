class Car:
    def __init__(self, color: str, horsepower: int) -> None:
        self.color = color
        self.horsepower = horsepower

BMW: Car = Car("Gray", 330)
print(BMW.color, BMW.horsepower)
print(f"The BMW is {BMW.color} and has {BMW.horsepower}hp")

Volvo: Car = Car("White", 250)
print(f"The volvo is {Volvo.color}, and has {Volvo.horsepower}hp")

