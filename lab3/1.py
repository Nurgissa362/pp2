# Classes
# 1.

class StringManipulator:
    def __init__(self):
        self.text = ""

    def getString(self):
        self.text = input("Введите строку: ")

    def printString(self):
        print(self.text.upper())


string_obj = StringManipulator()
string_obj.geting()
string_obj.printString()

# 2 - task


class Shape:
    def area(self):
        return 0 

class Square(Shape):
    def __init__(self, length):
        self.length = length

    def area(self):
        return self.length ** 2  


square_obj = Square(5)
print(square_obj.area()) 

#3 - task

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width  

rectangle_obj = Rectangle(4, 6)
print(rectangle_obj.area())  

