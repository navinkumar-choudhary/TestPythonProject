name = "Navin"
def fun(x):
    print("value from fun one: ",name)
    print("X value before modification in Fun1: ", x)
    x = 100
    print("X value after modification in Fun1: ", x)

def main():
    print("Hi")
    print("Value from main: ",name)
    x=20
    fun(x)
    print("Value of x in main method: ",x)

main()