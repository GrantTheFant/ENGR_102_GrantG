# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Grant Gallun
# Section:      472
# Assignment:   THE ASSIGNMENT NUMBER (6.15)
# Date:         9/25/23


from math import *

juggle = int(input("Enter a positive integer:"))
i = 0
print(f"The Juggler sequence starting at {juggle} is:")
while juggle != 1:
    print(f"{juggle:.0f},", end=" ")
    if juggle % 2 == 1:
        # print(juggle)
        juggle = (pow(juggle, 3 / 2)) // 1
    elif juggle % 2 == 0:
        # print(juggle)
        juggle = (pow(juggle, 1 / 2)) // 1
    i += 1
print(f"{juggle:.0f}")
print(f"It took {i} iterations to reach 1")
