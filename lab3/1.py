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
string_obj.getString()
string_obj.printString()

