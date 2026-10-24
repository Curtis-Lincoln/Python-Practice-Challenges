#Curtis Lincoln
#Challenge 34

def Beautiful_Number(Number):
    Number = str(Number)
    for Digit in range(1, len(Number)):
        Current = int(Number[:Digit])
        Remaining = Number[Digit:]

        while Remaining.startswith(str(Current + 1)):
            Current = Current + 1
            Remaining = Remaining[len(str(Current)):]

        if Remaining == '':
            return True

    return False
        
            
    
