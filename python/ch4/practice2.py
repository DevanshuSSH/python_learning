# WAP ro check grade based on marks (a/b/c/d) using if elif
student1 = int(input("Enter marks of student 1: "))
student2 = int(input("Enter marks of student 2: "))
student3 = int(input("Enter marks of student 3: "))
student4 = int(input("Enter marks of student 4: "))

students_result = (student1, student2, student3, student4)

for marks in students_result:

 if marks >= 75:
    print("grade A")
 elif marks >= 60:
    print("grade B")
 elif marks >= 45:
    print("grade C")
else: 
    print("fail")



