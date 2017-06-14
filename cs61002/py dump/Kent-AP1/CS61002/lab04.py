'''
Created on 09-Jul-2016

@author: Lokeshwar
'''
# CS61002: Algorithms and Programming 1 
# Name:Lokeshwar Reddy Kasarla
# Date:07-09-2016
# Lab04.py

#Pyhton Module for graphics and math calculations
from turtle import *
from math import sin, sqrt, radians


##### Template for assignments. Duplicate for appropriate number of exercises. ######

print "********** Exercise 4**********"
import turtle
#creating a custom turtle object
lokeshwar = turtle.Turtle()
#setting the speed of turtle to 100
lokeshwar.speed(100)
#drawing a rectangle code with given arguments
def draw_rectangle(length,height,color):
    lokeshwar.color(color)
    lokeshwar.begin_fill()
    lokeshwar.forward(length)
    lokeshwar.rt(90)
    lokeshwar.forward(height)
    lokeshwar.rt(90)
    lokeshwar.fd(length)
    lokeshwar.rt(90)
    lokeshwar.fd(height)
    lokeshwar.rt(90)
    lokeshwar.end_fill()
#function to draw a star with given size
def draw_star(size,color):
    R = (size)/(2*sin(radians(72)))
    A = (2*size)/(3+sqrt(5))
    lokeshwar.color(color)
    lokeshwar.begin_fill()
    lokeshwar.penup()
    lokeshwar.lt(18)
    lokeshwar.penup()
    lokeshwar.fd(R)
    lokeshwar.pendown()
    lokeshwar.lt(162)
    lokeshwar.fd(A)
    lokeshwar.rt(72)
    lokeshwar.fd(A)
    lokeshwar.lt(144)
    lokeshwar.fd(A)
    lokeshwar.rt(72)
    lokeshwar.fd(A)
    lokeshwar.lt(144)
    lokeshwar.fd(A)
    lokeshwar.rt(72)
    lokeshwar.fd(A)
    lokeshwar.lt(144)
    lokeshwar.fd(A)
    lokeshwar.rt(72)
    lokeshwar.fd(A)
    lokeshwar.lt(144)
    lokeshwar.fd(A)
    lokeshwar.rt(72)
    lokeshwar.fd(A)
    lokeshwar.penup()
    lokeshwar.lt(162)
    lokeshwar.fd(R)
    lokeshwar.lt(162)
    lokeshwar.end_fill()

#get color to send proportions of flag colors                
def get_color(color):
    if(color == "red"):
        r=0.698
        g=0.0
        b=0.023
    elif(color =="blue"):
        r=0.234
        g=0.233
        b=0.430
    else:
        r=1
        g=1
        b=1
    return r,g,b

#draw flag to call all the above functions and make the American flag
def draw_flag(height):
    draw_rectangle(height*1.90,height,get_color("red"))
    for flag_stripe in range (13):
        if(flag_stripe%2==0):
            color = get_color("red")
        else:
            color = get_color("white")
        draw_rectangle(height*1.9,height/13 ,color)
        lokeshwar.rt(90)
        lokeshwar.fd(height/13.0)
        lokeshwar.lt(90)
    lokeshwar.penup()
    lokeshwar.setposition(-250, 250)
    lokeshwar.pendown()
    draw_rectangle((height*0.76), ((height * 7) / 13.0), get_color("blue"))
    lokX = 0.0633*height
    lokY = 0.0538*height
    lokeshwar.penup()
    lokeshwar.fd(lokX)
    lokeshwar.rt(90)
    lokeshwar.fd(lokY)
    lokeshwar.lt(90)
    lokeshwar.pendown()
    #calling 5 rows of 6 stars
    for rows in range(5):    
        draw_sixStarsRow(height)
        lokeshwar.penup()
        lokeshwar.bk(lokX*12)
        lokeshwar.rt(90)
        lokeshwar.fd(lokY*2)
        lokeshwar.lt(90)
        lokeshwar.pendown()
    
    lokX = 0.0633*height*2
    lokY = 0.0538*height*2
    lokeshwar.penup()
    lokeshwar.setposition(-250,250)
    lokeshwar.fd(lokX)
    lokeshwar.rt(90)
    lokeshwar.fd(lokY)
    lokeshwar.lt(90)
    lokeshwar.pendown()
    
    #calling 4 rows of 5 stars
    for rows in range(4):
        draw_fiveStarsRow(height)
        lokeshwar.penup()
        lokeshwar.bk(lokX*5)
        lokeshwar.rt(90)
        lokeshwar.fd(lokY)
        lokeshwar.lt(90)
        lokeshwar.pendown()    
    
#function to write a five stars
def draw_fiveStarsRow(height):
    
    for star in range(5):
        draw_star(10,get_color("white"))
        lokeshwar.penup()
        lokeshwar.fd(0.0633*height*2)
        lokeshwar.pendown()
        
#function to write a six stars
def draw_sixStarsRow(height):
    
    for star in range(6):
        draw_star(10,get_color("white"))
        lokeshwar.penup()
        lokeshwar.fd(0.0633*height*2)
        lokeshwar.pendown()
        
lokeshwar.penup()
lokeshwar.setposition(-250,250)
lokeshwar.pendown()

#calling draw method to draw flag
draw_flag(300.0)        

lokeshwar.penup()
lokeshwar.setposition(-250,250)
lokeshwar.pendown()

#exiting the program
#turtle.exitonclick()

