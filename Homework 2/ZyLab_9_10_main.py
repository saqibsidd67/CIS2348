# Saqib Siddiqui
# PSID: 1495537

import csv
file_input = input()

with open(file_input,'r') as csvfile:
    reader = csv.reader(csvfile)

    count = {}
    row_num = 1
    for i in reader:
        for x in i:
            if x not in count.keys():
                count[x] = 1
            else:
                count[x] += 1
for y in count.keys():
    print(y + " " + str(count[y]))
