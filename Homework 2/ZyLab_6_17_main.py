# Saqib Siddiqui
# PSID: 1495537

passwordin = input()
finalpassword = ' '
a = len(passwordin)


for i in passwordin:

    if i == 'i':
        finalpassword += '!'

    elif i == 'a':
        finalpassword += '@'

    elif i == 'm':
        finalpassword += 'M'

    elif i == 'B':
        finalpassword += '8'

    elif i == 'o':
        finalpassword += '.'
    else:
        finalpassword += i


finalpassword+= 'q*s'
finalpassword2 = finalpassword.strip()

print(finalpassword2)




