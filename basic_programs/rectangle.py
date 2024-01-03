class Rectangle:

    def __init__(self,length,breadth):
        self.length = length
        self.breadth = breadth

    def get_area(self):
        area = self.length*self.breadth
        return area

a = int(input("Enter the length of rectangle: "))
b = int(input("Enter the breadth of rectangle: "))

obj1 = Rectangle(a,b)

print(obj1.get_area())
