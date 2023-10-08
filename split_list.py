# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Grant Gallun
# Section:      472
# Assignment:   THE ASSIGNMENT NUMBER (7.26)
# Date:         9/30/23

numbers = input("Enter numbers:")

numbers = numbers.split(" ")
numbs = list(numbers)
sum = 0
sumleft = 0
sumright = 0
left = []
right = []
for i in range(len(numbs)):
    sum += int(numbs[i])
sum = sum / 2
for i in range(len(numbs)):
    if sumleft != sum:
        left.append(int(numbs[i]))
        sumleft += int(numbs[i])
    else:
        right.append(int(numbs[i]))
        sumright += int(numbs[i])

if sumleft == sumright:
    print("Left:", left)
    print("Right:", right)
    print(f"Both sum to {int(sum)}")
else:
    print("Cannot split evenly")

# I forgot style comment
