# Saqib Siddiqui
# PSID: 1495537

new_dict = {}
new_list = []

def add_player():
    print("Enter a new player's jersey number:")
    new_player_number = int(input())
    while(new_player_number < 0 or new_player_number > 99):
        print("Enter new number")
        new_player_number = int(input())
    print("Enter the player's rating")
    new_player_rating = int(input())
    while(new_player_rating < 1 or new_player_rating > 9 ):
        print("Enter new number")
        new_player_rating = int(input())
    new_dict.update({new_player_number:new_player_rating})

def remove_player():
    print("Enter a jersey number:")
    new_player_number = int(input())
    while (new_player_number < 0 or new_player_number > 99):
        print("Enter new number")
        new_player_number = int(input())

    if new_player_number in new_dict.keys:
        del new_dict[new_player_number]

def update_player():
    print("Enter a  jersey number:")
    new_player_number = int(input())
    while (new_player_number < 0 or new_player_number > 99):
        print("Enter new number")
        new_player_number = int(input())
    print("Enter a new player's rating")
    new_player_rating = int(input())
    while (new_player_rating < 1 or new_player_rating > 9):
        print("Enter new number")
        new_player_rating = int(input())

    new_dict[new_player_number] = new_player_rating


def remove_player():
    print("Enter a  jersey number:")
    new_player_number = int(input())
    while (new_player_number < 0 or new_player_number > 99):
        print("Enter new number")
        new_player_number = int(input())

    if (new_player_number in new_dict.keys()):
        del new_dict[new_player_number]

def output_above_rating():
    print("Enter a rating:")
    new_player_rating = int(input())
    while(new_player_rating < 0 or new_player_rating > 9):
        print("Enter new rating")
        new_player_rating = int(input())
    print('ABOVE ' + str(new_player_rating))

    sort_list = sorted(new_dict.keys())

    for j in sort_list:
        if(new_dict[j] > new_player_rating):
            print("Jersey number: " + str(j) + ", Rating: " + str(new_dict[j]))

def output_roster():
    sort_list = sorted(new_dict.keys())
    print("ROSTER")
    for i in sort_list:
        print("Jersey number: " + str(i) + ", Rating: " + str(new_dict[i]))


for i in range(1, 6):
    print("Enter player {}'s jersey number:".format(i))
    new_player_number = int(input())

    while (new_player_number < 0 or new_player_number > 99):
        print("Enter new number")
        print("Enter player {}'s rating:".format(i))
        new_player_number = int(input())

    print("Enter player {}'s rating:".format(i))
    new_player_rating = int(input())

    while (new_player_rating < 0 or new_player_rating > 9):
        print("Enter new number")
        print("Enter player {}'s jersey number:".format(i))
        new_player_number = int(input())

    print()

    new_dict[new_player_number] = new_player_rating



menu_print = ('MENU\n'
                  'a - Add player\n'
                  'd - Remove player\n'
                  'u - Update player rating\n'
                  "r - Output players above a rating\n"
                  'o - Output roster\n'
                  'q - Quit\n')

output_roster()
print()

option = ''


while(option != 'q'):
    print(menu_print)
    print('Choose an option:')
    option = input()



    if (option == 'a'):
            add_player()
            print()

    elif (option == 'd'):
            remove_player()
            print()

    elif (option == 'u'):
        update_player()
        print()

    elif (option== 'r'):
        output_above_rating()
        print()

    elif (option == 'o'):
        output_roster()
        print()

    elif (option == 'q'):
        break










