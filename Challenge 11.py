#Curtis Lincoln
#Challenge 11

import string

Valid = False
Alphabet = list(string.ascii_uppercase)

while Valid == False:

    try:

        Number = int(input("Type in a number between 1 and 26 inclusive: "))

        if Number >= 1 and Number <= 26:
            print(Alphabet[Number - 1])
            print(ord(Alphabet[Number - 1]))
            Valid = True

        else:
            print("You did not type in an integer between 1 and 26.")

    except:
            print("You did not type in an integer between 1 and 26.")

            

   
