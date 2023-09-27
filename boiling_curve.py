# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Grant Gallun
# Section:      472
# Assignment:   THE ASSIGNMENT NUMBER (Lab 5.4)
# Date:         9/24/23



from math import *

# The curve starts out with a linear region for free convection, where boiling has not yet started (points A to B).

x = float(input("Enter the excess temperature:"))

pointx1 = 1.3
pointx2 = 5
pointx3 = 30
pointx4 = 120
pointx5 = 1200
pointy1 = 1000
pointy2 = 7000
pointy3 = 1.5 * 10**6
pointy4 = 2.5 * 10**4
pointy5 = 1.5 * 10**6


def getLine(xzero, x, yzero, y, x2):
    m = log(y / yzero) / log(x / xzero)
    y2 = yzero * pow((x2 / xzero), m)
    return y2


def boil(x):
    if x < pointx1 or x > 1200:
        print("Surface heat flux is not available")
        exit()
    if x >= pointx1 and x <= pointx2:
        return getLine(pointx1, pointx2, pointy1, pointy2, x)
    if x > pointx2 and x <= pointx3:
        return getLine(pointx2, pointx3, pointy2, pointy3, x)
    if x > pointx3 and x <= pointx4:
        return getLine(pointx3, pointx4, pointy3, pointy4, x)
    if x > pointx4 and x <= pointx5:
        return getLine(pointx4, pointx5, pointy4, pointy5, x)


print(f"The surface heat flux is approximately {boil(x):.0f} W/m^2")


# print(pointy5)


# The onset of nucleate boiling (B) starts at 5 °C of excess temperature and continues roughly linearly until the critical heat flux (C) is reached.


# There is a negative roughly linear trend from the critical heat flux down to the Leidenfrost point (D) which is the transition region, followed by an upward nearly linear film region (D to E).


# y=yzero*pow((x/xzero),m)
# m=log(y/yzero)/log(x/xzero)


#
