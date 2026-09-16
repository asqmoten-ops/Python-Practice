units = int(input("Enter number of units."))

bill=0

if units <= 100:
    bill = units * 0.50
elif units > 100 and units<=200 :
    bill = (100*0.50) + ((units-100) * 0.75)
else:
    bill = (100*0.50) + (100 * 0.75) + ((units - 200)*1.20)

if bill>250:
    bill=bill+(bill*0.10)


print(f"Your total amount is {bill}")


