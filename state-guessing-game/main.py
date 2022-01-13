# # with open("C:/Users/taprawat/PycharmProjects/pythonProjectday25/weather_data.csv","r") as data:
# #     templist=data.readlines()
# #     print(templist)
#
# # import csv
# #
# # with open("weather_data.csv") as data_file:
# #     data = csv.reader(data_file)
# #     temperatures = []
# #     for row in data:
# #         if row[1] != "temp":
# #             temperatures.append(int(row[1]))
# #
# #     print(temperatures)
#
# import pandas
#
# data = pandas.read_csv("weather_data.csv")
# # print( data[data.temp==data.temp.max()])
# monday=data[data.day=="Monday"]
# print(monday.temp*1.8+32)

import pandas

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
grey_squirrel = len(data[data["Primary Fur Color"] == "Gray"])
red_squirrel = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirrel = len(data[data["Primary Fur Color"] == "Black"])
print(grey_squirrel)
print(red_squirrel)
print(black_squirrel)

dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [grey_squirrel, red_squirrel, black_squirrel]
}
print(dict)
df=pandas.DataFrame(dict)
print(df)
df.to_csv("my_squirrel_data.csv")

