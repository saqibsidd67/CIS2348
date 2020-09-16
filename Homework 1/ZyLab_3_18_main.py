# Saqib Siddiqui
# PSID:1495537

import math

print('Enter wall height (feet):')
height = int(input())
print('Enter wall width (feet):')
width = int(input())
area = height * width
print('Wall area:', area,'square feet')

gallon_paint = area / 350
print('Paint needed:','{:.2f}'.format(gallon_paint),'gallons')
cans = math.ceil(gallon_paint)
print('Cans needed:',cans,'can(s)')

wall_color = input('\nChoose a color to paint the wall:')

color_dict = {'red':'$35','blue':'$25','green':'$23'}
convert = color_dict[wall_color]
convertagain = int(convert[1:])
final_price = convertagain * cans
final = str(final_price)
finalfinal = '$' + final


print('\nCost of purchasing',wall_color,'paint:',finalfinal)






