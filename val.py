# carbon_data = []
# f = open('co2.csv', 'r')
# file = f.read()
# rows = file.split('\n')
# print(file)
# for each in rows:
#     split_row = each.split(",")
#     carbon_data.append(split_row)
    
# # print(carbon_data[0:len(carbon_data)])

# carbon = []

# for row in carbon_data:
#     value0 = (row[0])
    
#     carbon.append(value0)
#     # carbon.append(value1)
# print(carbon[0:len(carbon)])

import matplotlib.pyplot as plt
import csv

x = []
y = []

with open('co2.csv','r') as csvfile:
    plots = csv.reader(csvfile, delimiter=',')
    for row in plots:
        x.append(float(row[0]))
        y.append(float(row[1]))

print(x)
print(y)