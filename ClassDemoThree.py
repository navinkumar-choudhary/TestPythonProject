# Class with Constructor Parameters

class ConstrParam:
    num = 0
    def __init__(self,val):
        self.num = val
    def ShowDetails(self):
        print("Value of Num is "+str(self.num))

c1 = ConstrParam(100) # Parameterized Constructor
c1.ShowDetails()