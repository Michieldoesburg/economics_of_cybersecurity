import os
import _csv as csv
import numpy as np
import matplotlib.pyplot as plt
from pandas import read_csv
from collections import Counter

#######################Reading in data#######################
print("Start reading file")
dir_path = "feedbacks.csv"
column_names = ['hash_str','category','marketplace','item_hash','date','giver_hash','receiver_hash','message','order_title', 'feedback_value', 'order_amount_usd']

data = read_csv(dir_path, names=column_names)
print("Finished reading file")
#############################################################

labels = data['date'].tolist()
del labels[0]

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

transaction_counter = [0 for i in range(len(unique_labels))]

for i in range(len(labels)):
	transaction_counter[unique_labels.index(labels[i])] = transaction_counter[unique_labels.index(labels[i])] + 1

#list_of_transactions = [market_counter[i] for i in unique_markets]

y_pos = np.arange(len(unique_labels))
 
plt.bar(y_pos, transaction_counter, align='center', alpha=0.5)
plt.xticks(y_pos, unique_labels)
plt.xlabel('Year')
plt.ylabel('Number of transactions')
plt.title('Number of transactions per year')
 
plt.show()


#plt.xlabel('Market', fontsize=10)
#plt.ylabel('Percentage', fontsize=10)
#plt.title('Percentage of total goods sold on underground markets, per market')

#plt.show()

