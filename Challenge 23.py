#Curtis Lincoln
#Challenge 23

import string

def No_Punctuation(Sentence):
    return Sentence.translate(str.maketrans('','', string.punctuation)).upper()



