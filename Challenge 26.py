#Curtis Lincoln
#Challenge 26
import string

def High_Score(Sentence):
    Sentence_List = Sentence.split()
    Count = -1    
    High_Score = 0
    High_Score_Word = ''

    for Word in Sentence.lower().split():
        Score = 0
        Count = Count + 1

        for Char in Word:
            if Char in string.ascii_lowercase:
                Score = Score + (ord(Char) - 96)

        if Score > High_Score:
            High_Score = Score
            High_Score_Word = Sentence_List[Count]

    return f"Word: {High_Score_Word}, Score: {High_Score}"
    
        


                
            
                       
