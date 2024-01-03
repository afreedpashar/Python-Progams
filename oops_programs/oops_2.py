class Student:
    def __init__(self,name,roll,marks):
        self.name = name 
        self.roll = roll
        self.marks = marks
    
    def talk(self):
        print("my name is: ",self.name)
        print("my roll number is",self.roll)
        print("my marks are ",self.marks)

s1 = Student("afreed",101,90)
s2 = Student("rehman",100,80)
print(s1.name)
print(s1.roll)

# print(s.marks)
print(s1.talk())
print(s2.talk())

