#Curtis Lincoln
#Challenge 42

def Binary_Denary(Binary):
    Power = len(Binary) -1
    Denary = 0

    for Bit in range(len(Binary)):
        Denary = Denary + (int(Binary[Bit])* (2**Power))
        Power = Power - 1

    return Denary
    
