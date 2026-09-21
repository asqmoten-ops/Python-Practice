students = [
    {"name": "Ali", "scores": [80, 75, 90]},
    {"name": "Sara", "scores": [95, 88, 92]},
    {"name": "Bilal", "scores": [60, 55, 70]}
]


for i in range(len(students)):
    sum=0
    for score in students[i]["scores"]:
        sum=sum+score
    avg=sum/len(students[i]["scores"])
    if avg>=85:
        print( f"{students[i]["name"]} has achieved Grade A with an average of {avg}")
    else:
        print( f"{students[i]["name"]} has achieved Grade B with an average of {avg}")

raw_config = {
    "voltage": 240,
    "frequency": 50
}

voltage=raw_config.get("voltage")
freq=raw_config.get("frequency")
phase=raw_config.get("phase", 3)

print(f"V: {voltage}, F: {freq}, Phase: {phase}")
