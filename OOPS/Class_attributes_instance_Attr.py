class Cart:
    
    # Class Attributes
    flat_discount = 0
    min_bill = 100
    
    def __init__(self):
        
        # Instance Attribute  we use Self. for IA
        self.items = {}

###########################################################

## Methods

# Instance
# Class
# Static


##########################---------Instance----Method--------####################################

class Cart:

    flat_discount = 0
    min_bill = 100
    def __init__(self):
        self.items = {}

    def add_item(self,Item_name,Item_quantity):
        self.items[Item_name] = Item_quantity 

    def display_items(self):
        print(self.items)

a = Cart()
a.add_item("Apple",6)
a.display_items


################################------Class---Methods---########################################


class Cart:
    flat_discount = 0
    min_bill = 100

    # Decorator
    @classmethod
    
    def update_flat_discount(cls,new_flat_discount):
        cls.flat_discount = new_flat_discount

    @classmethod

    def increase_flat_discount(cls,amount):
        new_flat_discount = cls.flat_discount + amount
        cls.update_flat_discount(new_flat_discount)  


# Calling class method

Cart.update_flat_discount(200)
print(Cart.flat_discount)
Cart.increase_flat_discount(300)



####################################------Static----Methods------######################################


class Cart:

    flat_discount = 0
    min_bill = 100
    def __init__(self):
        self.items = {}

    def add_item(self,Item_name,Item_quantity):
        self.items[Item_name] = Item_quantity 

    def display_items(self):
        print(self.items)

    # Decorator
    @classmethod
    
    def update_flat_discount(cls,new_flat_discount):
        cls.flat_discount = new_flat_discount

    @staticmethod

    def greet():
        print("have a Great shopping time!!!")
    

a = Cart()
a.add_item("Apple",6)
a.display_items

Cart.update_flat_discount(200)
print(Cart.flat_discount)
Cart.greet()