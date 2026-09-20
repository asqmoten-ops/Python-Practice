machine_status = {
    "spinning_frame" : 12,
    "weaving_loom" : 4,
    "carding_unit" : 0
}

for key,value in machine_status.items():
    if value==0:
        print(f"ALERT {key} is completely offline!")
    elif value>0:
        print(f"{key} : {value} units operating")

machine_status["dyeing_vat"]=6

print(machine_status)

