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

dir_path = dir_path + '/feedbacks.csv'
column_names_feedback = ['hash_str','category','marketplace','item_hash','date','giver_hash','receiver_hash','message','order_title', 'feedback_value', 'order_amount_usd']
data_feedback = read_csv(dir_path, names=column_names_feedback)
print("Finished reading file")
#############################################################

#Reading specific data and removing label
vendor_hashes = data_items["vendor_hash"].tolist()
markets = data_items["marketplace"].tolist()
item_hashes = data_items["item_hash"].tolist()
total_sales = data_items["total_sales"].tolist()
del vendor_hashes[0]
del markets[0]
del item_hashes[0]
del total_sales[0]


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

#Getting the unique vendors
unique_vendor_hashes = [] #5585 vendors
for vendor_number in range(len(vendor_hashes)):
	if vendor_hashes[vendor_number] not in unique_vendor_hashes:
		unique_vendor_hashes.append(vendor_hashes[vendor_number])

#Storing item hashes per vendor hash
vendor_items = dict()
item_vendor = dict()
vendor_revenue = dict()
for index in range(len(unique_vendor_hashes)):
	vendor_items[unique_vendor_hashes[index]] = list()
	vendor_revenue[unique_vendor_hashes[index]] = 0

for item_number in range(len(item_hashes)):
	vendor_items[vendor_hashes[item_number]].append(item_hashes[item_number])
	item_vendor[item_hashes[item_number]] = vendor_hashes[item_number]
	vendor_revenue[vendor_hashes[item_number]] = float(vendor_revenue[vendor_hashes[item_number]]) + float(total_sales[item_number])
print("Finished creating vendor-item combinations.")

#Calculate revenue per market
revenue_per_market = list()
vendor_markets_revenue = list()
for market_number in range(len(vendors_per_market)):
	vendors = vendors_per_market[market_number]
	market_revenue = 0
	vendor_market_revenue = list()
	for index in range(len(vendors)):
		market_revenue = market_revenue + float(vendor_revenue[vendors[index]])
		vendor_market_revenue.append(float(vendor_revenue[vendors[index]]))
	revenue_per_market.append(market_revenue)
	vendor_market_revenue.sort(reverse=True, key=float)
	vendor_markets_revenue.append(vendor_market_revenue)

#Calculate percentage vendors control of market revenue
vendor_percentage = [0,10,20,30,40,50,60,70,80,90,100]
revenue_accumulated_markets = list()
for index in range(len(vendor_markets_revenue)):
	revenue_accumulated_market = list()
	for percentage in vendor_percentage:
		percentage_number = float(percentage)/float(100)
		number_of_vendors = percentage_number * len(vendor_markets_revenue[index])
		revenue = 0
		for vendor_number in range(int(number_of_vendors)):
			revenue = revenue + float(vendor_markets_revenue[index][vendor_number])
		revenue_accumulated_market.append(revenue)
	revenue_accumulated_markets.append(revenue_accumulated_market)

#Change market revenues in percentages of total revenue of the market
for index in range(len(revenue_accumulated_markets)):
	market_revenue = revenue_accumulated_markets[index]
	market_revenue_percentage = list()
	for revenue in market_revenue:
		market_revenue_percentage.append((float(revenue)/float(revenue_per_market[index]))*100)
	revenue_accumulated_markets[index] = market_revenue_percentage


plt.xlabel('Percentage of vendors of the market', fontsize=10)
plt.ylabel('Percentage of the total revenue of the market', fontsize=10)
plt.title('Percentage of vendors representing percentage of total revenue per market')
plt.plot(vendor_percentage, revenue_accumulated_markets[0], color='blue', label=unique_markets[0])
plt.plot(vendor_percentage, revenue_accumulated_markets[1], color='green', label=unique_markets[1])
plt.plot(vendor_percentage, revenue_accumulated_markets[2], color='red', label=unique_markets[2])
plt.plot(vendor_percentage, revenue_accumulated_markets[3], color='yellow', label=unique_markets[3])
plt.plot(vendor_percentage, revenue_accumulated_markets[4], color='purple', label=unique_markets[4])
plt.plot(vendor_percentage, revenue_accumulated_markets[5], color='black', label=unique_markets[5])
plt.plot(vendor_percentage, revenue_accumulated_markets[6], color='darkgreen', label=unique_markets[6])
plt.plot(vendor_percentage, revenue_accumulated_markets[7], color='lightblue', label=unique_markets[7])
plt.legend(loc='best')
plt.show()
