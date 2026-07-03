name=input("Enter your name: ")
marks=int(input("Enter your marks: "))
if marks>=90:
    grade='A'  
    print("Hello", name, "your grade is:", grade)
elif marks>=80:
    grade='B'
    print("Hello", name, "your grade is:", grade)
elif marks>50:
    grade='C'  
    print("Hello", name, "your grade is:", grade)
elif marks<33 and marks>=0:
    grade='F'
    print("Hello", name, "your grade is:", grade)
else:
    print("Invalid marks entered.")
   
