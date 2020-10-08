# Saqib Siddiqui
# PSID: 1495537

def exact_change( user_total):
    numdollars = int(user_total / 100)
    user_total = int(user_total % 100)
    if numdollars == 1:
        print(numdollars,'dollar')
    elif numdollars > 1:
        print(numdollars, 'dollars')
    numquarters = int(user_total / 25)
    user_total = int(user_total % 25)
    if numquarters == 1:
        print(numquarters,'quarter')
    elif numquarters > 1:
        print(numquarters, 'quarters')
    numdimes = int(user_total / 10)
    user_total = int(user_total % 10)
    if numdimes == 1:
        print(numdimes,'dime')
    elif numdimes > 1:
        print(numdimes, 'dimes')
    numnickels = int(user_total / 5)
    user_total = int(user_total % 5)
    if numnickels == 1:
        print(numnickels,'nickel')
    elif numnickels > 1:
        print(numnickels, 'nickels')
    numpennies = int(user_total / 1)
    user_total = int(user_total % 1)
    if numpennies == 1:
        print(numpennies,'penny')
    elif numpennies > 1:
        print(numpennies, 'pennies')
    return numdollars, numquarters, numdimes, numnickels, numpennies


if __name__ == "__main__":
    inputval = int(input())
    if inputval <= 0:
        print('no change')
    numdollars, numquarters, numdimes, numnickels, numpennies = exact_change(inputval)

