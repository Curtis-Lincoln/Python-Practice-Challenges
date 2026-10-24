#Curtis Lincoln
#Challenge 35

def Persistent_Number(Number):
    Valid = False
    while not Valid:
        if Number[0].isdigit():
            if Number.__contains__("."):
                print("The number you typed was not a positive integer.")
                Number = input("Type in a positive integer: ")

            else:
                Number_List = list(str(Number))
                Number_List = list(map(int, Number_List))
                Count = 0

                while len(Number_List) > 1:
                    Value = 1
                    for x in range(len(Number_List)):
                        Value = Value * Number_List[x]

                    Number_List = list(str(Value))
                    Number_List = list(map(int, Number_List))
                    Count = Count + 1

                return Count
        else:
            print("The number you typed was not a positive integer.")
            Number = input("Type in a positive integer: ")
            
