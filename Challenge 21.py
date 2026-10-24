#Curtis Lincoln
#Challenge 21

def Camel_Case(Sentence):
    Valid = False
    while not Valid:
        if Sentence.islower():
                
            Sentence = list(Sentence)
            Sentence[0] = Sentence[0].upper()

            for Char in range(len(Sentence)):
                if Sentence[Char] == " ":
                    Sentence[Char+1] = Sentence[Char+1].upper()
                    Sentence[Char] = ""

            return ''.join(Sentence)

        else:
            print("That sentence was not lowercase.")
            Sentence = input("Type in a sentence: ")

