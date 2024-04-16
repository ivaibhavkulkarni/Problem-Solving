# Assigning values to Properties we use __int__ method

class Mobile:
    
    # Constructor to initialize properties
    def __init__(self, Model,Camera):
        self.Model = Model
        self.Camera = Camera

    # acessing inside attribute

    def Get_attri(self):
        print(self.Model)


    # Action method
    def Making_call(self, number):
        print("Calling...{}".format(number))


    # Updating model 
    def updating_model(self,update_model):
        self.Model = update_model

# Creating an Object
Mobile_1 = Mobile("IPhone 4s", "5 Mp")
Mobile_1.Making_call(95050403)
print(type(Mobile_1))
Mobile_1.Get_attri()
Mobile_1.updating_model("Iphone XX")
Mobile_1.Get_attri()


# NOTE :
# Properties are refered as Attributes
# Actions are reffered as Methods
