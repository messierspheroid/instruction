# with open("./weather_data.csv") as data_file:
#     data = data_file.readlines()
#     print(data)

# import csv
#
# with open("./weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#     print(temperatures)

import pandas

data = pandas.read_csv("./weather_data.csv")
# # two types of "types", series and dataframes
# # this is a dataframe, two-dimensional
# print(type(data))
# # this is a series, one-dimensional
# print(type(data["temp"]))
#
# data_dict = data.to_dict()
# print(data_dict)
#
# temp_list = data["temp"].to_list()
# print(temp_list)
#
# print(len(temp_list))
#
# temp_sum = sum(temp_list)
# quantity = len(temp_list)
# average_temp = temp_sum/quantity
# print(average_temp)
#
# print(data["temp"].mean())
#
# print(data["temp"].max())
#
# # get data in columns
print(data["condition"])
# print(data.condition)

# get data in rows
# print(data[data["day"] == "Monday"])
# print(data[data["temp"] == data["temp"].max()])

# monday = data[data["day"] == "Monday"]
# # print(monday.condition)
#
# monday_temp = int(monday["temp"])
# temp_f = (monday_temp * 9/5) + 32
# print(temp_f)
#
# # create a dataframe from scratch
# data_dict = {
#     "students": ["Amy", "James", "Angela"],
#     "scores": [76, 56, 65]
# }
#
# data = pandas.DataFrame(data_dict)
# # save to csv
# data.to_csv("./new_data.csv")

data = pandas.read_csv("./2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
gray_count = len(data[data["Primary Fur Color"] == "Gray"])
black_count = len(data[data["Primary Fur Color"] == "Black"])
cinnamon_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
data_dict = {
    "Primary Fur Colors": ["Gray", "Black", "Cinnamon"],
    "Count": [gray_count, black_count, cinnamon_count],
}
df = pandas.DataFrame(data_dict)
df.to_csv("squirrel_count.csv")
