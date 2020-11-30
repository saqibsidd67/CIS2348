# Saqib Siddiqui
# PSID: 1495537



split_string = input().split()
name_string = split_string[0]

while (name_string != '-1'):
    try:
        age_string = split_string[1]
        age_add = int(age_string) + 1
    except ValueError as exct:
        age_add = 0

    print('{} {}'.format(name_string,age_add))



    split_string = input().split()
    name_string = split_string[0]







