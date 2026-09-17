#Question 1
out1=bool("")
out2=bool(0)
out3=bool("False")
print(out1, out2, out3)

#False, False, True

#Question 2
total = 0
for num in range(1, 8):
    if num % 2 == 0:
        continue
    if num > 5:
        break
    total += num
print(f"Final Total: {total}") #I predicted 9

#Question 3
count = 0
while count < 10:
    count +=1
    print(f"T-minus {count}")
    if count == 5:
        print("Halfway there")
print("Blast off!")
#(Hint: Why will the screen freeze when running this loop?)

# The loop will run infintie amount of times so I changed count to 1 and added a counting statement in line 20. and edited line 19.

#Question 4

fuel = int(input("Enter fuel amount. "))
genhrs=0
while True:
    burfuel=int(input("Enter amount of fuel burned in an hour."))
    genhrs +=1
    fuel=fuel-burfuel
    if fuel<=0:
        print("Generator Halted: Fuel Depleted")
        break
    elif fuel<=20:
        print("LOW FUEL WARNING: Refuel immediately!")

print(f"Total hours run is {genhrs}")
 