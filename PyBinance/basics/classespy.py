class Car:
    def __init__(self, color,brand,model):
        self.color = color
        self.brand = brand
        self.model = model

    def get_values(self):
        print(f'The color is {self.color} brand is {self.brand} and the model is {self.model}')

    def drive(self):
        print('I m driving...')

    def stop(self):
        print('brakes applies...')