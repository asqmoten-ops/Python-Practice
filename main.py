# Challenge 1

#salary= int(input("Enter your salary")) 
#age= int(input("Enter your age"))

#if salary < 50000:
#    tax=0
#elif salary > 50000:
#    if age > 60:
#        tax=5
#    else:
#        tax=10

#print(f"Your calculated tax is {tax}%")


# Challenge 2

mathscore=int(input("Enter Math Score"))
engscore=int(input("Enter English Score"))
extracurricular=input("Do you have any ECAs?")

if mathscore<85 :
    print("Rejected. Math requirements not met.")
else:
    if engscore<75:
        print("Rejected. English requirements not met.")
    else:
        if extracurricular=="yes":
            print("Directly Admitted")
        else:
            print("Waitlisted. Missing ECAs.")    




