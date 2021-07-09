student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 76, 98],
}

# # looping through dictionaries
# for (key, value) in student_dict.items():
#     print(key)
#     print(value)

import pandas

student_data_frame = pandas.DataFrame(student_dict)
# print(student_data_frame)

# # loop through a data frame is not time efficient bc pandas has its own built in for loop func
# for (key, value) in student_data_frame.items():
#     print(key)
#     print(value)

# # loop through rows of a data frame
# for (index, row) in student_data_frame.iterrows():
#     # print(index)
#     # this provides an overview of the DataFrame
#     # each row is a pandas series object
#     if row.student == "Angela":
#         print(row.score)


# new_dict = {new_key: new_value for (key, value) in dict.items() if test}
