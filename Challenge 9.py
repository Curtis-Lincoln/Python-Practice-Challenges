#Curtis Lincoln
#Challenge 9

Valid = False
Total = 0
Num_Values = 0

while not Valid:
    try:
        Number = int(input("Type in a number: "))

        if Number < 0:
            Mean = Total / Num_Values
            print(Mean)
            Valid = True

        else:
            Total = Total + Number
            Num_Values = Num_Values + 1

    except:
        print("That was not a number!")
    
        
