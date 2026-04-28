student = {
    "name": "Anmol",
    "age": 20,
    "marks": 85
}

print(student["name"])

student["city"] = "Kota"

student["marks"] = 90

del student["age"]

for key, value in student.items():
    print(key, ":", value)