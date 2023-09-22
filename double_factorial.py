# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Grant Gallun
# Section:      472
# Assignment:   THE ASSIGNMENT NUMBER (6.?)
# Date:         9/21/23


def doublefactorial(n):
    iseven = False
    double_factorial = 1
    if n % 2 == 0:
        iseven = True
    if iseven:
        for i in range(1, n + 1):
            if i % 2 == 0:
                double_factorial *= i
    else:
        for i in range(1, n + 1):
            if i % 2 == 1:
                double_factorial *= i
    return double_factorial


# I forgot again
