# Methods that don't use the self parameter (work at the class level)
# Decorators allow us to wrap another function in order to extend the behaviour of the wrapped function, without permanently modifying it

class Student:
    @staticmethod # decorators
    def college():
        print("This is a static method which will work on class level ")

Student.college()