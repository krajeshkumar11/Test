# My first program
class Hello: # class Hello
    def __init__(self, message):
        self.message = message

    def printtext(self): # To print to console
        print("hello world ", self.message)

HW = Hello("Rajesh")
HW.printtext()
