import colorgram
from turtle import Turtle, Screen
import turtle as t
import random

timmy = Turtle()
screen = Screen()
timmy.speed('fastest')
t.colormode(255)

colors = colorgram.extract('image.jpg', 30)

list_of_rgb_color = []


def get_rgb_color_from_image(number_of_color):
    r = colors[number_of_color].rgb[0]
    g = colors[number_of_color].rgb[1]
    b = colors[number_of_color].rgb[2]
    rgb = (r, g, b)

    return rgb


for i in range(30):
    new_val = get_rgb_color_from_image(i)
    list_of_rgb_color.append(new_val)

timmy.penup()
timmy.setheading(125)
timmy.forward(300)
timmy.setheading(0)


def create_a_row():
    for _ in range(10):
        timmy.dot(20, random.choice(list_of_rgb_color))
        timmy.penup()
        timmy.forward(50)


def turn_right():
    timmy.right(90)
    timmy.forward(50)
    timmy.right(90)


def turn_left():
    timmy.left(90)
    timmy.forward(40)
    timmy.left(90)


for _ in range(5):
    create_a_row()
    turn_right()
    create_a_row()
    turn_left()

screen.exitonclick()

'''pro code'''

# import turtle as turtle_module
# import random
#
# turtle_module.colormode(255)
# tim = turtle_module.Turtle()
# tim.speed("fastest")
# tim.penup()
# tim.hideturtle()
# color_list = [(202, 164, 109), (238, 240, 245), (150, 75, 49), (223, 201, 135), (52, 93, 124), (172, 154, 40), (140, 30, 19), (133, 163, 185), (198, 91, 71), (46, 122, 86), (72, 43, 35), (145, 178, 148), (13, 99, 71), (233, 175, 164), (161, 142, 158), (105, 74, 77), (55, 46, 50), (183, 205, 171), (36, 60, 74), (18, 86, 90), (81, 148, 129), (148, 17, 20), (14, 70, 64), (30, 68, 100), (107, 127, 153), (174, 94, 97), (176, 192, 209)]
# tim.setheading(225)
# tim.forward(300)
# tim.setheading(0)
# number_of_dots = 100
#
# for dot_count in range(1, number_of_dots + 1):
#     tim.dot(20, random.choice(color_list))
#     tim.forward(50)
#
#     if dot_count % 10 == 0:
#         tim.setheading(90)
#         tim.forward(50)
#         tim.setheading(180)
#         tim.forward(500)
#         tim.setheading(0)
#
#
#
#
#
#
#
#
#
# screen = turtle_module.Screen()
# screen.exitonclick()
