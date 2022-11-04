class Rectangle:
    def __init__(self):
        self.l, self.b = list(map(int,input().split(' ')))
    def getArea(self):
        print(self.l * self.b)
        
    # Write your code here.
r = Rectangle()
r.getArea()
quit()
