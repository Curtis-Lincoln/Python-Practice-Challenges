
#Curtis Lincoln
#Challenge 16

def Split(Sentence):

    Word = ''
    Sentence_List = []

    for Char in Sentence:

        if Char == " ":
            Sentence_List.append(Word)
            Word = ''

        else:
            Word = Word + Char
            
    Sentence_List.append(Word)

    return Sentence_List


        
        
