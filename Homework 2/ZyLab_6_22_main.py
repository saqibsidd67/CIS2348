# Saqib Siddiqui
# PSID: 1495537

x1 = int(input())
y1 = int(input())
eq1 = int(input())
x2 = int(input())
y2 = int(input())
eq2  = int(input())
num = 0
for x in range(-10,11):
    for y in range(-10,11):
        if (x1 * x) + (y1 * y) == eq1 and (x2 * x) + (y2*y) == eq2:

            print(x, end= ' ')
            print(y)
            num = num + 1

if num == 0:
    print('No solution')








