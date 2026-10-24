#Curtis Lincoln
#Challenge 17

def Palindrome(Sentence):
    if len(Sentence) >= 4:
        if Sentence[::-1].lower() == Sentence.lower():
            return True
        else:
            return False
    else:
        return False 
