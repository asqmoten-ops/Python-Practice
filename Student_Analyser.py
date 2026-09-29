#Sample Dataset

course_data=[
    {"student_id" : "ST-101", "name" : "Ali", "quizzes" : [85, 90, 78], "attendance" : 92},
    {"student_id" : "ST-102", "name" : "Sara", "quizzes" : [95, 98, 92], "attendance" : 88},
    {"student_id" : "ST-103", "name" : "Bilal", "quizzes" : [60, 58, 65], "attendance" : 70},
    {"student_id" : "ST-104", "name" : "Zainab", "quizzes" : [40, 55, 50], "attendance" : 81}
]

# Average Calculator
def calculate_avg(scores):
    if len(scores)==0:
        return 0.0
    return sum(scores)/len(scores)

# Grade Assigner
def assign_grade(avg_score):
    if avg_score>=85:
        return("A")
    elif avg_score>=70:
        return("B")
    elif avg_score>=50:
        return("C")
    else:
        return("F")

# Testing Code
for student in course_data:
    scores=student["quizzes"]
    avg=calculate_avg(scores)
    grade=assign_grade(avg)
    print(f"Student: {student["name"]}, Average Score: {avg:.1f}, Grade: {grade}")

#Task 2 + Test

def process_student_records(students_list):
    processed_report = []
    for student in students_list:
        scores=student["quizzes"]
        avg=calculate_avg(scores)
        grade=assign_grade(avg)
        attendance=student["attendance"]
        if attendance >= 85 and grade != "F": 
            status="PASSED"
        else:
            status="Failed"
        processed_report.append({
            "student_id": student["student_id"],
            "name": student["name"],
            "average": round(avg, 2),
            "grade": grade,
            "status": status
        })
    return processed_report
processed_report=process_student_records(course_data)
print(processed_report)

# Global Average of Class

def global_average(p_report):
    classavg=0.0
    passed=0
    need_att=0
    totalscore=0.0
    top_performer=""
    h_avg=-1
    globalavg=[]
    for pupil in p_report:
        if pupil["status"]=="PASSED":
            passed +=1
        else:
            need_att +=1
        totalscore +=pupil["average"]

        if pupil["average"]>h_avg:
            h_avg=pupil["average"]
            top_performer=pupil["name"]

    classavg=totalscore/len(p_report)
    globalavg.append({
        "Class Average": round(classavg, 2),
        "Total Passed": passed,
        "Need Attention": need_att,
        "Top Performer": top_performer
    })
    return globalavg

print(global_average(processed_report))

def display_menu():
    print("\n" + "="*40)
    print("   STUDENT COURSE & GRADE ANALYZER CLI")
    print("="*40)
    print("1. View Full Student Report")
    print("2. View Class Summary & Metrics")
    print("3. Search Student by Name")
    print("4. Exit")
    print("="*40)

def main():
    report = process_student_records(course_data)
    
    while True:
        display_menu()
        choice = input("Select an option (1-4): ").strip()
        
        if choice == "1":
            for student in report:
                print(student)
            # Loop chala kar 'report' ke saare students print karen
            pass
            
        elif choice == "2":
            print(global_average(report))
            # 'global_average(report)' call karen aur metrics display kare
            pass
            
        elif choice == "3":
            name=input("Enter Name ").strip()
            found=False
            for person in report:
                if name.lower()==person["name"].lower():
                    print("Name is found")
                    found=True
                    break
            if not found:
                print("Name not found")
            # YOUR CHALLENGE: User se name input len aur 'report' mein search karke match print karen
            pass
            
        elif choice == "4":
            print("Exiting CLI. Goodbye!")
            break
        else:
            print("Invalid selection! Try again.")
if __name__ == "__main__":
    main()

