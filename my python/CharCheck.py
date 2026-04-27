#Character Check
#Take a single character input and check if it is a vowel, consonant, digit, or special character.

char=input("Enter a character: ")
if char.isalpha():
        if char.lower() in ['a','e','i','o','u']:
            print("Vowel")
        else:
            print("Consonant")
elif char.isdigit():
    print("Digit")
else:
    print("Special Char")
