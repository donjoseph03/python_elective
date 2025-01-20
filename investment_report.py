amount=float(input("enter the amount: "))
year=int(input("enter the number of years:"))
rate=float(input("enter intrest rate: "))

for i in range(1,year+1):
    interest=amount*rate/100
    amount=amount+interest
    print("%-8d%-20.3f%-20.4f" % (i,interest,amount))
print("-------------------------------------\nTotal amount accumulated: Rs %-20.3f " % amount)
