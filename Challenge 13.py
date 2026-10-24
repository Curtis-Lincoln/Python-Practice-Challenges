#Curtis Lincoln
#Challenge 13

import string

def Tuple(String):

    List_ABC = "ABC"
    List_123 = "123"

    if len(String) == 2:

        if String[0] in List_ABC and String[1] in List_123:

            for x in range(3):
                if String[0] == List_ABC[x]:
                    Letter_Index = x

                if String[1] == List_123[x]:
                    Number_Index = x

            return Letter_Index, Number_Index

        else:
            return False,
    else:
        return False,

    
       
