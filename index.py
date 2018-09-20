import os
import _csv as csv
import numpy as np
import matplotlib.pyplot as plt
from pandas import read_csv

#######################Reading in data#######################
print("Start reading file")
dir_path = os.path.dirname(os.path.realpath(__file__))
file_ = dir_path + '/marketplace.csv'
column_names = ['name','total_sales','last_90','last_30','last_7','first_observed','last_observed','csv','coveragecsv']
data = read_csv(file_, names=column_names)
print("Finished reading file")
#############################################################

total_sales = data[column_names[1]].tolist()
del total_sales[0]




plt.plot(total_sales)
plt.show()
