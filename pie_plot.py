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



#plt.plot(total_sales)
#plt.show()

labels = 'Agora', 'Evolution', 'Silk Road 2', 'Silk Road 1', 'Black Market Reloaded', 'Pandora', 'Hydra'

total_sales = data[column_names[1]].tolist()
del total_sales[0]

sizes = [total_sales[0], total_sales[1], total_sales[2], total_sales[3], total_sales[4], total_sales[5], total_sales[6]]
explode = (0,0,0,0,0,0,0)  # only "explode" the 2nd slice (i.e. 'Hogs')

fig1, ax1 = plt.subplots()
patches, texts, autotexts = ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
        shadow=False, startangle=90)
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
autotexts[4].set_fontsize(8)
autotexts[5].set_fontsize(8)
autotexts[6].set_fontsize(8)

ax1.set_title("Percentage of total goods sold on underground markets, per market \n")


plt.show()