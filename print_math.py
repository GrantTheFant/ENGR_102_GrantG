# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Grant Gallun
# Section:      472
# Assignment:   THE ASSIGNMENT NUMBER (Lab 1.12)
# Date:         8/23/23

import math

#it might be a little excessive for this assignment
#but I'm creating variables for the equations so I promote better organization for myself and for my team in the future

mass = 27
acc = 1.5

force =mass*acc

distance = 0.025
angle = 35*math.pi/180
wave = 2*distance*math.sin(angle)
days = 5
mass2=27
hl=3.8

radon=mass2*math.pow(2,(-days/hl))


moles = 5
vol = .27
temp = 415
const = 8.314

pressure=5*const*temp/(vol)
pressure=pressure/1000
#I multiplied vol by 1k to convert units but that caused the equation to end in the wrong digit
#I also tried rounding the last digit down but realized my mistake before I figured out how

print("Force is", force, "N")
print("Wavelength is", wave, "nm")
print("Radon-222 left is", radon, "g")
print("Pressure is", pressure, "kPa")