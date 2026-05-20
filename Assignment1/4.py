# Input student details
name = input("Enter student name: ")
student_class = input("Enter class: ")

total = 0

for i in range(1, 6):
    marks = float(input(f"Enter marks of subject {i}: "))
    total += marks

percentage = (total / 500) * 100


if percentage >= 60:
    grade = 'A'
elif percentage >= 50 and percentage < 60:
    grade = 'B'
elif percentage >= 40 and percentage < 50:
    grade = 'C'
elif percentage >= 33 and percentage < 40:
    grade = 'D'
else:
    grade = 'Fail'

print("\nRESULT---")
print("Name       :", name)
print("Class      :", student_class)
print("Total Marks:", total)
print("Percentage :", percentage)
print("Grade      :", grade)