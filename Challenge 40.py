#Curtis Lincoln
#Challenge 40

def Binary_Hex(Binary):
    
    Binary_Values = ["0000","0001","0010","0011","0100","0101","0110","0111","1000","1001","1010","1011","1100","1101","1110","1111"]
    Hex_Values = ["0","1","2","3","4","5","6","7","8","9","A","B","C","D","E","F"]
    Hex = ''

    while len(Binary) % 4 != 0:
        Binary = "0" + Binary

    Binary  = " ".join([Binary[Bit:Bit+4] for Bit in range(0, len(Binary), 4)])
    Binary = Binary.split()

    for Nibble in range(len(Binary)):
        for Pointer in range(16):
            if Binary[Nibble] == Binary_Values[Pointer]:
                Hex = Hex + Hex_Values[Pointer]

    return Hex


