
class Square:
    def __init__(self, l=10):
        self.length = l
    def printArea(self):
        print(self.length*self.length)
        

    # Write init and printArea method here.

l = int(input())
s = Square()
s.printArea()
a = Square(l)
a.printArea()
