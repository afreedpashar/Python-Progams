class Human:

    def __init__(self,num_heart):
        # print("Calling init from Human")
        self.eyes=2
        self.nose = 1
        self.myheart = num_heart

    def eat(self):
        print("i can eat")

    def work(self):
        print("I can work")

class Male:

    def __init__(self,name):
        # print("Calling init from Male")
        self.name = name 

    def work(self):
        print("I can code")

    def flirt(self):
        print("I can flirt")

class Boy(Human,Male):

    def __init__(self,name,heart,language):
        Human.__init__(self,heart)
        Male.__init__(self,name)
        self.language = language

    def sleep(self):
        print("I can sleep")

    def work(self):
        print("I can test")  

    def display(self):
        print(f"My name is {self.name},I am learning {self.language} ")

boy1=Boy("Afreed",1,"Python")
print(boy1.language)
boy1.display()
