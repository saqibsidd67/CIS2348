# Saqib Siddiqui
# PSID: 1495537

class ItemToPurchase:
    def __init__(self,item_name = 'none', item_price = 0, item_quantity = 0, item_description = 'none'):
        self.item_name = item_name
        self.item_price = item_price
        self.item_quantity = item_quantity
        self.item_description = item_description

    def print_item_cost(self):
        product = self.item_price * self.item_quantity
        print('{} {} @ ${} = ${}'.format(self.item_name, self.item_quantity, self.item_price, product))

    def print_item_description(self,ItemToPurchase):
        print('{} : {}'.format(self.item_name,self.item_description))



class ShoppingCart:
    def __init__(self, customer_name = 'none', current_date = 'January 1, 2016 ',cart_items = []):
        self.customer_name = customer_name
        self.current_date = current_date
        self.cart_items = cart_items

    def add_item(self,ItemToPurchase):
        self.cart_items.append(ItemToPurchase)

    def remove(self,remove_word):
        for i in self.cart_items:
            if (self.cart_items[i] == remove_word):
                self.cart_item.remove(remove_word)
                break
            else:
                print('Item not found in cart. Nothing removed ')

    def modify_item(self,ItemToPurchase):
        for i in self.cart_tems:
            if(self.cart_items[i].item_name == ItemToPurchase.item_name):
                self.cart_item_quantity[i] = ItemToPurchase.item_quantity[i]
                break
            else:
                print('Item not found in cart. Nothing modified.')

    def get_num_items_in_cart(self):
        num_items = 0
        for i in self.cart_items:
            num_items = num_items + i.item_quantity
        return num_items


    def get_cost_of_cart(self):
        final_price = 0
        price = 0
        for j in self.cart_items:
            price = j.item_price * j.item_quantity
            final_price +=  price
        return final_price

    def print_total(self):
        if (self.get_cost_of_cart() == 0):
            print("{}'s Shopping Cart - {}".format(self.customer_name, self.current_date))
            print("Number of Items: {}".format(self.get_num_items_in_cart()))
            for i in range(len(self.cart_items)):
                i.print_item_cost()
            print()
            print("SHOPPING CART IS EMPTY")
            print()
            print("Total: ${}".format(self.get_cost_of_cart()))
            print()

        else:
            print("{}'s Shopping Cart - {}".format(self.customer_name,self.current_date))
            print("Number of Items:{}".format(self.get_num_items_in_cart()))
            for i in range(len(self.cart_items)):
                i.print_item_cost()
            print()

            print("Total:${}".format(self.get_cost_of_cart()))
            print()

    def print_descriptions(self):
        if (self.get_num_items_in_cart == 0):
            print('SHOPPING CART IS EMPTY')
        else:
            print("{}'s Shopping Cart - {}".format(self.customer_name, self.current_date))
            print('Item Descriptions')
            for i in self.cart_items:
                i.print_item_description




def print_menu(shoppingCart):
    shoppingcart = shoppingCart

    menu_print = ('MENU\n'
                  'a - Add item to cart\n'
                  'r - Remove item from cart\n'
                  'c - Change item quantity\n'
                  "i - Output items' descriptions\n"
                  'o - Output shopping cart\n'
                  'q - Quit\n')

    print()
    print(menu_print)

    option = ''


    while(option != 'q'):
        print('Choose an option:')
        option = input()

        if (option == 'q'):
            break


        while( option != 'a' and option != 'r' and option != 'c' and option != 'i' and option != 'o' and option != 'q'):
         print('Choose an option:')
         option = input()



        if(option == 'a'):
            print('\n ADD ITEM TO CART')
            print('Enter the item name:')
            item_name = input()
            print('Enter the item description')
            item_description = input()
            print('Enter the item price')
            item_price = int(input())
            print('Enter the item quantity')
            item_quantity = int(input())
            add_x = ItemToPurchase(item_name,item_description,item_quantity,item_description)
            shoppingcart.add_item(add_x)

        elif(option == 'r'):
            print('\nREMOVE ITEM FROM CART')
            print('Enter name of item to remove:')
            remove_item = input()
            shoppingcart.remove(remove_item)

        elif(option == 'c'):
            itempurchase = ItemToPurchase()
            print('\nCHANGE ITEM QUANTITY')
            print('Enter the item name:')
            item_to_modify = input()
            print('Enter the new quantity')
            new_quantity = int(input())
            shoppingcart.modify_item(itempurchase)

        elif(option == 'i'):
            print("\nOUTPUT ITEMS' DESCRIPTIONS")
            shoppingcart.print_descriptions()

        elif(option == 'o'):
            print("\n\n\n\nOUTPUT SHOPPING CART")
            shoppingcart.print_total()
        #else:
            #print('Choose an option:')
            #option = input()

        if(option != 'q'):
            print(menu_print)




if __name__ == '__main__' :

    itemtopurchase = ItemToPurchase()
    print("Enter customer's name:")
    customer_name = input()
    print("Enter today's date:")
    current_date = input()
    print()

    print('Customer name: {}'.format(customer_name))
    print("Today's date: {}".format(current_date))

    shoppingCart = ShoppingCart(customer_name,current_date)
    print_menu(shoppingCart)
















