#1. Concept & Code Reading (Predict output without running):
#   data = [10, 20, 30]
#alias = data
#alias.append(40)
#print(f"Original: {data}")
#print(f"Alias: {alias}")

#ANSWER: Alias will print only 40 as it the data list has been replaced by 40.

  # (Question: Why did data change? What is the name of this memory concept?)

 #* 2. 2D List Challenge (Shift Operations):
  # A 2D matrix is given where each row represents a shift and the columns represent the fabric output (in meters) of 3 machines:


  # * Calculate and print the total fabric output for each shift (use a nested loop).
  #  * Print the grand total for the entire day.
shifts = [
    [120, 150, 130],  # Morning Shift
    [100, 110, 105],  # Evening Shift
    [80, 95, 90]      # Night Shift
]

total=0
gtotal=0
for i in range(len(shifts)):
    total=0
    for j in range(len(shifts[i])):
        total= total + shifts[i][j]
    gtotal=gtotal+total
    print(f"Total output of this shift is {total}")

print(f"Grand Total for the entire day is {gtotal}")
 #* 3. List Manipulation & Sanitization:
  # Given list:
sensor_logs = [45, -999, 52, 60, -999, 48, 55, -999, 50]

clean_logs = []
for x in sensor_logs:
    if x == -999:
        continue
    else:
        clean_logs.append(x)

clean_logs.sort(reverse=True)

print(clean_logs[-1], clean_logs[0])


   #-999 represents a sensor error reading.
   #* Create a new list clean_logs that contains only valid readings (filter out -999).
   #* Sort clean_logs in descending order (highest to lowest).
   #* Print the minimum and maximum values without using min() or max(), relying strictly on the indices of the sorted list.

 #* 4. Push to GitHub:
  # * Create the hw3.py file and commit it:
   #  git add hw3.py
#git commit -m "Complete Day 3: Lists, 2D arrays, and sensor data cleanup"
#git push
