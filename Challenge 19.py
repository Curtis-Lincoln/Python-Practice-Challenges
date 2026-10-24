#Curtis Lincoln
#Challenge 19

def isfloat(Number):

    if Number.replace(".","").isnumeric():
        return True
    else:
        return False

#Extension 1
def Float_Conversion(Number):
    Place_Value = 0
    Index = -1
    Number_Strip = Number.replace("-","")
    Number_Strip = Number_Strip.replace(".","")

    if Number_Strip.isnumeric():
        if "." in Number:
            if Number[0] == "-":
                Number = Number.replace("-","")
                while Number:
                    if Number[Index] == ".":
                        Number = Number.replace(".","")
                        Number_Converted = (int(Number) / 10**Place_Value) * -1.0
                        return True, Number_Converted

                    else:
                        Place_Value = Place_Value + 1
                        Index = Index - 1

            else:
                while Number:
                    if Number[Index] == ".":
                        Number = Number.replace(".","")
                        Number_Converted = (int(Number) / 10**Place_Value) * 1.0
                        return True, Number_Converted

                    else:
                        Place_Value = Place_Value + 1
                        Index = Index - 1
        else:
            Number_Converted = int(Number) * 1.0
            return True, Number_Converted
 
    else:
        return False
                

    






