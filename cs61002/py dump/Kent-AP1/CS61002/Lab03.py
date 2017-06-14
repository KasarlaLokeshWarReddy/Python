
# CS61002: Algorithms and Programming 1 
# Name:Lokeshwar Reddy Kasarla
# Date:07/03/2016
# Lab3.py

# Graphics Programing in Python Using lkasarlas for making random shapes
 

print "********** Exercise 3 **********"

#importing random,  turtle, os, time and stdio modules for random,graphics, input and output functions.

import turtle
import stdio
import random
import os
import time

stdio.writeln("Random shapes in Turtle with two different angles")
stdio.writeln("This Program generates random shapes everytime it is run")
stdio.writeln ("________________________________________________________")

#always true condition
while True:
    #reading raw_input 
    string_input_value = raw_input("Enter number of pairs of lines you want (between 8 and 300) :")
    
    if string_input_value.isdigit():
        #parsing string to interger type
        iterations = int(string_input_value)
        #checking the input is between 8 and 300
        if iterations >= 8 and iterations <= 300 :
            #success exiting the outer while loop
            break
        else:
            #clauses for integers not between 8 and 300
            stdio.writeln("please give an integer between 8 and 300 only as input")
    else:
        
        stdio.writeln("Please enter an integer between 8 and 300 only as input")


angle_1=random.randint(0,360)
angle_2=random.randint(0,360)

#assigning turtle object to lkasarla variable 
lkasarla = turtle.Turtle()
#setting the speed to 0
lkasarla.speed("fastest")

#starting the loop with given input number of times
for lines in range(iterations):    
    #setting a random color
    lkasarla.color((random.random(),random.random(),random.random()))
    #starting the fill and writing the through turtle
    lkasarla.begin_fill()
    lkasarla.pendown()
    #moving right with angle_1
    lkasarla.rt(angle_1)
    #moving back
    lkasarla.bk(200)
    #moving left with angle_2
    lkasarla.lt(angle_2)
    #moving forward
    lkasarla.fd(200)
    #setting pen off and ending the fill area
    lkasarla.penup()
    lkasarla.end_fill() 
    
#pausing the screen for 10 seconds so that we can see the output
time.sleep(10)

#terminating the program
os._exit(1)