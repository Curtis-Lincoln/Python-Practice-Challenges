#Curtis Lincoln
#Challenge 36

def Multiples_3_5(Number):
    Valid = False
    Total = 0
    while not Valid:
        if Number > 0 and type(Number) is int:
            for Digit in range(Number):
                if Digit % 3 == 0:
                    Total = Total + Digit
                elif Digit % 5 == 0:
                    Total = Total + Digit

            return Total
        else:
            print("The number you typed was not a positive integer.")
            Number = int(input("Type in a positive integer: "))

