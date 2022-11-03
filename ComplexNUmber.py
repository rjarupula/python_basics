from os import *
from sys import *
from collections import *
from math import *



class ComplexNumbers:
    
    def __init__(self, a,b,c,d):
        self.r1 = a
        self.i1 = b
        self.r2 = c
        self.i2 = d
        
    def plus(self):
        self.p = (self.r1+self.r2)
        self.ip = (self.i1 + self.i2)
        print("{} + i{}".format(self.p, self.ip))
    def multiply(self):
        self.m = ((self.r1 * self.r2)-(self.i1*self.i2))
        self.mi = ((self.r1*self.i2)+(self.r2*self.i1))
        print("{} + i{}".format(self.m, self.mi))

        #create your class here.

a, b = list(map(int, input().split(' ')))
c, d = list(map(int, input().split(' ')))

A = ComplexNumbers(a,b,c,d)
t = input()

if t == '1':
    A.plus()
elif t == '2':
    A.multiply()
else:
    print('Error Choice')
        
    
    
#Driver's code goes here.
