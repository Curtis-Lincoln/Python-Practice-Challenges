#Curtis Lincoln
#Challenge 12

import string
Valid = False
Uppercase_Alphabet = string.ascii_uppercase
Lowercase_Alphabet = string.ascii_lowercase

while Valid == False:

    try:
        Letter = input("Type in a single character which must be a letter: ")

        if Letter in Uppercase_Alphabet or Letter in Lowercase_Alphabet: 
            print(ord(Letter))
            Valid = True

        else:
            print("You did not type in a single character which was a letter!")

    except:
        print("You did not type in a single character which was a letter!")

            

