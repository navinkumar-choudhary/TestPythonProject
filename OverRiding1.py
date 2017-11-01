# OverRiding 

class A:
    def Display(self):
        print("Display Method in Class A")
class B(A):
    def __init__(self):
        print("Object of Class B is Created")
    def Display(self):
        super().Display()
        print("Overridden Display Method of class A in Class B")
b = B()
b.Display()