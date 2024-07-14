# methods are nothing but functions inside a class is termed as methods

class Student:
    cname = "default"
    def __init__(self, fname, lname, age):
        self.fname = fname
        self.lname = lname 
        self.age = age

    def getAge(self):
        return self.age

s1 = Student('Adarsh','Tiwari',23)
print(s1.getAge())
print(s1.cname)