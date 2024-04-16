class Cart:

    def __init__(self):
        self.items = {}
        self.price = {"Apple":25,"Banana": 30}
    
    def add_items(self, Item_name,Item_quantity):
        self.items[Item_name] = Item_quantity

    
    def removing_item(self, Item_name):
        del self.items[Item_name]

    
    def get_cart_items(self):
        cart_item = []
        for items in self.items.keys():
            cart_item.append(items)
        return cart_item


    def updating_quantity(self,Item_name,updated_quantity):
        self.items[Item_name] = updated_quantity


    def get_total_price(self):
        total_price = 0
        for items,quantity in self.items.items():
            total_price += quantity * self.price[items]
        return total_price

cart_obj = Cart()

cart_obj.add_items("Apple","6")
cart_obj.add_items("Banana","6")
print(cart_obj.items)
print(cart_obj.get_cart_items())
cart_obj.removing_item("Banana")
print(cart_obj.items)
print(cart_obj.get_cart_items())
cart_obj.updating_quantity("Apple",12)
print(cart_obj.items)
print(cart_obj.get_cart_items())
print(cart_obj.get_total_price())