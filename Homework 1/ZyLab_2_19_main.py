# Saqib Siddiqui
# PSID:1495537

print('Enter amount of lemon juice (in cups):')
lemon_cups = float(input())
print('Enter amount of water (in cups):')
water_cups = float(input())
print('Enter amount of agave nectar (in cups):')
agave_cups = float(input())
print('How many servings does this make?')
servings = float(input())

print('\nLemonade ingredients - yields','{:.2f}'.format(servings),'servings')
print('{:.2f}'.format(lemon_cups),'cup(s) lemon juice')
print('{:.2f}'.format(water_cups),'cup(s) water')
print('{:.2f}'.format(agave_cups),'cup(s) agave nectar')


print('\nHow many servings would you like to make?')
servings_tomake = int(input())
print('\nLemonade ingredients - yields','{:.2f}'.format(servings_tomake),'servings')
servings_divided = servings_tomake / servings
lemonservings = servings_divided * lemon_cups
waterservings = servings_divided * water_cups
agaveservings = servings_divided * agave_cups
print('{:.2f}'.format(lemonservings),'cup(s) lemon juice')
print('{:.2f}'.format(waterservings),'cup(s) water')
print('{:.2f}'.format(agaveservings),'cup(s) agave nectar')


print('\nLemonade ingredients - yields','{:.2f}'.format(servings_tomake),'servings')
lemon_gallons = lemonservings/16
water_gallons = waterservings/16
agave_gallons = agaveservings/16
print('{:.2f}'.format(lemon_gallons),'gallon(s) lemon juice')
print('{:.2f}'.format(water_gallons),'gallon(s) water')
print('{:.2f}'.format(agave_gallons),'gallon(s) agave nectar')