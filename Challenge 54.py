#Curtis Lincoln
#Challenge 54

def Grades(Score):
    if Score <= 10:
        return "U"
    elif Score <= 25:
        return "E"
    elif Score <= 50:
        return "D"
    elif Score <= 70:
        return "C"
    elif Score <= 85:
        return "B"
    else:
        return "A"
