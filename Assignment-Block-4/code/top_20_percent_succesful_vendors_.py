import os
import _csv as csv
import numpy as np
import matplotlib.pyplot as plt
from pandas import read_csv
import datetime

#General information:
#5585 vendors total
#44578 items total
g_year = 2017

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
feedback_item_hashes = data_feedback["item_hash"].tolist()
feedback_item_value = data_feedback["order_amount_usd"].tolist()
feedback_item_date = data_feedback["date"].tolist()
feedback_item_date_unmodified = data_feedback["date"].tolist()
del vendor_hashes[0]
del markets[0]
del item_hashes[0]
del total_sales[0]
del feedback_item_hashes[0]
del feedback_item_value[0]
del feedback_item_date[0]
del feedback_item_date_unmodified[0]

#Stripping of the rest of the date and only keeping the year
for i in range(len(feedback_item_date)):
	feedback_item_date[i] = str(feedback_item_date[i])[:4]

def get_vendors_per_market(unique_markets, markets, vendors, vendors_this_year):
	vendors_per_market = []
	for market_number in range(len(unique_markets)):
		list_of_unique_vendor_hashes = [] 
		for vendor_number in range(len(vendors)):
			if vendors[vendor_number] not in list_of_unique_vendor_hashes and markets[vendor_number] == unique_markets[market_number] and vendors[vendor_number] in vendors_this_year:
				list_of_unique_vendor_hashes.append(vendor_hashes[vendor_number])
		vendors_per_market.append(list_of_unique_vendor_hashes)
	return vendors_per_market

def get_vendors_in_year(item_sales, vendors_per_item):
	vendors = []
	count = 0
	for item in item_sales:
		if item in vendors_per_item:
			for vendor in vendors_per_item[item]:
				if vendor not in vendors:
					vendors.append(vendor)
	return vendors

def get_vendors_per_item(items, vendors):
	vendor_per_item = dict()
	for item_index in range(len(items)):
		if items[item_index] in vendor_per_item and vendors[item_index] not in vendor_per_item[items[item_index]]:
			vendor_per_item[items[item_index]].append(vendors[item_index])
		elif items[item_index] not in vendor_per_item:
			vendor_per_item[items[item_index]] = [vendors[item_index]]
	return vendor_per_item


def get_items_per_vendor(items, vendors):
	vendor_items = dict()
	for item_index in range(len(items)):
		if vendors[item_index] in vendor_items and items[item_index] not in vendor_items[vendors[item_index]]:
			vendor_items[vendors[item_index]].append(items[item_index])
		elif vendor_hashes[item_index] not in vendors:
			vendor_items[vendors[item_index]] = [items[item_index]]
	return vendor_items
			
		
def create_sales_dictionary_for_specified_year(item_hashes, transaction_dates, transaction_values, year):
	item_sales = dict()
	#Getting total sales of items in a specific year
	for index in range(len(item_hashes)):
		if item_hashes[index] in item_sales and str(transaction_dates[index]) == str(year):
			item_sales[item_hashes[index]] = item_sales[item_hashes[index]] + float(transaction_values[index])
		elif str(transaction_dates[index]) == str(year):
			item_sales[item_hashes[index]] = float(transaction_values[index])
	return item_sales

def get_unique_values(values):
	unique_values = []
	for value_number in range(len(values)):
		if values[value_number] not in unique_values:
			unique_values.append(values[value_number])
	return unique_values

def get_revenue_per_vendor(vendors_per_item, item_sales):
	vendor_revenue = dict()
	for item in item_sales:
		vendors = vendors_per_item[item]
		for vendor in vendors:
			if vendor not in vendor_revenue:
				vendor_revenue[vendor] = item_sales[item]
			else:
				vendor_revenue[vendor] = vendor_revenue[vendor] + item_sales[item]
	return vendor_revenue

def create_vendor_revenue_tuples(vendor_revenue):
	tuples = []
	for vendor in vendor_revenue:
		tuples.append((vendor, float(vendor_revenue[vendor])))
	return tuples

def get_top_vendors(numbers_of_vendors, tuples):
	top_vendors = []
	for index in range(numbers_of_vendors):
		top_vendors.append(tuples[index][0])
	return top_vendors

def get_top_vendors_per_market(vendors_per_market, vendor_revenue):
	top_vendors_per_market = []
	for market_vendors in vendors_per_market:
		vendor_revenue_tuples = []
		for vendor in market_vendors:
			vendor_revenue_tuples.append((vendor, float(vendor_revenue[vendor])))
		vendor_revenue_tuples.sort(key=lambda x: x[1], reverse=True)
		number_of_top_vendors = int(0.2 * len(vendor_revenue_tuples))
		top_vendors = get_top_vendors(number_of_top_vendors, vendor_revenue_tuples)
		top_vendors_per_market.append(top_vendors)
	return top_vendors_per_market

def calculate_lifespan_of_each_vendor_in_days(vendors, vendors_per_item, items_sold, transaction_items, transaction_dates, year, real_transaction_dates):

	#Creates an empty list for each vendor
	vendor_dates = dict()
	for vendor in vendors:
		vendor_dates[vendor] = []

	#Assume that item hashes are unique over all markets
	for transaction_index in range(len(transaction_items)):
		if transaction_items[transaction_index] in items_sold and str(transaction_dates[transaction_index]) == str(year):
			vendor_dates[vendors_per_item[transaction_items[transaction_index]][0]].append(real_transaction_dates[transaction_index])

	#Sort all the dates
	for vendor in vendor_dates:
		dates = [datetime.datetime.strptime(ts, "%Y-%m-%d") for ts in vendor_dates[vendor]]
		dates.sort()
		vendor_dates[vendor] = dates

	#Calculate lifespan for each vendor
	vendor_lifespan_in_days = dict()
	for vendor in vendor_dates:
		first_date = vendor_dates[vendor][0]
		last_date = vendor_dates[vendor][len(vendor_dates[vendor]) - 1]
		number_of_days = (last_date - first_date).days
		vendor_lifespan_in_days[vendor] = number_of_days

	return vendor_lifespan_in_days

def calculate_average_lifespan_per_market_in_days(vendor_lifespan_in_days, top_vendors_per_market):
	average_lifespan_per_market = []
	for market_vendors in top_vendors_per_market:
		if len(market_vendors) == 0:
			average_lifespan_per_market.append(0)
		else:
			total_lifespan = 0
			total_vendors = len(market_vendors)
			for vendor in market_vendors:
				total_lifespan = total_lifespan + int(vendor_lifespan_in_days[vendor])
			average_lifespan_per_market.append(float(total_lifespan)/float(total_vendors))
	return average_lifespan_per_market


#Basic Knowledge
unique_markets = get_unique_values(markets)
unique_vendors = get_unique_values(vendor_hashes)
print("Got unique markets and vendors")
items_per_vendor = get_items_per_vendor(item_hashes, vendor_hashes)
print("Got items per vendor")
vendors_per_item = get_vendors_per_item(item_hashes, vendor_hashes)
print("Got vendors per item")

years = [2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018]
lifespans_per_market = []
for index in unique_markets:
	lifespans_per_market.append([])

for year in years:
	print("Year %d" % year)
	#Year specific knowledge
	item_sales = create_sales_dictionary_for_specified_year(feedback_item_hashes, feedback_item_date, feedback_item_value, year) #Items per year + revenue
	print("Got item sales for this year")
	vendors = get_vendors_in_year(item_sales, vendors_per_item)
	print("Got vendors in this year")
	vendors_per_market = get_vendors_per_market(unique_markets, markets, vendor_hashes, vendors) #Ordered by order of unique_markets
	print("Got vendors per market this year")
	vendor_revenue = get_revenue_per_vendor(vendors_per_item, item_sales)
	print("Got revenue per vendor this year")
	top_vendors_per_market = get_top_vendors_per_market(vendors_per_market, vendor_revenue)
	print("Got top vendors per market")
	vendor_lifespan_in_days = calculate_lifespan_of_each_vendor_in_days(vendors, vendors_per_item, item_sales, feedback_item_hashes, feedback_item_date, year, 	feedback_item_date_unmodified)
	print("Got lifespan per vendor")
	average_lifespan_per_market = calculate_average_lifespan_per_market_in_days(vendor_lifespan_in_days, top_vendors_per_market)
	print("Got average lifespan of top vendors for each market")
	
	for index in range(len(average_lifespan_per_market)):
		lifespans_per_market[index].append(average_lifespan_per_market[index])


plt.xlabel('Years', fontsize=10)
plt.ylabel('Average lifespan of the top 20% vendors in days', fontsize=10)
plt.title('Average lifespan of the top 20% vendors in days per market per year')
plt.plot(years, lifespans_per_market[0], color='blue', label=unique_markets[0])
plt.plot(years, lifespans_per_market[1], color='green', label=unique_markets[1])
plt.plot(years, lifespans_per_market[2], color='red', label=unique_markets[2])
plt.plot(years, lifespans_per_market[3], color='yellow', label=unique_markets[3])
plt.plot(years, lifespans_per_market[4], color='purple', label=unique_markets[4])
plt.plot(years, lifespans_per_market[5], color='black', label=unique_markets[5])
plt.plot(years, lifespans_per_market[6], color='darkgreen', label=unique_markets[6])
plt.plot(years, lifespans_per_market[7], color='lightblue', label=unique_markets[7])
plt.legend(loc='best')
plt.show()
