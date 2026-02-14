def add_student():
    name = input("Enter student name: ")
    roll = input("Enter roll number: ")
    marks = input("Enter marks: ")

    with open("students.txt", "a") as file:
        file.write(f"{name},{roll},{marks}\n")

    print("Student added successfully!\n")


def view_students():
    try:
        with open("students.txt", "r") as file:
            students = file.readlines()
            if not students:
                print("No students found.\n")
            else:
                for student in students:
                    name, roll, marks = student.strip().split(",")
                    print(f"Name: {name}, Roll: {roll}, Marks: {marks}")
    except FileNotFoundError:
        print("No student records found.\n")


def main():
    while True:
        print("1. Add Student")
        print("2. View Students")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_student()
        elif choice == "2":
            view_students()
        elif choice == "3":
            print("Exiting program...")
            break
        else:
            print("Invalid choice. Try again.\n")


if __name__ == "__main__":
    main()
