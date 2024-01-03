# class Employee:
#     def __init__(self,x,y,z):
#         self.name = x
#         self.age = y
#         self.weight = z

#     def display(self):
#         print("The Employee name is {}, his age is {} and his weight is {}".format(self.name,self.age,self.weight))

# e1=Employee("Afreed",25,60)
# e2=Employee("Farhan",21,50)

# e1.display()
# e2.display()

# class Test:
#     def __init__(self):
#         self.a =10
#         self.b = 20
#     def m1(self):
#         self.c=40
#         self.e=69

# o1 = Test()
# o1.m1()
# o1.d=80 #creating instance variable outside the class of a particular object
# print(o1.__dict__)

#to delete the instance variable from the object

# class Delete:
#     def __init__(self):
#         self.a = 10
#         self.b = 20
#         self.c = 30
#         self.d = 40
    
#     def m1(self):
#         del self.a

# obj1 = Delete()
# print(obj1.__dict__)
# obj1.m1()
# print(obj1.__dict__)
# del obj1.c
# print(obj1.__dict__)


#the instav=nce variable deleted from one object will not be deleted from another object
class Delete:
    def __init__(self):
        self.a = 10
        self.b = 20
        self.c = 30
        self.d = 40
    
    def m1(self):
        del self.a

obj1 = Delete()
obj2 = Delete()
print(obj1.__dict__)
print(obj2.__dict__)
obj1.m1()
print(obj1.__dict__)
del obj2.b
print(obj2.__dict__)