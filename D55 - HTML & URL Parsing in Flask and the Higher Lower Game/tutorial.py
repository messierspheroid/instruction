# from flask import Flask
#
# app = Flask(__name__)
#
#
# @app.route('/')
# def hello_world():
#     return '<h1 style="text-align: center">Hello, World!</h1>' \
#            '<p>This is a paragraph</p>' \
#            '<img src="https://media.giphy.com/media/3oriO0OEd9QIDdllqo/giphy.gif" width=200>'
#
#
# def make_bold(function):
#     def wrapper():
#         return "<b>" + function() + "</b>"
#     return wrapper
#
#
# def make_emphasis(function):
#     def wrapper():
#         return "<em>" + function() + "</em>"
#     return wrapper
#
#
# def make_underlined(function):
#     def wrapper():
#         return "<u>" + function() + "</u>"
#     return wrapper
#
#
# # different routs using the app route decorator
# @app.route('/bye')
# @make_bold
# @make_emphasis
# @make_underlined
# def bye():
#     return 'Bye!'
#
#
# # creating variable paths and converting the path to a specified data type
# @app.route('/username/<name>/<int:number>')
# def greet(name, number):
#     return f'Hello there {name}, you are {number} years old!'
#
#
# if __name__ == '__main__':
#     app.run(debug=True)


# class User:
#     def __init__(self, name):
#         self.name = name
#         self.is_logged_in = False
#
#
# def is_authenticated_decorator(function):
#     def wrapper(*args, **kwargs):
#         if args[0].is_logged_in:
#             function(args[0])
#     return wrapper
#
#
# @is_authenticated_decorator
# def create_blog_post(user):
#     print(f"This is {user.name}'s new blog post.")
#
#
# new_user = User("Angela")
# new_user.is_logged_in = True
# create_blog_post(new_user)

# # modify code without changing the code
# def func(f):
#     def wrapper(*args, **kwargs):
#         print("Started")
#         rv = f(*args, **kwargs)
#         print("Ended")
#         return rv
#
#     return wrapper
#
#
# @func
# def func2(x, y):
#     print(x)
#     return y
#
#
# @func
# def func3():
#     print("i am func3")
#
#
# x = func2(5, 6)
# print(x)

# # another example
# import time
#
#
# def timer(func):
#     def wrapper(*args, **kwargs):
#         start = time.time()
#         rv = func()
#         total = time.time() - start
#         print("Time:", total)
#         return rv
#
#     return wrapper
#
#
# @timer
# def test():
#     for _ in range(1000):
#         pass
#
#
# @timer
# def test2():
#     time.sleep(2)
#
#
# test()
# test2()


def logging_decorator(function):
    def wrapper(*args, **kwargs):
        print(f"You called {function.__name__}({args})")
        print(f"It returned:", function(1, 2, 3))
    return wrapper


@logging_decorator
def a_function(x, y, z):
    return x+y+z


a_function(1, 2, 3)