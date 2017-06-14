# CS61002: Algorithms and Programming 1 
# Name: Lokeshwar Reddy Kasarla
# Date: 07/31/2016
# Lab07.py





print "********** Exercise 7**********"

#for using math module
import math

#creating a vector class with given information 
class vector:
    
    #default constructor
    def __init__(self,x,y):
        #assigning the parameters to self variables
        self.x = x
        self.y = y
    
    #__str__ function to return the string for printing
    def __str__(self):
        return "({0},{1})".format(self.x,self.y)
    
    #__add__ to add the vector with sent with vector present in self
    def __add__(self,other):
        x = self.x + other.a
        y = self.y + other.b
        return vector(x,y)
    
    #__sub__ to subtract the vector with sent with vector present in self
    def __sub__(self,other):
        x = self.x + (- other.a )
        y = self.y + (- other.b )
        return vector(x,y)
    
    #__mul__ to multiply the vector with sent with vector present in self
    def __mul__(self,other):
        x = self.x * other.x
        y = self.y * other.x
        return x+y
    
    #to return magnitude of the vector
    def magnitude(self):
        return math.hypot(self.x, self.y)        
    
