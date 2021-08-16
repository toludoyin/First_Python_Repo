#OBJECT ORIENTED PROGRAM
class product:

    def __init__(self,name,age):
        self.name = name
        self.age = age

    def ProductName(self):
            print(f"My name is {self.name})

    def AgeNumber(self):
                print(f"I am {self.age} years old" )

p = product("Biodun","22")
p.AgeNumber()
p.ProductName()

