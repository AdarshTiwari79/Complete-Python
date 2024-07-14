# Constructor: All classes have a function called _init_(), which is always executed when the object is being initiated.

# syntax : def __init__(self, param1,...): --> The self parameter is a reference to the current instance of the class, and is used to access variables that belongs to the class.
#               self.name = param1

# Creating class 
"""
class Student:
    def __init__(self, fullname):
        self.name = fullname

s1 = Student("Adarsh")
print(s1.name)
"""
# Class and Instance(Object) Attributes
# Class Attributes : defined as the property of the class and can be accessed via any object of the class
# Instance attributes : defined at the time of the object creation with the help of the parameter of the parameterized constructors

class Employee:
    ename = "Anonymous" # class attribute
    def __init__(self, ename, sal):
        self.ename = ename  # instance attribute
        self.sal = sal

# when class attribute and instance attribute have same name then the preference goes to instance attribute 

#print(Employee.ename)  # We can access class attribute directly without creating object of the class 

e1 = Employee("Saurav",30000)
print(e1.ename)  # Here priority goes to instance variable
print(e1.sal)

