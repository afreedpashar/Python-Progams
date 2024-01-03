class Grading:

    totalMarks = 600

    def __init__(self,name,marks):
        self.name = name
        self.marks = int(marks)
        self.percent = self.calculate_percentage()
    
    def display(self):
        print("Hi", self.name)
        print("Your marks are: ",self.marks)
    
    def calculate_percentage(self):
        return (self.marks/Grading.totalMarks)*100
    
    def grade(self):
        if self.percent >= 85:
            print("Dictinction")
        elif self.percent>=65 and self.percent<85:
            print("First class")
        elif self.percent>=35 and self.percent<60:
            print("Second class")
        else:
            print("You failed")

n = int(input("Enter number of students: "))
for i in range(n):
    name = input("Enter your name: ")
    marks = input("Enter your marks: ")
    s = Grading(name,marks)
    s.display()
    s.grade()
    print()