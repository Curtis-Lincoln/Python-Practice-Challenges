#Curtis Lincoln
#Challenge 43

def Denary_Binary(Denary):
    Binary = ''
    Count = Denary
    Power = 0

    while Count > 1:
        Count = Count/2
        Power = Power + 1

    Power_1 = Power
    while Denary > 0:
        if Denary >= 2**Power:
            Denary = Denary - 2**Power
            Power = Power - 1
            Binary = Binary + "1" 
        else:
            Power = Power - 1
            Binary = Binary + "0"

    while len(Binary) != Power_1+1:
            Binary = Binary + "0"
    while len(Binary)%4 != 0:
        Binary = "0" + Binary
    return(Binary)


        
    
