defect_count = 0 
for i in range(1,6):
    status=input(f"Batch {i} : Enter status (Pass/Defect)")
    if status.lower()=="defect":
        defect_count += 1

        if defect_count==3:
            print("CRITICAL ALERT: Production line stopped due to high defects!")
            break

print(f"Audit Complete. Total Defects Found is {defect_count}")


