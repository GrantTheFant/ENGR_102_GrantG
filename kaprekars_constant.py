# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Grant Gallun
# Section:      472
# Assignment:   THE ASSIGNMENT NUMBER (7.28)
# Date:         10/2/23


# Enter a four-digit integer: 2027
# 2027 > 6993 > 6264 > 4176 > 6174
# 2027 reaches 6174 via Kaprekar's routine in 4 iterations
n = input("Enter a four-digit integer:")

n = list(n)

if len(n) != 4:
    for i in range(4 - len(n)):
        n.insert(0, "0")

if int("".join(n)) > 9999 or int("".join(n)) < 1:
    print("invalid input")
    exit()


def TurntoInt(n):
    for i in range(len(n)):
        n[i] = int(n[i])
    return n


def TurntoStrArray(n):
    for i in range(len(n)):
        n[i] = str(n[i])
    return n


def TurntoArray(sum):
    sum = list(str(sum))
    if len(sum) != 4:
        for i in range(4 - len(sum)):
            sum.insert(0, "0")
    return sum


sum = 0
count = 0
kap = 6174
temp = []
og_no = int("".join(n))
while int("".join(n)) != 6174:
    # for i in range(5):
    print(int("".join(n)), ">", end=" ")
    n = sorted(TurntoInt(n), reverse=True)
    n = TurntoStrArray(n)
    # print(int("".join(n)))
    sum = int("".join(n))
    n.reverse()
    sum = sum - int("".join(n))
    # print(sum)
    n = TurntoArray(sum)
    count += 1
    if int("".join(n)) == 0:
        kap = 0
        break

print(int("".join(n)))

print(f"{og_no} reaches {kap} via Kaprekar's routine in {count} iterations")
