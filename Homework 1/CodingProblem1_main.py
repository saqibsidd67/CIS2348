# Saqib Siddiqui
# PSID: 1495537

print('Birthday Calculator')
print('Current Day')
current_month = int(input('Month:'))
current_day = int(input('Day:'))
current_year = int(input('Year:'))

print('Birthday')
birth_month = int(input('Month:'))
birth_day = int(input('Day:'))
birth_year = int(input('Year:'))

if current_month == birth_month and current_day == birth_day:
    current_age = current_year - birth_year
    print('Happy Birthday!')
    print('You are',current_age,'years old.')
elif current_month < birth_month:
    current_age = current_year - birth_year - 1
    print('You are', current_age, 'years old.')
elif current_month > birth_month:
    current_age = current_year - birth_year
    print('You are', current_age, 'years old.')
elif current_month == birth_month and current_day > birth_day:
    current_age = current_year - birth_year
    print('You are', current_age, 'years old.')
elif current_month == birth_month and current_day < birth_day:
    current_age = current_year - birth_year - 1
    print('You are', current_age, 'years old.')
