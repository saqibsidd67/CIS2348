# Saqib Siddiqui
# PSID: 1495537


number = input()
list_split= [int (i) for i in number.split() if int(i) >= 0]

list_split.sort()


for num in list_split:
    print(num,end = ' ')
