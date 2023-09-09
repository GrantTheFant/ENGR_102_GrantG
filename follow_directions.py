# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Grant Gallun
# Section:      472
# Assignment:   THE ASSIGNMENT NUMBER (Lab 1.13)
# Date:         8/23/23

import math

counter=.1
x=1+counter

def funky():
    global x
    global counter
    print(math.sin((x-1))/(x-1))
    counter=counter/10
    x=1+(counter)
    
print("This shows the evaluation of sin(x - 1)/(x - 1) evaluated close to x = 1")
print("my guess is 1")
funky()
funky()
funky()
funky()
funky()
funky()
funky()
funky()
print("\n mental math checks out but I guess I forgot the decimal")
#NOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO I FORGOT THE COMMENT THERE GOES MY FIRST ATTEMPT 100%
    
    

