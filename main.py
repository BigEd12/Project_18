# import colorgram
#
# rgb_colours = []
#
# colours = colorgram.extract('image.jpg', 15)
#
# for colour in colours:
#     r = colour.rgb.r
#     g = colour.rgb.g
#     b = colour.rgb.b
#     new_colour = (r, g, b)
#     rgb_colours.append(new_colour)
#
# print(rgb_colours)

import turtle
from turtle import Turtle, Screen
import random
turtle.colormode(255)
tim = Turtle()


colour_list = [(150, 75, 49), (202, 164, 109), (236, 230, 216), (140, 176, 207), (25, 32, 48), (26, 107, 159),
               (237, 225, 235), (209, 161, 111), (144, 29, 63), (230, 212, 93), (4, 163, 197), (218, 60, 84),
               (229, 79, 43), (195, 130, 169), (54, 168, 114)]


def random_colour():
    return(random.choice(colour_list))


def forward_dots(square_size, spacing, dot_size):
    for _ in range(square_size):
        tim.penup()
        tim.forward(spacing)
        tim.color(random_colour())
        tim.dot(dot_size)


def end_of_row(square_size, spacing):
    tim.back(square_size * spacing)
    tim.left(90)
    tim.forward(spacing)
    tim.right(90)


tim.ht()
tim.speed(0)
tim.setheading(225)
tim.penup()
tim.forward(300)
tim.setheading(0)

for _ in range(10):
    forward_dots(10, 50, 20)
    end_of_row(10, 50)






























screen = Screen()
screen.exitonclick()