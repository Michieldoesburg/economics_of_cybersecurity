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

print(unique_labels)

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

totalEvolution = list ()
for i in range(len(unique_labels)):

	for label_number in range(len(data)):
		if data[column_names[1]][label_number] == 'Evolution' and data[column_names[0]][label_number] == unique_labels[i]:
			print(data[column_names[2]][label_number])
			totalEvolution.append(float(data[column_names[2]][label_number]))

totalHydra = list ()
for i in range(len(unique_labels)):

	for label_number in range(len(data)):
		if data[column_names[1]][label_number] == 'Hydra' and data[column_names[0]][label_number] == unique_labels[i]:
			print(data[column_names[2]][label_number])
			totalHydra.append(float(data[column_names[2]][label_number]))
			
totalPandora = list ()
for i in range(len(unique_labels)):

	for label_number in range(len(data)):
		if data[column_names[1]][label_number] == 'Pandora' and data[column_names[0]][label_number] == unique_labels[i]:
			print(data[column_names[2]][label_number])
			totalPandora.append(float(data[column_names[2]][label_number]))

totalSilk1 = list ()
for i in range(len(unique_labels)):

	for label_number in range(len(data)):
		if data[column_names[1]][label_number] == 'Silk Road 1' and data[column_names[0]][label_number] == unique_labels[i]:
			print(data[column_names[2]][label_number])
			totalSilk1.append(float(data[column_names[2]][label_number]))
			
N = 7
cat1 = (totalAgora[0], totalAlphabay[0], totalBlack[0], totalEvolution[0], totalHydra[0], totalPandora[0], totalSilk1[0])
cat2 = (totalAgora[1], totalAlphabay[1], totalBlack[1], totalEvolution[1], totalHydra[1], totalPandora[1], totalSilk1[1])
cat3 = (totalAgora[2], totalAlphabay[2], totalBlack[2], totalEvolution[2], totalHydra[2], totalPandora[2], totalSilk1[2])
cat4 = (totalAgora[3], totalAlphabay[3], totalBlack[3], totalEvolution[3], totalHydra[3], totalPandora[3], totalSilk1[3])
cat5 = (totalAgora[4], totalAlphabay[4], totalBlack[4], totalEvolution[4], totalHydra[4], totalPandora[4], totalSilk1[4])
cat6 = (totalAgora[5], totalAlphabay[5], totalBlack[5], totalEvolution[5], totalHydra[5], totalPandora[5], totalSilk1[5])
cat7 = (totalAgora[6], totalAlphabay[6], totalBlack[6], totalEvolution[6], totalHydra[6], totalPandora[6], totalSilk1[6])
cat8 = (totalAgora[7], totalAlphabay[7], totalBlack[7], totalEvolution[7], totalHydra[7], totalPandora[7], totalSilk1[7])


ind = np.arange(N)    # the x locations for the groups
width = 0.35       # the width of the bars: can also be len(x) sequence

p1 = plt.bar(ind, cat1, width)
p2 = plt.bar(ind, cat2, width)
p3 = plt.bar(ind, cat3, width)
p4 = plt.bar(ind, cat4, width)
p5 = plt.bar(ind, cat5, width)
p6 = plt.bar(ind, cat6, width)
p7 = plt.bar(ind, cat7, width)
p8 = plt.bar(ind, cat8, width)

plt.ylabel('Scores')
plt.title('Scores by group and gender')
plt.legend((p1[0], p2[0], p3[0], p4[0], p5[0], p6[0], p7[0], p8[0]), ('Agora', 'Alpha', 'Black', 'Evolution', '1', '1', '1', '1'))

plt.show()
