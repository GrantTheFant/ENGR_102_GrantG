# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Grant Gallun
# Section:      472
# Assignment:   THE ASSIGNMENT NUMBER (7.26)
# Date:         9/30/23

# Use the following letter to number conversions in your program: a > 4, e > 3, o > 0, s > 5, t > 7

leet_speak = input("Enter some text:")
leet_speaklist = list(leet_speak)
code = {}
numbers = ["4", "3", "5", "0", "7"]
letters = ["a", "e", "s", "o", "t"]
for i in range(len(numbers)):
    code[letters[i]] = numbers[i]

for i in range(len(leet_speaklist)):
    if leet_speaklist[i] in code:
        leet_speaklist[i] = code.get(leet_speaklist[i])

print(f'In leet speak, "{leet_speak}" is:')
print("".join(leet_speaklist))
