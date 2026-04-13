# Create class College
class College:
    college_name = "Sahyadri College"

    def __init__(self, student_name, branch):
        self.student_name = student_name
        self.branch = branch

    def display(self):
        print("College:", College.college_name)
        print("Student:", self.student_name)
        print("Branch:", self.branch)


c1 = College("ABC", "CSE")
c2 = College("XYZ", "ECE")

c1.display()
c2.display()
