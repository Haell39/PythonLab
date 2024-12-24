from classespy import Car



car1 = Car('White', 'Toyota', 'Corolla')
car2 = Car('Red', 'Honda', 'Civic')

print(car2.color)
print(car1.brand)

car1.get_values()
car2.get_values()
car1.drive()
car1.stop()