student={}
n=int(input("enter number of students:"))
for i in range(n):
    roll=input("enter roll number:")
    name=input("enter a name")
    student[roll]=name
print("student details:")
for roll,name in student.items():
    print("roll no",roll,"name:",name)
