import turtle as tu
import colorsys as cs


tu.setup(700, 840, startx=100, starty=100)
tu.speed(1)
tu.tracer(10)
tu.width(2)
tu.bgcolor("black")


for j in range(25):  
    for i in range(15):  
        
        tu.color(cs.hsv_to_rgb(i / 15, i / 25, 1))  
        
        tu.right(90)
        tu.circle(200 - j * 4, 90)  
        tu.left(90)
        tu.circle(200 - j * 4, 90)  
        tu.right(180)
        tu.circle(50, 24)  


tu.hideturtle()
tu.done()