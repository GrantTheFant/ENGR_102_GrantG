from math import *
day = int(input('Please enter a positive value for day: '))

if(day<11):
    gadget=10*day
else:
    gadget=int(.5*(pow(day,2))+10*day)