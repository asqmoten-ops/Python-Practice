power_readings = [45, 120, 310, 85, 410, 95, 110, 25]

normal_readings=[]

spike_readings=[]

for i in power_readings:
    if i >200:
        spike_readings.append(i)

    else:
        normal_readings.append(i)

spike_readings.sort()
normal_readings.sort()

total=0
count=0

for j in normal_readings:
    total=total + j
    count+=1

mean_normal_readings=total/count

print(f"The mean of normal reading is {mean_normal_readings}")

print(f"The number of dangerous spikes is {len(spike_readings)}")

hspike=spike_readings[-1]

print(f"The single highest spike is {hspike}")