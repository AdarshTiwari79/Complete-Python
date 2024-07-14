# @attribute : This decorator is used to treat a function as an attribute.
# this decorator is used when we want a direct change in the property as other properties are modified
"""
class Student:
    def subject(self, phy, chem, maths):
        self.phy = phy
        self.chem = chem
        self.maths = maths
        self.percentage = str((self.phy + self.chem + self.maths)/3)+"%"

s = Student()
s.subject(33, 89, 99)
print(s.phy)
print(s.percentage)

s.phy = 83 # as mark of one subject is modified but there is no change in percentage
print(s.phy)
print(s.percentage)
"""

class Student:
    def subject(self, phy, chem, maths):
        self.phy = phy
        self.chem = chem
        self.maths = maths

    @property
    def percentage(self):
        return str((self.phy + self.chem + self.maths)/3)+"%"

s = Student()
s.subject(33, 89, 99)
print(s.phy)
print(s.percentage)

s.phy = 83 # as mark of one subject is modified direct change in percentage is taken place
print(s.phy)
print(s.percentage)

