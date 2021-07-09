# # *args, define a function and specify an unspecified number of inputs
# def add(*args):
#     print(args[0])
#     total = 0
#     for n in args:
#         total += n
#     return total
#
# print(add(3, 5, 7, 8))

# # *kwargs (keyword arguments), create a dict that represents keyword args and their values
# def calculator(n, **kwargs):
#     print(kwargs)
#     # for key, value in kwargs.items():
#     #     print(key)
#     #     print(value)
#
#     # take 2, then add it to (add=3) and finally multiply (multiply=5)
#     #     (2 + 3) * 5 = 25
#     n += kwargs["add"]
#     n *= kwargs["multiply"]
#     print(n)
#
#
# calculator(2, add=3, multiply=5)

class Car:

    def __init__(self, **kw):
        self.make = kw.get("make")
        self.model = kw.get("model")
        self.color = kw.get("color")
        self.seats = kw.get("seats")

# you have to specify "make" and "model" if you don't use .get
# .get makes it so that attributes are optional
my_car = Car(make="Nissan", model="Skyline")
print(my_car.model)
