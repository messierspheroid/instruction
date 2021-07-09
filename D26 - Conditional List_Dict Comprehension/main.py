# # List comprehension
# # for loop
# numbers = [1, 2, 3]
# new_list = []
# for n in numbers:
#     add_1 += 1
#     new_list.append(add_1)

# # instead
# new_list = [new_item for item in list]
# # for example....
# numbers = [1, 2, 3]
# new_list = [n + 1 for n in numbers]

# name = "Chad"
# letters_list = []
# new_list = [letter for letter in name]

# doubled = [n * 2 for n in range(1, 5)]

# conditional list comprehension
# new_list = [new_item for item in list if test]

# names = ["Alex", "Beth", "Caroline", "Dave", "Elanor", "Freddie"]
# long_names = [name.upper() for name in names if len(name) > 5]
# print(long_names)

# numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
# result = [num for num in numbers if num % 2 == 0]
# print(result)

# # dictionary comprehension
# new_dict = {new_key: new_value for item in list}
# new_dict = {new_key: new_value for (key, value) in dict.items()}
# new_dict = {new_key: new_value for (index, row) in df.iterrows()}
# new_dict = {new_key: new_value for (key, value) in dict.items() if test}

# import random
#
# names = ["Alex", "Beth", "Caroline", "Dave", "Elanor", "Freddie"]

# # remember lists use only ["value] and dictionaries initiate with {"key": value}
#
# student_scores = {student: random.randint(1, 100) for student in names}
# passed_students = {student: score for (student, score) in student_scores.items() if score >= 60}
#
# print(passed_students)

# # Exercise 1
# sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
#
# result = {word: len(word) for word in sentence.split()}
#
# print(result)

# # Exercise 2
# weather_c = {
#     "Monday": 12,
#     "Tuesday": 14,
#     "Wednesday": 15,
#     "Thursday": 14,
#     "Friday": 21,
#     "Saturday": 22,
#     "Sunday": 24,
# }
#
# weather_f = {day: (temp_c * 9/5) + 32  for (day, temp_c) in weather_c.items() }
#
# print(weather_f)
