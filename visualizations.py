import os
import _csv as csv
import numpy as np
import matplotlib.pyplot as plt
from pandas import read_csv

#######################Reading in data#######################
print("Start reading file")
dir_path = "marketplace.csv"
column_names = ['name','total_sales','last_90','last_30','last_7','first_observed','last_observed','csv','coveragecsv']
data = read_csv(dir_path, names=column_names)
print("Finished reading file")
#############################################################

labels = data['name'].tolist()
del labels[0]
num_sales = data['total_sales'].tolist()
del num_sales[0]

for i in range(len(num_sales)):
    num_sales[i] = int(float(num_sales[i]))

total_goods_sold = sum(num_sales)

for i in range(len(num_sales)):
    num_sales[i] = num_sales[i] / total_goods_sold

X = labels
Y = num_sales

_X = np.arange(len(X))

plt.bar(_X, Y)
plt.xticks(_X, X) # set labels manually

plt.xlabel('Market', fontsize=10)
plt.ylabel('Percentage', fontsize=10)
plt.title('Percentage of total goods sold on underground markets, per market')

plt.show()

