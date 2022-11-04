from os import *
from sys import *
from collections import *
import math

class Fraction:
    
    def __init__(self,n, d):
        self.n = n
        self.d = d
    def sim(self):
        g = math.gcd(self.n, self.d)
        return (int(self.n/g), int(self.d/g))
    def frac(self, x, y):
        self.x = x
        self.y = y
        g = math.gcd(self.x, self.y)
        return (int(self.x/g), int(self.y/g))
    def add(self, a, b):
        self.a = a
        self.b = b
        if self.d == self.b:
            self.n, self.d = (self.n+self.a), self.b
            return (self.n, self.d)
        else:
            self.n, self.d = self.frac((self.n*self.b)+(self.d*self.a), (self.d*self.b))
            return  (self.n, self.d)
    
    def mul(self, a,b):
        self.a = a
        self.b = b
        self.n, self.d =  self.frac(self.n*self.a, self.b*self.d)
        return (self.n, self.d)
    

    #Driver code goes here.
n,d = list(map(int, input().split(' ')))
i = int(input())

F = Fraction(n,d)
while i > 0:
    t, a, b = list(map(int, input().split(' ')))
    if t == 1:
        r1,e1 = F.add(a,b)
        print("{}/{}".format(r1,e1))
    elif t == 2:
        r2,e2 = F.mul(a,b)
        print("{}/{}".format(r2,e2))
    elif t == 3:
        r3,e3 = F.sim()
        print("{}/{}".format(r3,e3))
    else:
        print('Error Code')
    i -= 1
