#Curtis Lincoln
#Challenge 27

def Left_Padding(Sentence, Length):
    if len(Sentence) < Length:
        return Sentence.rjust(Length)

    elif len(Sentence) > Length:
        return Sentence[Length-1:]
    
    else:
        return Sentence
        
        
