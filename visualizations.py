import os
import _csv as csv
import numpy as np
import matplotlib.pyplot as plt
from pandas import read_csv

#######################Reading in data#######################
print("Start reading file")
dir_path = "marketplace.csv"
column_names = ['name','total_sales','last_90','last_30','last_7','first_observed','last_observed','csv','coveragecsv']
data = read_csv(dir_path, names=column_names)
print("Finished reading file")
#############################################################

labels = data['name'].tolist()
del labels[0]
num_sales = data['total_sales'].tolist()
del num_sales[0]

sales_Data = data['csv'].tolist()
del sales_Data[0]

hash_map = {}

for x in labels:
    hash_map[x] = {}
    hash_map[x]['2011'] = 0
    hash_map[x]['2012'] = 0
    hash_map[x]['2013'] = 0
    hash_map[x]['2014'] = 0
    hash_map[x]['2015'] = 0

for y in range(len(sales_Data)):
    trx = sales_Data[y].split(',')
    print(trx)

    year1 = 100000000000000000
    year2 = 100000000000000000
    year3 = 100000000000000000
    year4 = 100000000000000000
    year5 = 100000000000000000

    for i in range(len(trx)):
        if '2011' in trx[i]:
            year1 = i
        if '2012' in trx[i]:
            year2 = i
        if '2013' in trx[i]:
            year3 = i
        if '2014' in trx[i]:
            year4 = i
        if '2015' in trx[i]:
            year5 = i

    for i in range(len(trx)):
        if '2011' in trx[i]:
            continue
        if '2012' in trx[i]:
            continue
        if '2013' in trx[i]:
            continue
        if '2014' in trx[i]:
            continue
        if '2015' in trx[i]:
            continue

        if i > year1 and i < year2:
            hash_map[labels[y]]['2011'] += int(float(trx[i]))
        if i > year2 and i < year3:
            hash_map[labels[y]]['2012'] += int(float(trx[i]))
        if i > year3 and i < year4:
            hash_map[labels[y]]['2013'] += int(float(trx[i]))
        if i > year4 and i < year5:
            hash_map[labels[y]]['2014'] += int(float(trx[i]))
        if i > year5:
            hash_map[labels[y]]['2015'] += int(float(trx[i]))

print(hash_map)

for i in range(len(num_sales)):
    num_sales[i] = int(float(num_sales[i]))

total_goods_sold = sum(num_sales)

for i in range(len(num_sales)):
    num_sales[i] = num_sales[i] / total_goods_sold * 100

X = labels
Y = num_sales

_X = np.arange(len(X))

plt.bar(_X, Y)
plt.xticks(_X, X) # set labels manually

plt.xlabel('Market', fontsize=10)
plt.ylabel('Percentage', fontsize=10)
plt.title('Percentage of total goods sold on underground markets, per market')

plt.show()




X = hash_map.keys()
Y = []
Z = []
H = []
G = []
F = []

for x in X:
    Y.append(hash_map[x]['2011'])
    Z.append(hash_map[x]['2012'])
    H.append(hash_map[x]['2013'])
    G.append(hash_map[x]['2014'])
    F.append(hash_map[x]['2015'])

_X = np.arange(len(X))

plt.bar(_X - 2.5, Y, 0.2)
plt.bar(_X - 1.5, Z, 0.2)
plt.bar(_X - 0.5, H, 0.2)
plt.bar(_X + 1.5, G, 0.2)
plt.bar(_X + 2.5, F, 0.2)

plt.xticks(_X, X) # set labels manually

plt.suptitle("Percentage of malicious netflows per network protocol.")
plt.show()