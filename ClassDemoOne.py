# Data Encapsulation Concept

class Calculator:
    name = ""
    price = 0

    def Details(self):
        print(self.name+'\'s'+ " Price is "+str(self.price))

    def SetDetails(self, name1, price1):
        self.name = name1
        self.price = price1


camel = Calculator()
camel.name = "Camel"
camel.price = 5000
camel.Details()

casio = Calculator()
casio.name = "casio"
casio.price = 5001
casio.Details()

print("Updated Details of the Calculators are as Below")

update = Calculator()
update.SetDetails("Bosch",1000)
update.Details()