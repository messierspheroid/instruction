from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

# function that is being used as an input
def move_forwards():
    tim.forward(10)


screen.listen()

screen.onkey(key="space", fun=move_forwards)
screen.exitonclick()


# # higher order functions
# def add(n1, n2):
#     return n1 + n2
#
# def subtract(n1, n2):
#     return n1 - n2
#
# def multiply(n1, n2):
#     return n1 * n2
#
# def divide(n1, n2):
#     return n1 / n2
#
# def calculator(n1, n2, func):
#     return func(n1, n2)
#
# # the func calculator is considered the higher order function
# #     bc it's taking another function as an input and working with it inside the body of the function
# result = calculator(2, 3, divide)
# print(result)