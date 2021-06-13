"""
def isVowel(letter):
    if letter == "a" or letter == "e" or letter == "i" or letter == "o" or letter == "u":
        print("It's a vowel")
    else:
        print("It's not a vowel")
"""


def isVowel(letter):
    vowels = "aeiou"
    if letter in vowels:
        print("It's a vowel")
    else:
        print("It's not a vowel")


isVowel(str(input("Please type a letter:")))
