# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Grant Gallun
# Section:      472
# Assignment:   THE ASSIGNMENT NUMBER (4.16)
# Date:         9/8/23



number1=(float(input("Enter number 1:")))
number2=(float(input("Enter number 2:")))
number3=(float(input("Enter number 3:")))

if(number1>=number2 and (number1>=number3)):
    print("The largest number is",number1)
elif(number2>=number1 and (number2>=number3)):
    print("The largest number is",number2)
elif(number3>=number1 and (number3>=number2)):
    print("The largest number is",number3)
else:
    print("error")
#style comment!