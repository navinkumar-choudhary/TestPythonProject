class Bottle:
    content = ""

    def ShowDetails(self):
        if self.content !="":
            print("This Bottle Contains "+self.content)
        else:
            print("This Bottle is Empty")

    def Fill(self, content1):
        self.content = content1

    def Empty(self):
        self.content = ""

waterBottle = Bottle()
waterBottle.Fill("Water")
waterBottle.ShowDetails()

sodaBottle = Bottle()
sodaBottle.Fill("Soda")
sodaBottle.ShowDetails()
sodaBottle.Empty()
sodaBottle.ShowDetails()