# Conceptual implementation in Python
# Private attribute & methods are meant to be used only within the class and are not 
# accessible from outside the class.

class Private:
    __name = "Anonymus" # any attribute or method will treated as private when it starts with two _ sign

    def __private(self):
        print("private method accessible only within class")
    
    def meth(self):
        self.__private()
        print(self.__name)

p = Private()
p.meth()
p.__private() # provide error