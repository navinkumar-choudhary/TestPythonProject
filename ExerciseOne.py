# 1
print("Hello \nNavin")

# 2
print(4+50)

# 3
print(round(4/2))

# 4
print(-5 + 8 * 6)
print((55+9) % 9)
print(20 + (-3)*5 / 8)
print(5 + 15 / 3 * 2 - 8 % 3)

# 5
num1 = int (input("Enter the First Number: "))
num2 = int (input("Enter the Second Number: "))
print(num1*num2)

# 6
print((5+2),(5*2),(5-2),(4/2),(5%2))

# 7
print(((25.5 * 3.5 - 3.5 * 3.5) / (40.5 - 4.5)))

# 8
print(4.0 * (1 - (1.0/3) + (1.0/5) - (1.0/7) + (1.0/9) - (1.0/11)))

#9
radius = 4
pi=3.14
areaofCircle = (pi*(radius**2))
circumferenceofCircle = 2*pi*radius
print("Area of Circle: ", areaofCircle)
print("Circumference of Circle",circumferenceofCircle)

#10 convert temperature from Fahrenheit to Celsius degree.
fahrenheit = int(input("Please enter the temperature in Fahrenheit to convert into Celsius: "))
celsius = (fahrenheit - 32)*5/9
print("%s Fahrenheit is equals to %s Celsius"%(fahrenheit,celsius))

#11 program that reads a number in inches, converts it to meters.
inches = int (input("Enter the Inches to convert to Meters: "))
meters = inches*0.0254
print("%s inches equals to %s meters"%(inches,meters))

#12 reads an integer between 0 and 1000 and adds all the digits in the integer
intNum = -4
isInteger = False
number = []
sum = 0
while isInteger != True:
    intNum = int (input("Please enter the Integer between 0 to 1000: "))
    if intNum in range(0,1000):
        isInteger = True
print("Integer Number entered by you is: %s"%intNum)
newInt = str(intNum)
for digit in newInt:
    number.append(int(digit))
for i in number:
    sum+=i
print("The sum of the Digits of a Integer entered by you is: ",sum)


#13 convert minutes into a number of years and days

mins = int (input("Enter the Minutes to Convert to Years and days: "))

days = round((mins/(60*24)))
print("%s Min(s) are equals to %s Day(s)."%(mins,days))

#14 program that reads a number and display the square, cube, and fourth power.
num = int(input("Enter the Number: "))
print("For the Number %s the Square is %s, Cube is %s and Fourth power is %s"%(num, num**2, num**3, num**4))

#15 program to break an integer into a sequence of individual digits

intNum = int(input("Enter the Number: "))
number = []
newInt = str(intNum)
for digit in newInt:
    number.append(int(digit))
print("character sequence in the Given number %s is "%intNum)
for i in number:
    print(i)

#16 program to get a number from the user and print whether it is positive or negative.
num = int(input("Please enter the Number to check +ve ot -ve: "))
if num < 0:
    print("%s is an Nagetive integer."%num)
else:
    print("%s is an Positive integer."%num)

#17 program that reads a floating-point number and prints "zero" if the number is zero.



#18 Write a Python program that takes the user to provide a single character from the alphabet.
# Print Vowel or Consonant, depending on the user input.
# If the user input is not a letter (between a and z or A and Z) print an error message.
char = input("Please enter the character: ")
if char in ('a','e','i','o','u','A','E','I','O','U'):
    print("%s character is Vowel."%char)
elif char in ('b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v','w','x','y''z','B','C','D','F','G','H','J','K','L','M','N','P','Q','R','S','T','V','W','X','Y''Z'):
    print("%s character is Consonant"%char)
else:
    print("%s character is not valid."%char)


#19 Python program that takes a year from user and print whether that year is a leap year or not
year = int(input("enter the Calender Year: "))
isLeap = False

if year%4 == 0 and year%100 == 0 and year%400 == 0 :
    print("%s is a leap year.")
else:
    print("%s is not a leap year.")

#20 program to display n terms of natural numbers and their sum.

nTerm = int(input("Enter the N term for Natural Numbers to display the sum of those numbers: "))
sum = 0
i = 1
print("%s terms of naturals Numbers are: "%nTerm)
for j in range(i,nTerm+1):
    print(j)
for i in range(i,nTerm+1):
    sum+=i
print("Sum of an N Terms of Inters is",sum)


#21 program in Python to display the cube of the number upto given an integer
term = int (input("Enter the term: "))
j = 1
print("cube of the numbers up to given an integer %s" %term)
for i in range (j,term):
    print(i**3)