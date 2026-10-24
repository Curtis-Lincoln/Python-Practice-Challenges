#Curtis Lincoln
#Challenge 28

def Right_Padding(Sentence, Length, Character):
    if len(Sentence) < Length:
        return Sentence.ljust(Length, Character)
        
    elif len(Sentence) > Length:
        return Sentence[:Length]

    else:
        return Sentence 
