# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Grant Gallun
# Section:      472
# Assignment:   THE ASSIGNMENT NUMBER (6.16)
# Date:         9/25/23


# A positive number 𝑛 is a balancing number if the sum of numbers from 1 to (𝑛 − 1) is equal to the sum
# of numbers (𝑛 + 1) to (𝑛 + 𝑟) where 𝑟 is a positive integer.

n = int(input("Enter a value for n:"))
rtemp = n
sum1 = 0
sum2 = 0
i = 0
for i in range(1, int(n)):
    # print(sum1)
    sum1 += i
    # print(sum1)
while sum2 < sum1:
    n += 1
    sum2 += n
# print(sum2,sum1,n)
if sum1 == sum2:
    print(f"{rtemp} is a balancing number with r={n-rtemp}")
if sum1 != sum2:
    print(f"{rtemp} is not a balancing number")
