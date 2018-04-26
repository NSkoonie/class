#hw8p5
#Noah Schoonover

class RetailItem():

    def __init__(self, description, units_in_inventory, price):
        self.description = description
        self.units_in_inventory = units_in_inventory
        self.price = price

item1 = RetailItem('Jacket', 12, 59.95)
item2 = RetailItem('Designer Jeans', 40, 34.95)
item3 = RetailItem('Shirt', 20, 24.95)

print('{:17}{:>10}{:>10}'.format('Description', 'Inv', 'Price'))
print()
for item in (item1, item2, item3):
    print('{:17}{:10}{:10}'.format(item.description, item.units_in_inventory, item.price))
