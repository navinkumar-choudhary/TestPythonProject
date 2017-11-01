# Class with Constructor Parameters

class Cars:
    name = ""
    brand = ""
    price = 0
    def __init__(self,name1,brandName1,price1):
        self.name = name1
        self.brand = brandName1
        self.price = price1

    def ShowCarDetails(self):
        print(self.name+" is of Brand "+"\'"+self.brand+"\'"+" and price is "+str(self.price))

car1 = Cars("Nano","Tata",200000) # Parameterized Constructor
car1.ShowCarDetails()