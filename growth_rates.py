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
column_names = ['hash_str','category','marketplace','item_hash','date','giver_hash','receiver_hash','message','order_title', 'feedback_value']

data = read_csv(file_, names=column_names)
print("Finished reading file")
#############################################################

#Preparing all column data
markets = data[column_names[1]].tolist()
del markets[0]
labels = data[column_names[3]].tolist()
del labels[0]
buyers = data[column_names[5]].tolist()
del buyers[0]
sellers = data[column_names[4]].tolist()
del sellers[0]

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

#Getting the unique markets to be used in the graph
unique_markets = []
for market_number in range(len(markets)):
	if markets[market_number] not in unique_markets:
		unique_markets.append(markets[market_number])
print("Finished finding the unique markets")


#Making statistics Market->Year->[#Buyers,#Sellers]
stats = [[[0, 0] for k in range(len(unique_labels))] for l in range(len(unique_markets))]

#Count the number of unique buyers per year
for k in range(len(unique_labels)):
	temp_list = []
	for l in range(len(buyers)):
		if buyers[l] not in temp_list and labels[l] == unique_labels[k]:
			temp_list.append(buyers[l])
			market_index = unique_markets.index(markets[l])
			stats[market_index][k][0]= stats[market_index][k][0] + 1
	del temp_list
print("Finished counting the unique buyers")

#Count the number of unique sellers per year
for k in range(len(unique_labels)):
	temp_list = []
	for l in range(len(sellers)):
		if labels[l] == '2013' and markets[l] == 'Silkroad 1':
			print("Hit")
		if sellers[l] not in temp_list and labels[l] == unique_labels[k]:
			temp_list.append(sellers[l])
			market_index = unique_markets.index(markets[l])
			stats[market_index][k][1] = stats[market_index][k][1] + 1
	del temp_list
print("Finished counting the unique sellers")

print(stats)


buyers_per_market_per_year = [[] for k in range(len(unique_markets))]
for i in range(len(stats)):
	#Per market combine results for all the years
	year_data = []
	for j in range(len(stats[i])):
		year_data.append(stats[i][j][0])
	buyers_per_market_per_year[i] = year_data

sellers_per_market_per_year = [[] for k in range(len(unique_markets))]
for i in range(len(stats)):
	#Per market combine results for all the years
	year_data = []
	for j in range(len(stats[i])):
		year_data.append(stats[i][j][1])
	sellers_per_market_per_year[i] = year_data

plt.xlabel('Year', fontsize=10)
plt.ylabel('Number of active buyers (bought at least 1 product in that year)', fontsize=10)
plt.title('Number of active buyers per marketplace per year')
plt.plot(unique_labels, buyers_per_market_per_year[0], color='blue', label=unique_markets[0])
plt.plot(unique_labels, buyers_per_market_per_year[1], color='green', label=unique_markets[1])
plt.plot(unique_labels, buyers_per_market_per_year[2], color='red', label=unique_markets[2])
plt.plot(unique_labels, buyers_per_market_per_year[3], color='yellow', label=unique_markets[3])
plt.plot(unique_labels, buyers_per_market_per_year[4], color='purple', label=unique_markets[4])
plt.plot(unique_labels, buyers_per_market_per_year[5], color='black', label=unique_markets[5])
plt.plot(unique_labels, buyers_per_market_per_year[6], color='darkgreen', label=unique_markets[6])
plt.plot(unique_labels, buyers_per_market_per_year[7], color='lightblue', label=unique_markets[7])
plt.legend(loc='best')
plt.show()

plt.xlabel('Year', fontsize=10)
plt.ylabel('Number of active sellers (sold at least 1 product in that year)', fontsize=10)
plt.title('Number of active sellers per marketplace per year')
plt.plot(unique_labels, sellers_per_market_per_year[0], color='blue', label=unique_markets[0])
plt.plot(unique_labels, sellers_per_market_per_year[1], color='green', label=unique_markets[1])
plt.plot(unique_labels, sellers_per_market_per_year[2], color='red', label=unique_markets[2])
plt.plot(unique_labels, sellers_per_market_per_year[3], color='yellow', label=unique_markets[3])
plt.plot(unique_labels, sellers_per_market_per_year[4], color='purple', label=unique_markets[4])
plt.plot(unique_labels, sellers_per_market_per_year[5], color='black', label=unique_markets[5])
plt.plot(unique_labels, sellers_per_market_per_year[6], color='darkgreen', label=unique_markets[6])
plt.plot(unique_labels, sellers_per_market_per_year[7], color='lightblue', label=unique_markets[7])
plt.legend(loc='best')
plt.show()

del sellers
del buyers
del labels
del data

