# class ClassName: <-- PascalCase
# camelCase and snake_case

# attributes are something the object has
# methods are what an object does

class User:
    # # finishing out the class without content
    # pass

    # initialize attributes -- def __init_(self, parameters,.....)
    #   self.attribute = parameter
    # constructor == __init__ function
    def __init__(self, user_id, username):
        self.id = user_id
        self.username = username
        # 0 is a default value
        self.followers = 0
        self.following = 0

    # a method always needs to have a self parameter
    def follow(self, user):
        user.followers += 1
        self.following += 1




# piece-wise (input 1x1)
user_1 = User("001", "Angela")
user_2 = User("002", "Jack")

user_1.follow(user_2)

print(user_1.followers)
print(user_1.following)

print(user_2.followers)
print(user_2.following)
