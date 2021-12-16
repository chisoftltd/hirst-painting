import turtle as turtle_hirst
import random
from turtle import Screen

screen = Screen()

turtle_hirst.colormode(255)
crazy = turtle_hirst.Turtle()
color_list = [(240, 231, 221), (228, 152, 86), (120, 171, 203), (1, 0, 0), (40, 111, 159), (240, 201, 83)]
for j in range(10):
    crazy.penup()
    crazy.goto(-100, 40 * j)
    for _ in range(10):
        crazy.penup()
        crazy.dot(20, random.choice(color_list))
        crazy.forward(35)


screen.exitonclick()
