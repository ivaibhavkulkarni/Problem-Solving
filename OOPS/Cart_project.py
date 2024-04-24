class Product:

    def __init__(self,Product_name,quantity,Price,Deal_price,Rating):
        self.Product_name = Product_name
        self.quantity = quantity
        self.Price = Price
        self.Deal_price = Deal_price
        self.Rating = Rating

    def Display_Items(self):
        print("Product name: {}".format(self.Product_name))
        print("Quantity: {}".format(self.quantity))
        print("Price: {}".format(self.Price))
        print("Deal Price: {}".format(self.Deal_price))
        print("Rating: {}".format(self.Rating))

    def Get_Deal_price(self):
        return self.Deal_price


class Electronic_Items(Product):
    
    def __init__(self,Product_name,quantity,Price,Deal_price,Rating,warranty):
        super().__init__(self,Product_name,Price,Deal_price,Rating)
        self.warranty = warranty

    def Get_Warranty(self):
        print("Warranty: {}".format(self.Warranty))

    def Display_Items(self):
        super().Display_Items()
        print("Warranty: {}".format(self.warranty))


class Grocery_Items(Product):
    
    def Set_expiry(self,Expiry):
        self.Expiry = Expiry

    def Get_expiry(self):
        print("Expiry date: {}".format(self.Expiry))

    def Display_grocary_items(self):
        self.Display_Items()
        print("Expiry Date: {}".format(self.Expiry))


class Order:

    def __init__(self,Delivery_Speed,Delivery_address):
        self.cart_items = []
        self.Delivery_speed = Delivery_Speed
        self.Delivery_address = Delivery_address

    def add_item(self,Product,Quantity):
        self.cart_items.append((Product,Quantity))
    
    def Display_order_details(self):
        for Product , Quantity in self.cart_items:
            Product.Display_Items()
            print("Quantity: {}".format(Quantity))

    def Display_order_bill(self):
        total_bill = 0
        for Product, Quantity in self.cart_items:
            price = Product.Get_Deal_price() * Quantity
            total_bill += price
        print("Total bill: {}".format(total_bill))

################ Method 1 Method Overidding

tv = Electronic_Items("Tv",1,1999,1899,5.0,28)
tv.Display_Items()

################## Methos 2

milk = Grocery_Items("Milk",2,30,30,5.0)
milk.Set_expiry("24h")
milk.Display_grocary_items()

order = Order("Prime delivery","hyderabad")
order.add_item(tv,1)
order.add_item(milk,2)
order.Display_order_details()
order.Display_order_bill()







