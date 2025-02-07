class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def get_details(self):
        return f"Employee Name: {self.name}, Salary: {self.salary} INR"

class FullTimeEmployee(Employee):
    def __init__(self, name, salary, benefits):
        super().__init__(name, salary)
        self.benefits = benefits

    def get_details(self):
        return f"{super().get_details()}, Benefits: {self.benefits}"

class PartTimeEmployee(Employee):
    def __init__(self, name, salary, hours):
        super().__init__(name, salary)
        self.hours = hours

    def get_details(self):
        return f"{super().get_details()}, Working Hours: {self.hours} hours/week"

# Inheritance in action
full_time = FullTimeEmployee("John Doe", 50000, "Health Insurance")
part_time = PartTimeEmployee("Jane Smith", 20000, 20)

print(full_time.get_details())
print(part_time.get_details())
