def calculateSI(principle, time, rateOfInterest):
    si = (principle*time*rateOfInterest)/100
    print("Principle: ",principle)
    print("Time: ", time)
    print("ROI: ", rateOfInterest)
    return si
print(calculateSI(time=2,principle=1000,rateOfInterest=2))