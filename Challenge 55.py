#Curtis Lincoln
#Challenge 55

def Duplicate(Word):
    Word = list(Word.upper())
    Valid = False 
    while not Valid:
        Index = 1
        while Index < len(Word):
            if Word[Index] == Word[Index-1]:
                Word = Word[:Index-1] + Word[Index+1:]
                print(Word)
                Index = Index - 1
            Index += 1

        if Word == []:
            Valid = True

        if not Valid:
            Count = 0
            for x in range(1,len(Word)):
                if Word[x] != Word[x-1]:
                    Count += 1
            if Count == len(Word)-1:
                Valid = True
    
