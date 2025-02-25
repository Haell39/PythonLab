from datetime import datetime

def show_date() -> None:
    print("Current Date and Time:", datetime.now())

show_date()

def add(x: int, y: int) -> int:
    sum = x + y
    print(sum)

add(5, 6)

def greet(name: str) -> None:
    print(f'Hello, {name}!')

greet('Rafel')
greet('Bob')