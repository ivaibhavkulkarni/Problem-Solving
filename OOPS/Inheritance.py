# Inheritence 

# Super Class

class Product():

    def __init__(self,name,price,deal_price,ratings):
        self.name = name
        self.price = price
        self.deal_price = deal_price
        self.ratings = ratings
        self.your_savings = price - deal_price

    def display_items(self):
        print("Product Name: {}".format(self.name))
        print("Price: {}".format(self.price))
        print("Deal price: {}".format(self.deal_price))
        print("Rating: {}".format(self.ratings))


# Subclass
class ElectronicItems(Product):
    def set_warranty(self,warranty_in_months):
        self.warranty_in_months = warranty_in_months

    def get_warranty(self):
        return ("Warranty in months: {}".format(self.warranty_in_months))


    def display_electronic_items(self):
        self.display_items()
        print("Warranty in months: {}".format(self.warranty_in_months))


class GroceryItems(Product):
    def set_expiry_date(self,expiry_date):
        self.expiry_date = expiry_date

    def get_expiry_date(self):
        return "Expiry date: {}".format(self.expiry_date)
     


##### WAY 1 
e = ElectronicItems("Laptop",30000,25000,5)
e.display_items()
e.set_warranty(24)
print(e.get_warranty())

print("- - - - - - - - - ")

##### WAY 2
p1 = ElectronicItems("Tv",45000,42000,4.0)
p1.set_warranty(48)
p1.display_electronic_items()


print("- - - - - - - - - - - -")

g = GroceryItems("Horlicks",60,59,5)
g.display_items()
g.set_expiry_date("6-3-2022")
print(g.get_expiry_date())
