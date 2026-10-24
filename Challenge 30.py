#Curtis Lincoln
#Challenge 30

def Needle_Haystack(Needle, Haystack):
    Haystack = Haystack.split()
    Index = 0
    Position = 0
    SPACE = 1
    for _ in Haystack:
        if Needle == Haystack[Index]:
            while Index > 0:
                Word = Index - 1
                if Word > -1:
                    Position = Position + len(Haystack[Word]) + SPACE
                    Index = Index - 1

            return f"The position of the first letter of the needle in the haystack is at position {Position}"

        else:
            Index = Index + 1

    return -1


    
            
            
            





