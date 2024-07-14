# Define a Circle class to create a circle with radius r using the constructor.
# Define an Area() method of the class which calculates the area of the circle.
# Difine a Perimeter() method of the class which allow you to calculate the perimeter of the circle.
"""
class Circle:
    def __init__(self, radius):
        self.radius = radius

    def Create(self):
        print("Circle of radius ",self.radius," is created")

    def Area(self):
        self.area = 3.14 * int(self.radius**2)
        print("Area of the circle with radius ",self.radius, " is ",self.area)

    def Perimeter(self):
        self.perimeter = 2 * 3.14 * int(self.radius)
        print("Perimeter of the circle with radius ",self.radius, " is ", self.perimeter)
    
c1 = Circle(4)
c1.Create()
c1.Area()
c1.Perimeter()
"""

# Define a Employee class with attributes role, department & salary. This class also has a showDetails() method
# Create an Engineer class that inherits properties from Employee & has additional attributes: name & age.

"""
class Employee:
    def __init__(self, role, dept, sal):
        self.role = role
        self.department = dept
        self.salary = sal

    @classmethod
    def showDetails(cls):
        print("Role : ",cls.role," Department : ",cls.department," Salary : ",cls.salary)

class Engineer(Employee):
    def __init__(self, name, age):
        self.name = name
        self.age = age
        super().__init__("Developer","IT","38,000")


# emp1 = Employee("Deginer","IT","30,000")
# emp1.showDetails()

eng1 = Engineer("Adarsh","Saurav")
print(eng1.role)
"""

# Create a class called Order which stores item & its price.
# Use Dunder function __gt__() to convey that:
# order1 > order2 if price of order1>price of order2

class Order:
    def __init__(self, item, price):
        self.item = item
        self.price = price

    def __gt__(self,order2):
        return self.price > order2.price

ord1 = Order("Kurkure", 20)
ord2 = Order ("Samosa", 10)
print(ord2 > ord1)