class Vehicle:
    def __init__(self,c,p):
        self.color = c
        self.price = p
class Car(Vehicle):
    def __init__(self, c, p, t):
        super().__init__(c ,p)
        self.numberOfTyres = t
class Bike(Vehicle):
    def __init__(self, c, p, t):
        super().__init__(c ,p)
        self.numberOfTyres = t
b = Bike("Red",150000,2)
c = Car("Blue",250000,4)
print(b.color)
print(b.price)
print(b.numberOfTyres)
print(c.color)
print(c.price)
print(c.numberOfTyres)