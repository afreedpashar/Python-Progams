class Employee:

    raise_amount = 1.04 #class variable it can be applied to whole class instance
    no_of_employees = 0
    
    def __init__(self,first,last,pay):
        self.first = first
        self.last = last
        self.payment= pay
        self.email = first + last + '@company.com' 

        Employee.no_of_employees+=1

    def full_name(self):
        return '{} {}'.format(self.first,self.last)
    
    def email_name(self):
        return '{}'.format(self.email)

    def apply_raise(self):
        self.payment = int(self.payment * Employee.raise_amount)  #the self.payment is from __init__ constructor 
    
    @classmethod
    def set_raise_amount(cls,amount):
        cls.raise_amount = amount 
    
    @classmethod
    def from_string(cls,emp_str):
        first,last,payment = emp_str.split('-')
        return cls(first,last,payment)



print(Employee.no_of_employees)

Employee.set_raise_amount(1.08)

emp_1 = Employee("Afreed","Pasha",50000)
emp_2 = Employee("Sara","Khan",60000)
emp_3 = Employee("Shifa","Khan",70000)
emp_str_4 = 'Saleem-Khan-80000'

# first,last,payment = emp_str_4.split('-') #instead of this we will create a class method from_string(cls,emp_str)

new_emp = Employee.from_string(emp_str_4)
print(new_emp.first)
print(new_emp.last)
print(new_emp.payment)

# print(emp_1.full_name())
# print(emp_1.email_name())
# print(emp_3.full_name())

# print(Employee.full_name(emp_1))

# print(emp_1.payment)
# print()
# emp_1.apply_raise()
# print(emp_1.payment)
# print()
# emp_2.apply_raise()
# print(emp_2.payment)

# print(emp_1.__dict__) #we can use __dict__ to get the v=key value pair in dictionary form
# print(Employee.__dict__)
# emp_1.raise_amount=1.06
# emp_1.apply_raise()
# print(emp_1.raise_amount)
# print(emp_1.__dict__)
# print(emp_2.__dict__)

print(Employee.no_of_employees)
print(emp_1.raise_amount)