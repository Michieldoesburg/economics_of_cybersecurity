import os
import _csv as csv
import numpy as np
import matplotlib.pyplot as plt
from pandas import read_csv

#######################Reading in data#######################
print("Start reading file")
dir_path = os.path.dirname(os.path.realpath(__file__))
file_ = dir_path + '/categorypermarket.csv'
column_names = ['category','marketplace','sum(total_sales)']
data = read_csv(file_, names=column_names)
print("Finished reading file")
#############################################################

labels = data[column_names[1]].tolist()
del labels[0]

unique_labels = []
for label_number in range(len(data[column_names[0]])):
	if data[column_names[0]][label_number] not in unique_labels:
		unique_labels.append(data[column_names[0]][label_number])
unique_labels.sort()

totalAgora = list ()
for i in range(len(unique_labels)):

	for label_number in range(len(data)):
		if data[column_names[1]][label_number] == 'Agora' and data[column_names[0]][label_number] == unique_labels[i]:
			print(data[column_names[2]][label_number])
			totalAgora.append(data[column_names[2]][label_number])

totalAgora = list ()
for i in range(len(unique_labels)):

	for label_number in range(len(data)):
		if data[column_names[1]][label_number] == 'Agora' and data[column_names[0]][label_number] == unique_labels[i]:
			print(data[column_names[2]][label_number])
			totalAgora.append(float(data[column_names[2]][label_number]))
			
totalAlphabay = list ()
for i in range(len(unique_labels)):

	for label_number in range(len(data)):
		if data[column_names[1]][label_number] == 'Alphabay' and data[column_names[0]][label_number] == unique_labels[i]:
			print(data[column_names[2]][label_number])
			totalAlphabay.append(float(data[column_names[2]][label_number]))
			

totalBlack = list ()
for i in range(len(unique_labels)):

	for label_number in range(len(data)):
		if data[column_names[1]][label_number] == 'Black Market Reloaded' and data[column_names[0]][label_number] == unique_labels[i]:
			print(data[column_names[2]][label_number])
			totalBlack.append(float(data[column_names[2]][label_number]))
print(totalAgora)
print(totalAlphabay)
			
N = 9
agora = (totalAgora[0], totalAgora[1], totalAgora[2], totalAgora[3], totalAgora[4], totalAgora[5], totalAgora[6], totalAgora[7], totalAgora[8])
alpha = (totalAlphabay[0], totalAlphabay[1], totalAlphabay[2], totalAlphabay[3], totalAlphabay[4], totalAlphabay[5], totalAlphabay[6], totalAlphabay[7], totalAlphabay[8])
black = (totalBlack[0], totalBlack[1], totalBlack[2], totalBlack[3], totalBlack[4], totalBlack[5], totalBlack[6], totalBlack[7], totalBlack[8])

ind = np.arange(N)    # the x locations for the groups
width = 0.35       # the width of the bars: can also be len(x) sequence

p1 = plt.bar(ind, agora, width)
p2 = plt.bar(ind, alpha, width, bottom=agora)
p3 = plt.bar(ind, agora, width)

plt.ylabel('Scores')
plt.title('Scores by group and gender')
plt.legend((p1[0], p2[0], p3[0]), ('Agora', 'Alpha', 'Black'))

plt.show()
