# -*- coding: utf-8 -*-
"""
Created on Sun Feb 16 00:15:26 2020

@author: PALAK DHINGRA
"""

import turtle

def createSquare():
    window= turtle.Screen()
    window.bgcolor("red")
    
    brad = turtle.Turtle()
    brad.shape("turtle")
    brad.color("yellow")
    brad.speed(2)
    squareAngle = 0
    while squareAngle < 15:
        squareMovements=0
        brad.right(25)
        while squareMovements < 4:
            brad.forward(100)
            brad.right(90)
            squareMovements = squareMovements + 1
        squareAngle = squareAngle + 1    
     
    angie = turtle.Turtle()
    angie.circle(100)
    angie.color("blue")
    
    trio = turtle.Turtle()
    trio.color("white")
    trioAngle=1
    while trioAngle < 4:
        trio.forward(100)
        trio.right(120)
        trioAngle = trioAngle +1
    
    window.exitonclick()
    
createSquare()

