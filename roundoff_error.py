# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Grant Gallun
# Section:      472
# Assignment:   THE ASSIGNMENT NUMBER (4.17)
# Date:         9/9/23


############ Part A ############
a=1/7
print(f'a = {a}')
b=a*7
print(f'b = a * 7 = {b}')
#yep
c=2*a
d=5*a
f=c+d

print(f'f = 2 * a + 5 * a = {f}')
#nope
from math import sqrt
x = sqrt(1/3)
print(f'x = {x}')
y=x*x*3
print(f'y = x * x * 3 = {y}')
z=x*3*x
print(f'z = x * 3 * x = {z}')
# one is 1.0 other is .9 repeating
############ Part B ############
TOL=1e-10
# check if b and f are equal within specified tolerance 
if abs(b-f)<TOL:
    print(f'b and f are equal within tolerance of {TOL}')
else:
    print(f'b and f are NOT equal within tolerance of {TOL}')

if abs(y-z)<TOL:
    print(f'y and z are equal within tolerance of {TOL}')
else:
    print(f'y and z are NOT equal within tolerance of {TOL}')
############ Part C ############
m=.1
print(f"m = {m}")
n=3*m
print(f'n = 3 * m = 0.3 {n==0.3}')
p = 7*m
print(f'p = 7 * m = 0.7 {p==0.7}')
q= n + p
print(f'q = n + p = 1 {q==1}')

    
