present=0
present_students=[]
absent=0
total_students=int(input("Enter the total number of students: "))
for i in range(total_students):
    name=input("Enter the name of the student: ")
    status=input("Enter 'P' for present and 'A' for absent: ").upper().strip()
    if status=='P':
        present+=1
        present_students.append(name)
    elif status=='A':
        absent+=1
    else:
        print("Invalid input. Please enter 'P' or 'A'.")
print("-" * 15, "Attendance Report", "-" * 15)
print("Total number of students:", total_students)
print("Total number of students present:", present)
print("Total number of students absent:", absent)
for i in range(len(present_students)):
    print(i+1, present_students[i])
print("-" * 30)