#Curtis Lincoln
#Challenge 29

def Center_Padding(Sentence, Length, Character):
    if len(Sentence) < Length:
        return Sentence.center(Length, Character)

    elif len(Sentence) > Length:
        Center_Length = int((len(Sentence) - Length)//2)
        if len(Sentence)%2 == 0:
            if Length%2 == 0:
                Sentence = Sentence[Center_Length:len(Sentence)-Center_Length]

            else:
                Sentence = Sentence[Center_Length+1:len(Sentence)-Center_Length]                            
        else:
            if Length%2 == 0:
                Sentence = Sentence[Center_Length+1:len(Sentence)-Center_Length]

            else:
                Sentence = Sentence[Center_Length:len(Sentence)-Center_Length]

        return Sentence

    else:
        return Sentence



    
