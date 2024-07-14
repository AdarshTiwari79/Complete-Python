# super() : used to access any parent class method (including constructor) in child class

class Parent:
    def __init__(self, pname):
        self.pname = pname

    def pmeth(self):
        print("parent method")

class Child(Parent):
    def __init__(self, cname, pname):
        self.cname = cname
        super().__init__(pname)
       

obj = Child("child","parent")
print(obj.pname)

