#machine_status = {
 #   "spinning_frame" : 12,
  #  "weaving_loom" : 4,
   # "carding_unit" : 0
#}

#for key,value in machine_status.items():
 #   if value==0:
  #      print(f"ALERT {key} is completely offline!")
   # elif value>0:
    #    print(f"{key} : {value} units operating")
#
#machine_status["dyeing_vat"]=6

#print(machine_status)

departments = [
    {"dept": "Spinning", "units": 1400, "rate_per_unit": 22},
    {"dept": "Weaving", "units": 2800, "rate_per_unit": 20},
    {"dept": "Dyeing", "units": 950, "rate_per_unit": 25},
    {"dept": "Finishing", "units": 450, "rate_per_unit": 18}
]

high_expense_depts=[]
gtotal=0 
for i in range(len(departments)):
    dcost=departments[i]["units"]*departments[i]["rate_per_unit"]
    print(dcost)
    if dcost>50000:
        print(f"HIGH EXPENSE:{departments[i]["dept"]} exceeded budget with PKR {dcost}")
        high_expense_depts.append(departments[i]["dept"])
    gtotal=gtotal+dcost

print(high_expense_depts)