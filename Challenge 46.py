#Curtis Lincoln
#Challenge 46

def Binary_Denary(Binary):
    Power = len(Binary) -1
    Denary = 0

    for Bit in range(len(Binary)):
        Denary = Denary + (int(Binary[Bit])* (2**Power))
        Power = Power - 1

    return Denary

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
    return Binary

def main(Binary_1, Binary_2):
    Denary_1 = Binary_Denary(Binary_1)
    Denary_2 = Binary_Denary(Binary_2)
    Denary = Denary_1 + Denary_2
    Binary = Denary_Binary(Denary)
    return Binary

    
