def calculateSI(principle, time, rateOfInterest=2):  # 2 refers to the default value for ROI
    si = (principle*time*rateOfInterest)/100
    return si

print(calculateSI(1000,1,4))
print(calculateSI(1000,1))
