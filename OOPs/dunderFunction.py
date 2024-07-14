# dunder functions are used to operator overloading in python 

# In python there is no any arithmetic operator to use on complex numbers.
# So we can overload existing operator with our logic to perform arithmetic operation on complex numbers

class Complex:
    def __init__(self, real, img):
        self.real = real
        self.img = img
    
    def showNumber(self):
        print(self.real, "i +", self.img, "j")

    def __add__(self, n2):
        newReal = self.real + n2.real
        newImg = self.img + n2.img
        return Complex(newReal, newImg)

num1 = Complex(2, 3)
num1.showNumber()

num2 = Complex(3, 8)
num2.showNumber()

num3 = num1 + num2
num3.showNumber()