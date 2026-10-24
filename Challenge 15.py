#Curtis Lincoln
#Challenge 15

def Grid(Rows = 5, Columns = 5):

    if Rows >= 3 and Rows <= 10:
        if Columns >= 3 and Columns <= 10:
            for x in range(Rows):
                print("----" * (Columns))
                print("|  |" * (Columns))
                print("|  |" * (Columns))

            print("----" * (Columns))
            return True
        else:
            return False
    else:
        return False
    
    
        
            

    
