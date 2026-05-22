import csv

data = []

n = int(input("How many contacts do you want to enter? "))

for i in range(n):
    print(f"\nEnter details for Contact {i+1}")
    
    name = input("Enter Name: ")
    address = input("Enter Address: ")
    mobile = input("Enter Mobile: ")
    email = input("Enter Email: ")
    
    data.append([name, address, mobile, email])


with open("address_book.csv", "w", newline="") as file:
    writer = csv.writer(file)
    
    writer.writerow(["Name", "Address", "Mobile", "Email"])
    
    writer.writerows(data)

print("\nData successfully written to address_book.csv")