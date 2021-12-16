import turtle as turtle_hirst
import random

crazy = turtle_hirst.Turtle()
screen = turtle_hirst.Screen()
turtle_hirst.speed("fastest")
crazy.hideturtle()
crazy.penup()


turtle_hirst.colormode(255)

color_list = [(240, 231, 221), (228, 152, 86), (120, 171, 203), (1, 0, 0), (40, 111, 159), (240, 201, 83)]
for j in range(10):
    crazy.goto(-200, ((40 * j) - 200))
    for _ in range(10):
        crazy.dot(20, random.choice(color_list))
        crazy.forward(50)


crazy.color('blue')
style = ('Arial', 30, 'italic')
crazy.write('Miltos!', font=style, align='center')
crazy.hideturtle()
screen.exitonclick()
