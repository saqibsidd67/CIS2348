# Saqib Siddiqui
# PSID: 1495537


new_list=["January","February","March","April","May","June","July","August","September","October","November","December"]
date = ' '

while date != str(-1):
    date = input()
    for i in range(12):
        if new_list[i] in date and ',' in date:
            monthl = len(new_list[i])
            first_space = date.find(" ")
            second_space = date.find(" ",first_space + 1)
            third_space = date.find(" ", second_space + 1)
            comma = date.find(',')
            sub = comma - first_space

            if monthl == first_space and (comma + 1 == second_space) and third_space == -1:
                a= date.replace(new_list[i],str(i+1))
                b = a.split(' ')
                c = '/'.join(b)
                d = c.replace(',','')
                print(d)
























