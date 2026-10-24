#Curtis Lincoln
#Cahllenge 18

def Count_Letter(Sentence, Letter):
    Count = 0
    
    for Char in Sentence:
        if Letter == Char.lower() or Letter == Char.upper():
            Count = Count + 1

    return Count


#Extension 1

def Count_Character(Sentence, Letter):
    Count = 0
    Valid = False

    while not Valid:
        if len(Sentence) >= 20:
            if len(Letter) == 1 and Letter.isalpha():
                    for Char in Sentence:
                        if Letter == Char.lower() or Letter == Char.upper():
                            Count = Count + 1

                    return Count
            else:
                print("Your letter input was not valid.")
                Letter = input("Type in the letter you want counted: ")
        else:
            print("The sentence you typed was not long enogh")
            Sentence = input("Type in a sentence: ") 
    
