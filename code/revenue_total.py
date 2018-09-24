import os
import _csv as csv
import numpy as np
import matplotlib.pyplot as plt
from pandas import read_csv
from collections import Counter

#######################Reading in data#######################
print("Start reading file")
dir_path = os.path.dirname(os.path.realpath(__file__))
file_ = dir_path + '/feedbacks.csv'
column_names = ['hash_str','category','marketplace','item_hash','date','giver_hash','receiver_hash','message','order_title', 'feedback_value', 'order_amount_usd']

data = read_csv(file_, names=column_names)
print("Finished reading file")
#############################################################

#Preparing all column data

labels = data[column_names[4]].tolist()
del labels[0]
money = data[column_names[10]].tolist()
del money[0]

#Stripping of the rest of the date and only keeping the year
for i in range(len(labels)):
	labels[i] = str(labels[i])[:4]


#Getting the unique labels to be used in the graph in sorted order from low to high
unique_labels = []
for label_number in range(len(labels)):
	if labels[label_number] not in unique_labels:
		unique_labels.append(labels[label_number])
unique_labels.sort()
print("Finished finding the unique labels")


money_per_year = [0 for i in range(len(unique_labels))]

for i in range(len(money)):
	money_per_year[unique_labels.index(labels[i])] = money_per_year[unique_labels.index(labels[i])] + float(money[i])


plt.xlabel('Year', fontsize=10)
plt.ylabel('Total order value (USD)', fontsize=10)
plt.title('Total order value per year')
plt.plot(unique_labels, money_per_year)
plt.legend(loc='best')
plt.show()

del money
del labels
del data

