# Saqib Siddiqui
# PSID: 1495537

class ItemToPurchase:
    def __init__ (self, item_name = 'none', item_price = 0, item_quantity = 0):
        self.item_name = item_name
        self.item_price = item_price
        self.item_quantity = item_quantity

    def print_item_cost(self):
        product = self.item_price * self.item_quantity
        print('{} {} @ ${} = ${}'.format(self.item_name,self.item_quantity,self.item_price,product))

if __name__ == '__main__' :
    purchase = ItemToPurchase()
    purchase2 = ItemToPurchase()
    print('Item 1')
    print('Enter the item name:')
    purchase.item_name = input()
    print('Enter the item price:')
    purchase.item_price = int(input())
    print('Enter the item quantity:')
    purchase.item_quantity = int(input())

    print()
    print('Item 2')
    print('Enter the item name:')
    purchase2.item_name = input()
    print('Enter the item price:')
    purchase2.item_price = int(input())
    print('Enter the item quantity:')
    purchase2.item_quantity = int(input())

    print()
    print('TOTAL COST')
    purchase.print_item_cost()
    purchase2.print_item_cost()

    print()
    final_price = (purchase.item_price * purchase.item_quantity) + (purchase2.item_price * purchase2.item_quantity)
    print('Total: ${}'.format(final_price))






