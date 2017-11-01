# Function with Parameters and Returns value
def addNumbers(num1, num2):
    sum = num1 + num2
    return sum
print(addNumbers(10,20))

# Function without Parameters and does not return any value
def show():
    print("Simple Function without Parameters and without return value")
show()

# Function without parameter but returns value
def myName():
    return "NAveen"
print(myName())

# Function with Parameters but does not return value
def myCity(city):
    print("My city name is: "+city)
myCity("Goa")

# Variable scope
y = 20000
def scopeDemo():
    x = 10000
    print(x)
    print(y)

scopeDemo()
# print(x) #> we can't access the x outside the Function as it is local variable
print(y) # but we can print y outside the function as it is Global Variable
