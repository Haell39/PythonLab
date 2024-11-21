import turtle

tela = turtle.Screen()
tela.bgcolor("black")
tartaruga = turtle.Turtle()
tartaruga.color("yellow")
tartaruga.speed(10)

for i in range(36):
    for j in range(5):
        tartaruga.forward(100)
        tartaruga.right(144)
    tartaruga.right(10)

tela.mainloop()