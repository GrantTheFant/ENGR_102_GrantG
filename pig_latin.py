# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Grant Gallun
# Section:      472
# Assignment:   THE ASSIGNMENT NUMBER (e.g. Lab 1b-2)
# Date:         9/30/23


pig_Latin = input("Enter word(s) to convert to Pig Latin:")

pig_Latin = pig_Latin.split()


def split_word(word):
    listword = [char for char in word]
    return listword


def pig_latin(word):
    # If a word starts with a vowel, add “yay” on to the end of the word
    # Example: “engineering” becomes “engineeringyay”
    # Note: treat “y” as a vowel for this assignment
    if (
        word[0] == "a"
        or word[0] == "e"
        or word[0] == "i"
        or word[0] == "o"
        or word[0] == "u"
        or word[0] == "y"
    ):
        return "".join(word) + "yay"
    else:
        # If a word starts with a consonant (or cluster of consonants that form one sound), move the
        # consonant(s) to the end of the word, and add “ay” to the end
        count = 0
        while (
            word[0] != "a"
            and word[0] != "e"
            and word[0] != "i"
            and word[0] != "o"
            and word[0] != "u"
            and word[0] != "y"
        ):
            word.append(word[0])
            word.remove(word[0])
    return "".join(word) + "ay"


print('In Pig Latin, "{}" is:'.format(" ".join(pig_Latin)), end=" ")
for word in pig_Latin:
    print(pig_latin(split_word(word)), end=" ")


# Example output (using input howdy aggies whoop):
# Enter word(s) to convert to Pig Latin: howdy aggies whoop
# In Pig Latin, "howdy aggies whoop" is: owdyhay aggiesyay oopwhay
