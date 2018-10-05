import os
import _csv as csv
import numpy as np
import matplotlib.pyplot as plt
from pandas import read_csv
from collections import Counter

#######################Reading in data#######################
print("Start reading file")
dir_path = "items.csv"
column_names = ['item_hash','category','marketplace','title','vendor_hash','total_sales','first_observed','last_observed','ships_to','ships_from','description']

data = read_csv(dir_path, names=column_names)
print("Finished reading file")
#############################################################

places_to = data['ships_to'].tolist()
places_from = data['ships_from'].tolist()
del places_to[0]
del places_from[0]


unique_places_to = Counter(places_to).keys()
unique_places_from = Counter(places_from).keys()

places_to_count = dict()
places_from_count = dict()

for i in range(len(unique_places_to)):
	places_to_count[unique_places_to[i]] = 0
for i in range(len(unique_places_from)):
	places_from_count[unique_places_from[i]] = 0

for i in range(len(places_to)):
	places_to_count[places_to[i]] = places_to_count[places_to[i]] + 1
for i in range(len(places_from)):
	places_from_count[places_from[i]] = places_from_count[places_from[i]] + 1

print("Places to:")
print(places_to_count)
print("Places from:")
print(places_from_count)

#plt.xlabel('Market', fontsize=10)
#plt.ylabel('Percentage', fontsize=10)
#plt.title('Percentage of total goods sold on underground markets, per market')

#plt.show()

