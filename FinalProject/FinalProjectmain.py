# Saqib Siddiqui
# PSID: 1495537

# imports csv to help with opening files and datetime to help with importing current date
import csv
from datetime import datetime

# Opens ManufacturerList.csv and appends the contents into an empty string
m1 = []
with open('ManufacturerList.csv','r') as csvfile:
    id_reader = csv.reader(csvfile, delimiter = ",")

    for i in id_reader:
        m1.append(i)

# Opens PriceList.csv and appends the contents into an empty string
m2 = []
with open('PriceList.csv') as csvfile:
    id_reader2 = csv.reader(csvfile, delimiter = ",")

    for j in id_reader2:
        m2.append(j)

# Opens ServiceDatesList.csv and appends the contents into an empty string
m3=[]
with open('ServiceDatesList.csv') as csvfile:
    id_reader3 = csv.reader(csvfile, delimiter = ",")

    for k in id_reader3:
        m3.append(k)

# Sorts the list in order of IDs and if IDs are the same sorts in alphabetical order the model
m1.sort(key = lambda x:(x[1],x[2]))

# Combines both contents of all three lists to make a final list
for x in range(0,len(m1)):
    for y in range(0,len(m2)):
        if m1[x][0] == m2[y][0]:
            b = m1[x]
            b.insert(3,m2[y][1])

for x2 in range(0,len(m1)):
    for y2 in range(0,len(m3)):
        if m1[x2][0] == m3[y2][0]:
            b2 = m1[x2]
            b2.insert(4,m3[y2][1])

# The final list is written into the FullInventory file
f = open('FullInventory.csv','w')
for i in range(0,len(m1)):
    for j in range(0,6):
        if j != 5:
            a = m1[i][j] + ','
        else:
            a = m1[i][j]
        f.write(a)
    f.write('\n')
f.close()

# _Inventory

inventory = []
for ii in range(0,len(m1)):
    inventory.append(m1[ii][2])

#Removes duplicates by turning it into a dictionary
inventory = list(dict.fromkeys(inventory))

# Append to make each inventory file
invent_item = []
invent_item = m1
item_inventory = []
for jj in range(0,len(inventory)):
    for ii in range(0,len(invent_item)):
        title = inventory[jj].capitalize() + "Inventory.csv"
        if inventory[jj] == invent_item[ii][2]:
            item_inventory.append(invent_item[ii])
    # deletes item so the item type is not included within the file
    for x in range(0,len(item_inventory)):
        del (item_inventory[x][2])
    # item is sorted by incrementing ID numbers
    item_inventory.sort(key = lambda x:(x[0]))
    # file is created to create each inventory file with a for loopgoing through each file
    f2 = open(title, 'w')
    for i in range(0, len(item_inventory)):
        for j in range(0, 5):
            if j != 4:
                a = item_inventory[i][j] + ','
            else:
                a = item_inventory[i][j]
            f2.write(a)
        f2.write('\n')
    f2.close()
    item_inventory = []

# Past Service

# Since the item type was deleted, it has to be insrted back into the m1 variable
m1= []
with open('FullInventory.csv') as csvfile:
    id_reader4 = csv.reader(csvfile, delimiter = ",")

    for k in id_reader4:
        m1.append(k)

past_service = m1
service_date = []

# for loop to go through each date and comparing it to the current date
for ii in range(0,len(past_service)):
    current_date = datetime.now()
    a = past_service[ii][4]
    dates = datetime.strptime(a,"%m/%d/%Y")
    if dates < current_date:
        service_date.append(past_service[ii])
# sorts based on the date from oldest to newest
service_date.sort(key = lambda x: datetime.strptime(x[4],"%m/%d/%Y"))
# writes file for PastServiceDateInventory
f3 = open('PastServiceDateInventory.csv','w')
for i in range(0,len(service_date)):
    for j in range(0,6):
        if j != 5:
            a = service_date[i][j] + ','
        else:
            a = service_date[i][j]
        f3.write(a)
    f3.write('\n')
f3.close()

# Damaged Inventory

inventory_d = m1
damaged_inventory = []

# appends those that are damaged
for ii in range(0,len(inventory_d)):
    if inventory_d[ii][5] == 'damaged':
        damaged_inventory.append(inventory_d[ii])

# sorts based on the price from most expensive to least expensive
damaged_inventory.sort(key = lambda x:float(x[3]))

# Creates contents for the DamangedInventory file
f4 = open('DamagedInventory.csv', 'w')
for i in range(0, len(damaged_inventory)):
    for j in range(0, 5):
        if j != 4:
            a = damaged_inventory[i][j] + ','
        else:
            a = damaged_inventory[i][j]
        f4.write(a)
    f4.write('\n')
f4.close()


nodamage_nopast = []
# For loop to go though m1 and if is not damaged and are not past the service date are appended into a new
# seperate list
for ii in range(0,len(m1)):
    b2 = m1[ii][4]
    dates2 = datetime.strptime(b2, "%m/%d/%Y")
    if m1[ii][5] != 'damaged' and dates2 > current_date:
        nodamage_nopast.append(m1[ii])
nodamage_nopast.sort(key = lambda x:float(x[3]),reverse = True)

price_nodamage_nopast = []

# range of data that appends all the prices for those that are not damaged and not past the service date
for uu in range(0,len(nodamage_nopast)):
    price_nodamage_nopast.append(nodamage_nopast[uu][3])

# range of data that turns the strings in the prices to int to help with a step later on to determine what
# is closest to a specific variable

for gg in range(0,len(price_nodamage_nopast)):
    price_nodamage_nopast[gg] = int(price_nodamage_nopast[gg])


# inputs for the main query section
manufacturer_name = str(input('Enter manufacturer name:'))
item_type = str(input('Enter item type:'))



picked_choice = []
# while loop that will run if both inputs are not 'q'
while manufacturer_name != 'q' or item_type != 'q':

    # Quits the program if input is 'q
    if manufacturer_name == 'q' or item_type == 'q':
        break




    # for loop to go through the list of non damaged/not past service date data
    for ll in range(0, len(nodamage_nopast)):
        # .strip() is used to ignore any/all leading and trailing spaces. The conditional finds if the
        # no_damange_nopast variable is in the manufacturer name and item_type input
        if nodamage_nopast[ll][1].strip() in manufacturer_name.split(" ") and nodamage_nopast[ll][2].strip() in item_type.split(" "):
            picked_choice.append(nodamage_nopast[ll])
            print('Your item is: {} {} {} {}'.format(nodamage_nopast[ll][0],nodamage_nopast[ll][1],nodamage_nopast[ll][2], nodamage_nopast[ll][3]))
            # a break is done to only print the first iteration. in this case the most expensive item
            break

        # conditional only executes if there is not picked choice and the for loop above is done
        if len(picked_choice) == 0 and ll == len(nodamage_nopast) - 1:
            print('No such item in inventory. ')
    # if length is not 0 then the you may consider statement is printed
    if len(picked_choice) != 0:
        for pp in range(0, len(nodamage_nopast)):
            dd = int(picked_choice[0][3])
            # the prices list is sorted in term of closest to the picked choice
            price_nodamage_nopast.sort(key=lambda x: abs(dd - x))
            # turns the list from integers back to a string
            output = [str(xyxy) for xyxy in price_nodamage_nopast]
            final_list = []

            # final_list finds the elements the order of closeness to the inputted choices and appends it
            # into a seperate list
            for klm in range(0, len(output)):
                for lmn in range(0, len(nodamage_nopast)):
                     if nodamage_nopast[lmn][3] == output[klm]:
                        final_list.append(nodamage_nopast[lmn])
            # if the brand is different and the item type is the same, then the you may also consider statement
            # is printed in regards to the closest in price being the one that is printed out
            if picked_choice[0][1] != final_list[pp][1] and picked_choice[0][2] == final_list[pp][2]:
                print('You may,also,consider:{} {} {} {}'.format(final_list[pp][0], final_list[pp][1],final_list[pp][2], final_list[pp][3]))
                break


    # repeated input statements are only printed out if they don't equal 'q'

    manufacturer_name = str(input('Enter manufacturer name:'))
    if manufacturer_name == 'q':
        break

    item_type = str(input('Enter item type:'))
    if item_type == 'q':
        break
    # picked choice is returned to default in the case that another iteration is needed
    picked_choice = []

































































