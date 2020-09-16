# Saqib Siddiqui
# PSID: 1495537

print("Davy's auto shop services")
print('Oil change -- $35')
print('Tire rotation -- $19')
print('Car wash -- $7')
print('Car wax -- $12')

first_service = input('\nSelect first service:')
second_service = input('\nSelect second service:')

new_dict = {'Oil change': '$35','Tire rotation': '$19','Car wash': '$7' , 'Car wax': '$12','-':'No service'}

print("\n\nDavy's auto shop invoice")

#print('\nService 1:',first_service,',',new_dict[first_service])
#print('Service 2:',second_service,',',new_dict[second_service])



if first_service == '-':
    convert2 = new_dict[second_service]
    convertagain2 = int(convert2[1:])
    total = 0 + convertagain2
    total_service = str(total)
    finaltotal = '$' + total_service
    print('\nService 1: No service')
    secondstring = second_service + ', $' + str(convertagain2)
    print('Service 2:', secondstring)
    print('\nTotal:', finaltotal)
elif second_service == '-':
    convert1 = new_dict[first_service]
    convertagain1 = int(convert1[1:])
    total = 0 + convertagain1
    total_service = str(total)
    finaltotal = '$' + total_service
    firststring = first_service + ', $' + str(convertagain1)
    print('\nService 1:', firststring)
    print('Service 2: No service')
    print('\nTotal:', finaltotal)

else:
    convert1 = new_dict[first_service]
    convert2 = new_dict[second_service]
    convertagain1 = int(convert1[1:])
    convertagain2 = int(convert2[1:])
    total = convertagain1 + convertagain2
    total_service = str(total)
    finaltotal ='$' + total_service
    firststring = first_service + ', $' + str(convertagain1)
    print('\nService 1:',firststring)
    secondstring = second_service + ', $' + str(convertagain2)
    print('Service 2:',secondstring)
    print('\nTotal:',finaltotal)