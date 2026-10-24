#Curtis Lincoln
#Challenge 20
def Camel_Case(Sentence):
    Index = -1

    for _ in range(len(Sentence)):
        if Sentence[Index].isupper():
            Sentence = Sentence[:Index] + " " + Sentence[Index:]
            Index = Index - 1

        else:
            Index = Index - 1

    return Sentence

