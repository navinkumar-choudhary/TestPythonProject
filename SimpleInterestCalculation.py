# Python Program to Calculate the Simple Interest

PrincipleAmount =float( input("Enter Principle Amount: "))
Time = int(input("Enter the Time in Years: "))
RateOfInterest = float(input("Enter the Rate Of Interest: "))

simpleInterest = (PrincipleAmount*Time*RateOfInterest)/100
print(simpleInterest)