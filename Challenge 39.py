#Curtis Lincoln
#Challenge 39

def Narcistic_Number(Number):
    Valid = False
    while not Valid:
        if Number > 0 and type(Number) is int:
            Power = int(len(str(Number)))
            Number_List = list(str(Number))
            Number_List = list(map(int, Number_List))
            Total = 0

            for Digit in range(len(str(Number))):
                Total = Total + Number_List[Digit]**Power

            if Total == Number:
                return True
            else:
                return False
        else:
            print("The number you typed was not a positive integer.")
            Number = int(input("Type in a positve integer: "))
