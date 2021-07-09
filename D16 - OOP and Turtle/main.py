# # in OOP we are trying to model real life objects
# # objects have things (attributes = variables) and can do things (methods = functions)
# # class (e.g, blueprint) contains objects
# #   (what is produced from the blueprint, can be multiple with different attributes)
# #   that all do the same thing
# # SYNTAX - car = CarBlueprint() == object = Class(functions that activates construction of the object)
# #   car.speed == object.attribute
# #   car.stop() == object.method
# import another_module
# # print(another_module.another_variable)
#
# from turtle import Turtle, Screen
#
# # create a new object from a class
# timmy = Turtle()
# print(timmy)
#
# # call methods that are associated with the object, object.method()
# timmy.shape("turtle")
# timmy.color("coral")
#
# timmy.forward(100)
#
# my_screen = Screen()
# # how to access its attributes using object.attribute
# print(my_screen.canvheight)
# my_screen.exitonclick()

from prettytable import PrettyTable

table = PrettyTable()

table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"])
table.add_column("Type", ["Electric", "Water", "Fire"])

# align from center to left
table.align = "l"
print(table)
