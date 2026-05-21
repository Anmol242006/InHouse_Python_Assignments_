"""
Practise reading, writting, appending data in a file"""



while True:
    print("\n----- FILE HANDLING MENU -----")
    print("1. Write Data")
    print("2. Read Data")
    print("3. Append Data")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        data = input("Enter data to write: ")

        with open("practice.txt", "w") as file:
            file.write(data)

        print("Data written successfully")

    elif choice == "2":
        try:
            with open("practice.txt", "r") as file:
                content = file.read()

            print("\nFile Content:")
            print(content)

        except FileNotFoundError:
            print("File does not exist")

  
    elif choice == "3":
        data = input("Enter data to append: ")

        with open("practice.txt", "a") as file:
            file.write("\n" + data)

        print("Data appended successfully")


    elif choice == "4":
        print("Program Ended")
        break

    else:
        print("Invalid Choice")