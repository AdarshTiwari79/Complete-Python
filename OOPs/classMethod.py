# class method are used to access and modify the class properties.
# Now here we can confuse ourself while thinking about three different methods which are static method, instance method and class method
# So when we are trying to deal with instance variables then we use instance method. Static for when we don't want any modification within class or instance attributes.

class Student:
    name = "Adarsh Tiwari"

    @staticmethod
    def changeName(name):
        name = name # create a new variable and assign value to that instead of changing
        print(name)

    # instance method 
    def changeN(self, name):
        self.name = name # change the instance variable instead of class variable 
        print(name)

    @classmethod
    def changeName1(cls, name):
        cls.name = name # change the class variable
        print(name)

s = Student()
s.changeName('Ganesh Tiwari')
print(Student.name)

s.changeN("Saurav Tiwari")                                          
print(Student.name)                                         

s.changeName1("Brahmdev Tiwari")                                           
print(Student.name)