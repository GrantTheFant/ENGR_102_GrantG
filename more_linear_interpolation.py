# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Grant Gallun
# Section:      472
# Assignment:   THE ASSIGNMENT NUMBER (2.10)
# Date:         8/28/23


import math

time1 = 12
time2 = 85
distancex1 = 8
distancex2 =-5
distancey1 = 6
distancey2 = 30
distancez1 = 7
distancez2 = 9
speedx = (distancex2 - distancex1)/(time2 - time1)
speedy = (distancey2 - distancey1)/(time2 - time1)
speedz = (distancez2 - distancez1)/(time2 - time1)
counter=1

def interpolate(desiredtime):
 global counter
 distancex = (desiredtime-time1)*speedx+distancex1#(distancex1-speedx*time1)+speedx*desiredtime
 distancey = (desiredtime-time1)*speedy+distancey1
 distancez = (desiredtime-time1)*speedz+distancez1
 print("At time", desiredtime,"seconds:")
 print("x",end='')
 print(counter,"=",distancex, "m\ny",end='')
 print(f'2 + 2 ={counter}')
 print(counter,"=",distancey ,"m\nz",end='')
 print(counter, "=", distancez , "m")
 if counter<5:
  print("-----------------------")
 counter+=1


interpolate(30.0)
interpolate(37.5)
interpolate(45.0)
interpolate(52.5)
interpolate(60.0)

#hehe






