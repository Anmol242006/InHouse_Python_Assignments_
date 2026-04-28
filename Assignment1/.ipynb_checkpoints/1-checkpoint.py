name_ = input("Enter student name: ")
class_ = input("Enter class: ")

total = 0

for i in range(1, 6):
    marks = float(input(f"Enter marks of Subject {i}: "))
    total += marks

percentage = (total / 500) * 100

print("\nStudent Result!")
print("Name:", name_)
print("Class:", class_)
print("Total Marks:", total)
print("Percentage:", percentage, "%")