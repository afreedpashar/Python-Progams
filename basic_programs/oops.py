class Instructor:
    followers = 0
    def __init__(self,name,address,pincode):
        self.name = name
        self.address = address
        self.pincode = pincode
    
    def display(self,subject):
        print(f"hi, I am {self.name}")
        print(f"I live in {self.address}, I teach {subject}")

    def update_followers(self,followers_name):
        self.followers+=1   

instructor_1 = Instructor("Afreed","Chintamani","563125")
print(instructor_1.address)
instructor_1.display("python")
instructor_1.update_followers("Khan")
print(instructor_1.followers)

instructor_2 = Instructor("Nawaz","Bangalore","560068")
instructor_2.display("java")
instructor_2.update_followers("jiya")
print(instructor_2.followers)
