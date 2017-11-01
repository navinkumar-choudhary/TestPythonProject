import sys

num1 = 10
num2 = 5
arr = [10, 20, 30]

result = 0
try:
    result = num1/num2
except ZeroDivisionError:
    print("Error: ", sys.exc_info()[1])
finally:
    print("Finally Executed....... for 1st try")

try:
    print(arr[5])
except IndexError:
    print("Error: :", sys.exc_info()[1])
#    print("IndexError: list index out of range >> trying to access the number which is not there in the array")
#    print(IndexError)
finally:
    print("Finally Executed....... for 2nd try")
print(result)
print("Program Ended Normally")

try:
    limit = int (input("Enter the Number: "))
    if limit<1000:
        print("Within Limit")
    else:
        raise IndexError("Index Error")
except IndexError:
    print("Raised Exception Handled")