import os
import _csv as csv
import numpy as np
import matplotlib.pyplot as plt
from pandas import read_csv

#General information:
#5585 vendors total
#44578 items total

#######################Reading in data#######################
print("Start reading file")
dir_path = os.path.dirname(os.path.realpath(__file__))
file_ = dir_path + '/items.csv'
column_names_items = ['item_hash','category','marketplace','title','vendor_hash','total_sales','first_observed','last_observed','ships_to','ships_from','description']
data_items = read_csv(file_, names=column_names_items)
print("Finished reading file")
#############################################################

#Reading specific data and removing label
vendor_hashes = data_items["vendor_hash"].tolist()
markets = data_items["marketplace"].tolist()
del vendor_hashes[0]
del markets[0]


#Getting the unique markets to be used in the graph
unique_markets = []
for market_number in range(len(markets)):
	if markets[market_number] not in unique_markets:
		unique_markets.append(markets[market_number])
print("Finished finding the unique markets")

#Getting the vendor hashes per market
vendors_per_market = []
for market_number in range(len(unique_markets)):
	list_of_unique_vendor_hashes = [] 
	for vendor_number in range(len(vendor_hashes)):
		if vendor_hashes[vendor_number] not in list_of_unique_vendor_hashes and markets[vendor_number] == unique_markets[market_number]:
			list_of_unique_vendor_hashes.append(vendor_hashes[vendor_number])
	vendors_per_market.append(list_of_unique_vendor_hashes)
print("Finished finding the unique vendors")

#Getting the counts of vendors per markets
vendor_count_market = []
for vendor_list in vendors_per_market:
	vendor_count_market.append(len(vendor_list))



plt.xlabel('Markets', fontsize=10)
plt.ylabel('Number of vendors', fontsize=10)
plt.title('Number of vendors per market')
plt.bar(unique_markets, vendor_count_market, color="blue")
plt.legend(loc='best')
plt.show()
