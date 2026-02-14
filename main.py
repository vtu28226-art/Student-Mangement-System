import csv
import os

FILE_NAME = "students.csv"


# -----------------------------
# Add Student
# -----------------------------
def add_student():
    name = input("Enter student name: ")
    roll = input("Enter roll number: ")

    try:
        marks = float(input("Enter marks: "))
    except ValueError:
        print("Invalid marks! Please enter numbers only.\n")
        return

    with open(FILE_NAME, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([name, roll, marks])

    print("Student added successfully!\n")


# -----------------------------
# View All Students
# -----------------------------
def view_students():
    if not os.path.exists(FILE_NAME):
        print("No records found.\n")
        return

    with open(FILE_NAME, "r") as file:
        reader = csv.reader(file)
        students = list(reader)

        if not students:
            print("No students available.\n")
            return

        print("\n--- Student Records ---")
        for student in students:
            print(f"Name: {student[0]}, Roll: {student[1]}, Marks: {student[2]}")
        print()


# -----------------------------
# Search Student
# -----------------------------
def search_student():
    roll_search = input("Enter roll number to search: ")

    if not os.path.exists(FILE_NAME):
        print("No records found.\n")
        return

    found = False

    with open(FILE_NAME, "r") as file:
        reader = csv.reader(file)
        for student in reader:
            if student[1] == roll_search:
                print(f"Found: Name: {student[0]}, Marks: {student[2]}\n")
                found = True
                break

    if not found:
        print("Student not found.\n")


# -----------------------------
# Delete Student
# -----------------------------
def delete_student():
    roll_delete = input("Enter roll number to delete: ")

    if not os.path.exists(FILE_NAME):
        print("No records found.\n")
        return

    updated_students = []
    found = False

    with open(FILE_NAME, "r") as file:
        reader = csv.reader(file)
        for student in reader:
            if student[1] != roll_delete:
                updated_students.append(student)
            else:
                found = True

    with open(FILE_NAME, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerows(updated_students)

    if found:
        print("Student deleted successfully!\n")
    else:
        print("Student not found.\n")


# -----------------------------
# Update Student Marks
# -----------------------------
def update_student():
    roll_update = input("Enter roll number to update: ")

    if not os.path.exists(FILE_NAME):
        print("No records found.\n")
        return

    updated_students = []
    found = False

    with open(FILE_NAME, "r") as file:
        reader = csv.reader(file)
        for student in reader:
            if student[1] == roll_update:
                try:
                    new_marks = float(input("Enter new marks: "))
                except ValueError:
                    print("Invalid input.\n")
                    return
                student[2] = new_marks
                found = True
            updated_students.append(student)

    with open(FILE_NAME, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerows(updated_students)

    if found:
        print("Student updated successfully!\n")
    else:
        print("Student not found.\n")


# -----------------------------
# Main Menu
# -----------------------------
def main():
    while True:
        print("===== Student Management System =====")
        print("1. Add Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Delete Student")
        print("5. Update Student Marks")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_student()
        elif choice == "2":
            view_students()
        elif choice == "3":
            search_student()
        elif choice == "4":
            delete_student()
        elif choice == "5":
            update_student()
        elif choice == "6":
            print("Exiting program...")
            break
        else:
            print("Invalid choice. Try again.\n")


if __name__ == "__main__":
    main()
