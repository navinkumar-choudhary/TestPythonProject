
def printAll(*n):
    for i in n:
        print(i)

printAll(10, 20, 30, 40, 50)

def sumAll(*n):
    sum = 0
    for i in n:
        sum = sum+i
    print(sum)
sumAll(10, 20, 30)
sumAll(10, 20)
sumAll(10, 20, 30, 40, 50)

# Passing N numbers from user and halt when 0 and add all
def sumAllNumners (n):
    sum1 = 0
    for i in n:
        sum1+=i
    return sum1

numbers = []
i=1
while i != 0:
    i = int(input("Enter the numbers to be added and 0 to stop: "))
    numbers.append(i)
print(sumAllNumners(numbers))