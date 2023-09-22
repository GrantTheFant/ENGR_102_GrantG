from math import *

#Ask for input

Number = int(input("Enter a 4-digit integer:"))

Power = int(input("Enter the power:"))

NumSum = 0

#Now we split up the number into two separate numbers

#First we check the leading digit is zero

if (Number//1000>0):

    NumSum+=pow(Number//1000, Power)

#Then The hundreds place

NumSum+=pow(Number%1000//100, Power)


NumSum+=pow(Number%100//10, Power)

NumSum+=pow(Number%10,Power)

print(f"{Number} with given power {Power} is {int(NumSum)}")

if(Number == NumSum):
    print("Number is a PDI")
