# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Grant Gallun
# Section:      472
# Assignment:   THE ASSIGNMENT NUMBER (6.13 Howdy Whoop)
# Date:         9/21/23

x = int(input("Enter an integer:"))
y = int(input("Enter another integer:"))

for i in range(1, 101):
    if i % x == 0 and i % y == 0:
        print("Howdy Whoop")
        continue
    if i % x == 0:
        print("Howdy")
    if i % y == 0:
        print("Whoop")
    if i % x != 0 and i % y != 0:
        print(i)
# really had to include the comment huh
