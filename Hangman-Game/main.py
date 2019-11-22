import random

words = []
letters = []
word = ""
wrongLetters = 0
correctLetters = 0


def load_data():
    f = open("words.txt", "r")
    for x in f:
        words.append(x)
    f.close()


def print_lines():
    for letter in range(len(word) - 1):
        if any(item.lower() == word[letter].lower() for item in letters):
            print(word[letter], end=" ")
        else:
            print("_", end=" ")


def wait_for_input():
    print(" ")
    letter = ""
    while any(item.lower() == letter.lower() for item in letters) or letter == "" or len(letter) > 1:
        letter = input("Letter: ")
    letters.append(letter)
    if not any(item.lower() == letter.lower() for item in word):
        print("wrong")
        return 1
    return 0


def print_image():
    if wrongLetters == 0:
        print(" ")
        print(" ")
        print(" ")
        print(" ")
        print(" ")
        print(" ")
    elif wrongLetters == 1:
        print(" ")
        print(" ")
        print(" ")
        print(" ")
        print(" | ")
        print(" | ")
    elif wrongLetters == 2:
        print(" ")
        print(" ")
        print(" | ")
        print(" | ")
        print(" | ")
        print(" | ")
    elif wrongLetters == 3:
        print(" ")
        print(" ----------")
        print(" | ")
        print(" | ")
        print(" | ")
        print(" | ")
    elif wrongLetters == 4:
        print(" ")
        print(" ----------")
        print(" |        |")
        print(" | ")
        print(" | ")
        print(" | ")
    elif wrongLetters == 5:
        print(" ")
        print(" ----------")
        print(" |        |")
        print(" |        o")
        print(" | ")
        print(" | ")
    elif wrongLetters == 5:
        print(" ")
        print(" ----------")
        print(" |        |")
        print(" |        o")
        print(" |        |")
        print(" | ")
    elif wrongLetters == 6:
        print(" ")
        print(" ----------")
        print(" |        |")
        print(" |        o")
        print(" |        |")
        print(" |       | |")
    elif wrongLetters == 7:
        print(" ")
        print(" ----------")
        print(" |        |")
        print(" |        o")
        print(" |       -|-")
        print(" |       | |")


load_data()
word = words[random.randrange(0, len(words) - 1)]

while wrongLetters < 7 and correctLetters < len(list(set(word))) - 1:
    print_lines()
    letterVal = wait_for_input()
    if letterVal == 1:
        wrongLetters = wrongLetters + 1
    else:
        correctLetters = correctLetters + 1
    print_image()

print("correct word was: " + word)