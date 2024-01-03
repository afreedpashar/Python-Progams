class Circle:
    pi = 3.14

    def __init__(self,length,breadth):
        # self.radius = radius
        self.length = length
        self.breadth = breadth
        # self.area = Circle.pi*radius*radius

    def get_circumference(self):
        return 2*Circle.pi*self.radius
    
    def get_area(self):
        area=Circle.pi*self.radius**2
        return area
    
    def get_area_of_rectangle(self):
        area = self.length*self.breadth
        return area
a = int(input("Enter the length value: "))
b = int(input("Enter the breadth value: "))

# circle_1 = Circle(55)
# print(f"circumference of circle is:{circle_1.get_circumference()}")

circle_2 = Circle(a,b)
# print(circle_2.get_circumference())
# print(f"area of circle is:{circle_2.get_area()}")

print(circle_2.get_area_of_rectangle())


