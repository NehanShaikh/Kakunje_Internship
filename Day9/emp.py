class Employee:
    
    company_name = "Kakunje Software Pvt Ltd"
    
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def display(self):
        print("Company Name:", Employee.company_name)
        print("Employee Name:", self.name)
        print("Salary:", self.salary)


emp1 = Employee("ABC", 50000)
emp2 = Employee("XYZ", 60000)

emp1.display()
emp2.display()
