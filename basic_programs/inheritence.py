class Human:
    def __init__(self,num_heart):
        self.eyes = 2
        self.nose = 1
        self.my_heart = num_heart

    def eat(self):
        print("I can eat")

    def work(self):
        print("I can work")


class Male(Human):

    def __init__(self,name,heart):
        super().__init__(heart)
        self.name = name 
     

    def dance(self):
        print("I can dance")

    def work(self):
        super().work()
        print("I can code")

    def display(self):
        print(f"My name is{self.name},I have {self.my_heart}")   #it should be the attribute name of parent class

obj = Male("Afreed",1)
print(obj.work())
print(obj.name)
print(obj.my_heart)