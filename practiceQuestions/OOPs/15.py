# Create student class that takes name & marks of 3 subjects as arguments in constructor.
# Then create a method to print the average.

class Student:
    def __init__(self, sname, marks):
        self.sname = sname
        self.marks = marks

    def avg(self,n1, n2, n3):
        average = (n1 + n2 + n3)/3
        print("The average of numbers is : ", average)

s1 = Student("physics",99)
s2 = Student('chemistry', 83)
s3 = Student('mathematics', 82)

print(s1.sname, end = " ")
print(s1.marks)

print(s2.sname, end = " ")
print(s2.marks)

print(s3.sname, end = " ")
print(s3.marks)

n1 = int(input("Enter num1 : "))
n2 = int(input("Enter num2 : "))
n3 = int(input("Enter num3 : "))

s1.avg(n1, n2, n3)
