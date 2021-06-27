# Hunter Barrows    1550107

# Zylab 10.17

# Define class for total of item

class ItemToPurchase:
    def __init__(self):
        self.item_name = "none"
        self.item_price = 0
        self.item_quantity = 0
    def print_item_cost(self):
        total = self.item_price * self.item_quantity
        print(self.item_name, str(self.item_quantity), "@ ${}".format(self.item_price), "= ${}".format(total))

# Get item 1 input

if __name__ == "__main__":
    print("Item 1")
    Get_item1 = ItemToPurchase()
    Get_item2 = ItemToPurchase()
    Get_item1.item_name = input('Enter the item name:\n')
    Get_item1.item_price = int(input('Enter the item price:\n'))
    Get_item1.item_quantity = int(input('Enter the item quantity:\n'))

# Get item 2 input

    print("\nItem 2")
    Get_item2.item_name = input('Enter the item name:\n')
    Get_item2.item_price = int(input('Enter the item price:\n'))
    Get_item2.item_quantity = int(input('Enter the item quantity:\n'))

# Get total cost of items

    print("\nTOTAL COST")
    Get_item1.print_item_cost()
    Get_item2.print_item_cost()
    total = (Get_item1.item_price * Get_item1.item_quantity) + (Get_item2.item_price * Get_item2.item_quantity)
    print("\nTotal: ${}".format(total))
