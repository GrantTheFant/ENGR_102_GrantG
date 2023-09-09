# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Grant Gallun
# Section:      472
# Assignment:   THE ASSIGNMENT NUMBER (e.g. Lab 1b-2)
# Date:         //

import math

x=float(input("Please enter the side length: "))

def triangle():
    #
    area=math.sqrt((math.pow(x,2)-math.pow(x/2,2)))*x/2
    print(f"A triangle with side {x:.2f} has area {area:.3f}")

def square():
    #
    area=x*x
    print(f"A square with side {x:.2f} has area {area:.3f}")

def pentagon():
    
    area=.5*x*x*((5.0)/(2*math.tan(36*math.pi/180)))
    print(f"A pentagon with side {x:.2f} has area {area:.3f}")

def dodecagon():
    #Honestly no clue why this formula is what it is would like to know
    area=(3)*(2+math.sqrt(3))*math.pow(x,2)
    print(f"A dodecagon with side {x:.2f} has area {area:.3f}")


triangle()
square()
pentagon()
dodecagon()