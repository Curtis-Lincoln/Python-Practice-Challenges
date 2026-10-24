#Curtis Lincoln
#Challenge 45

def Hex_Binary(Hex):
    Hex_Values = ["0", "1","2","3","4","5","6","7","8","9","A","B","C","D","E","F"]
    Binary_Values = ["0000","0001","0010","0011","0100","0101","0110","0111","1000","1001","1010","1011","1100","1101","1110","1111"]

    Hex = list(Hex)
    Binary = ''
    Index = 0

    for Digit in Hex:
        for _ in range(len(Hex_Values)):
            if Digit == Hex_Values[Index]:
                Binary_Nibble = Binary_Values[Index]

            else:
                Index = Index + 1
        Binary = Binary + Binary_Nibble

    return Binary
def Binary_Denary(Binary):
    Power = len(Binary) -1
    Denary = 0

    for Bit in range(len(Binary)):
        Denary = Denary + (int(Binary[Bit])* (2**Power))
        Power = Power - 1

    return Denary

def main(Number):
    Binary = Hex_Binary(Number)
    Denary = Binary_Denary(Binary)
    return(Denary)
