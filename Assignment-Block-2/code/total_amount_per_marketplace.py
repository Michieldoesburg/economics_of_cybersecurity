import os
import _csv as csv
import numpy as np
import matplotlib.pyplot as plt
from pandas import read_csv
from collections import Counter

#######################Reading in data#######################
print("Start reading file")
dir_path = "feedbacks.csv"
column_names = ['hash_str','category','marketplace','item_hash','date','giver_hash','receiver_hash','message','order_title', 'feedback_value']

data = read_csv(dir_path, names=column_names)
print("Finished reading file")
#############################################################

markets = data['category'].tolist()
del markets[0]

#Getting the unique markets to be used in the graph
unique_markets = []
for market_number in range(len(markets)):
	if markets[market_number] not in unique_markets:
		unique_markets.append(markets[market_number])
print("Finished finding the unique markets")

#Create dictionary for simple counting
market_counter = dict()
for i in range(len(unique_markets)):
	market_counter[unique_markets[i]] = 0

#Counting the total transactions
for i in range(len(markets)):
	market_counter[markets[i]] = market_counter[markets[i]] + 1

list_of_transactions = [market_counter[i] for i in unique_markets]

y_pos = np.arange(len(unique_markets))
 
plt.bar(y_pos, list_of_transactions, align='center', alpha=0.5)
plt.xticks(y_pos, unique_markets)
plt.ylabel('Number of transactions')
plt.title('Number of transactions per marketplace')
 
plt.show()


#plt.xlabel('Market', fontsize=10)
#plt.ylabel('Percentage', fontsize=10)
#plt.title('Percentage of total goods sold on underground markets, per market')

#plt.show()

