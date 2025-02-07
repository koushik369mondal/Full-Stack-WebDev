"""

Student Management System
==========================

1. Add Student
2. View Student -> All and One
3. Update Student
4. Delete Student
5. Exit

"""


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
        name = input("Enter name: ")
        age = int(input("Enter age: "))
        address = input("Enter Address:")
        marks = int(input("Enter Marks: "))

        student = Student(name, age, address, marks)
        self.students.append(student)
        print("Student Successfully Added")
        return student

    def view_students(self):
        if len(self.students) == 0:
            print("No students found")
        else:
            view_type = input("All Students or One Student? (all/one): ")
            if view_type == "all":
                for student in self.students:
                    print(
                        f"Name: {student.name}\n Age: {student.age} \n Address: {student.address} \n Marks: {student.marks}"
                    )
            if view_type == "one":
                name = input("Enter the name of the student you want to see: ")
                for student in self.students:
                    if student.name == name:
                        print(
                            f"Name: {student.name}\n Age: {student.age} \n Address: {student.address} \n Marks: {student.marks}"
                        )

    def delete_student(self):
        name = input("Enter the student you want to delete: ")
        for student in self.students:
            if student.name == name:
                self.students.remove(student)
        print("Student Successfully Deleted")
        return self.students

    def update_student(self):
        name = input("Enter the student you want to update: ")
        for student in self.students:
            if student.name == name:
                student.name = input("Enter name: ")
                student.age = int(input("Enter age: "))
                student.address = input("Enter Address:")
                student.marks = int(input("Enter Marks: "))
                print("Student Successfully Updated")
                return student
        print("Student not found")


print("Welcome to Student Management System")
system = StudentManagementSystem()

while True:
    print("1. Add Student")
    print("2. Delete Student")
    print("3. Update Student")
    print("4. View Student")
    print("5. Exit The System")

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
        break
    else:
        print("Invalid Choice")
