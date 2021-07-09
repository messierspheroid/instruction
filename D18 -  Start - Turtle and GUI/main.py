import turtle as t
import random

tim = t.Turtle()
t.colormode(255)

tim.shape("turtle")

# # beginner
# tim.right(90)
# tim.forward(100)
# tim.right(90)
# tim.forward(100)
# tim.right(90)
# tim.forward(100)
# tim.right(90)
# tim.forward(100)

# # draw square
# for _ in range(4):
#     tim.forward(100)
#     tim.right(90)

# import basics
## import turtle
### from turtle import Turtle (!THIS IS THE BEST PRACTICE!)
#### from turtle import * <---- imports everything from the module (unlikely)

# alias module
##import turtle as t (t = alias)

# installing modules
##import heroes <--- this has to be installed

# # dash (50 * (pd 10, pu 10))
# for _ in range(15):
#     tim.pendown()
#     tim.forward(10)
#     tim.penup()
#     tim.forward(10)

# # tri to dec alt color w/100 line side length
# colors = ["red", "green", "blue", "orange", "purple", "pink", "yellow"]
#
# def draw_shape(num_sides):
#     angle = 360 / num_sides
#
#     for _ in range(num_sides):
#         tim.right(angle)
#         tim.forward(100)
#
# for shape_side_n in range(3,11):
#     tim.color(random.choice(colors))
#     draw_shape(shape_side_n)

# random walk, colors, increased thickness and speed, move = 10
# def random_color():
#     r = random.randint(0, 255)
#     g = random.randint(0, 255)
#     b = random.randint(0, 255)
#     random_color = (r, g, b)
#     return random_color
#
# directions = [0, 90, 180, 270]
#
# for _ in range(200):
#     tim.speed(0)
#     tim.pensize(10)
#     tim.color(random_color())
#     tim.forward(30)
#     tim.setheading(random.choice(directions))

# make a spirograph
def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color

tim.speed(0)

def draw_spirograph(size_of_gap):
    for _ in  range(int(360 / size_of_gap)):
        tim.color(random_color())
        tim.circle(100)
        tim.setheading(tim.heading() + size_of_gap)

draw_spirograph(5)

screen = t.Screen()
screen.exitonclick()