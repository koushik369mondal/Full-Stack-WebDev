class Student:
    def __init__(self, name: str, age: int, address: str, marks: int) -> None:
        self.name = name
        self.age = age
        self.address = address
        self.marks = marks


class StudentManagementSystem:
    def __init__(self):
        self.students = []

    def add_student(self):
        try:
            name = input("Enter name: ")
            age = int(input("Enter age: "))
            address = input("Enter Address: ")
            marks = int(input("Enter Marks: "))

            student = Student(name, age, address, marks)
            self.students.append(student)
            print("Student Successfully Added")
            return student
        except ValueError:
            print("Invalid input! Please enter correct data types (e.g., integer for age and marks).")

    def view_students(self):
        if len(self.students) == 0:
            print("No students found.")
        else:
            view_type = input("View All Students or One Student? (all/one): ").lower()
            if view_type == "all":
                for student in self.students:
                    self.print_student(student)
            elif view_type == "one":
                name = input("Enter the name of the student you want to see: ")
                found = False
                for student in self.students:
                    if student.name.lower() == name.lower():
                        self.print_student(student)
                        found = True
                        break
                if not found:
                    print(f"No student found with the name '{name}'")
            else:
                print("Invalid input! Please enter 'all' or 'one'.")

    def delete_student(self):
        name = input("Enter the name of the student you want to delete: ")
        found = False
        for student in self.students:
            if student.name.lower() == name.lower():
                self.students.remove(student)
                print(f"Student '{name}' successfully deleted.")
                found = True
                break
        if not found:
            print(f"No student found with the name '{name}'.")

    def update_student(self):
        name = input("Enter the name of the student you want to update: ")
        found = False
        for student in self.students:
            if student.name.lower() == name.lower():
                found = True
                print("What would you like to update?")
                print("1. Name")
                print("2. Age")
                print("3. Address")
                print("4. Marks")
                print("5. Update All Fields")
                try:
                    choice = int(input("Enter your choice: "))

                    if choice == 1:
                        student.name = input("Enter new name: ")
                    elif choice == 2:
                        student.age = int(input("Enter new age: "))
                    elif choice == 3:
                        student.address = input("Enter new address: ")
                    elif choice == 4:
                        student.marks = int(input("Enter new marks: "))
                    elif choice == 5:
                        student.name = input("Enter new name: ")
                        student.age = int(input("Enter new age: "))
                        student.address = input("Enter new address: ")
                        student.marks = int(input("Enter new marks: "))
                    else:
                        print("Invalid choice! No updates made.")
                    print("Student successfully updated.")
                except ValueError:
                    print("Invalid input! Please enter valid data types.")
                break
        if not found:
            print(f"No student found with the name '{name}'.")

    def print_student(self, student):
        print(f"Name: {student.name}")
        print(f"Age: {student.age}")
        print(f"Address: {student.address}")
        print(f"Marks: {student.marks}")
        print("-----------------------------")


print("Welcome to the Student Management System")
system = StudentManagementSystem()

while True:
    print("1. Add Student")
    print("2. Delete Student")
    print("3. Update Student")
    print("4. View Students")
    print("5. Exit the System")

    try:
        choice = int(input("Enter your choice: "))
        if choice == 1:
            system.add_student()
        elif choice == 2:
            system.delete_student()
        elif choice == 3:
            system.update_student()
        elif choice == 4:
            system.view_students()
        elif choice == 5:
            print("Exiting the system. Goodbye!")
            break
        else:
            print("Invalid choice! Please enter a number between 1 and 5.")
    except ValueError:
        print("Invalid input! Please enter a valid number.")
