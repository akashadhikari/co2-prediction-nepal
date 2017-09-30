import matplotlib.pyplot as plt
import csv

x = []
y = []

with open('co2.csv','r') as csvfile:
    plots = csv.reader(csvfile, delimiter=',')
    for row in plots:
        x.append(float(row[0]))
        y.append(float(row[1]))

plt.plot(x,y, label='Emission values')
plt.xlabel('Year')
plt.ylabel('Emission')
plt.title('Carbon-dioxide Emission\n(metric tons per capita)')
plt.legend()
plt.show()