# Private Protected - Called as Data Hiding

class A:
    def __init__(self):
        self.__x = 10 #
    def _ShowX(self):
        print("Showing x value from class A", self.__x)
    def Display(self):
        self._ShowX()
class B(A):
    def __init__(self):
        super().__init__()
    def Print(self):
        self._ShowX()

obj = A()
obj.Display()

objb = B()
objb.Print()