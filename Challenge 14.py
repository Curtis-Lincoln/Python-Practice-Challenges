#Curtis Lincoln
#Challenge 14

def Grid(Grid_Size):

    if Grid_Size >= 3 and Grid_Size <= 10:

        for x in range(Grid_Size):
            print("----" * (Grid_Size))
            print("|  |" * (Grid_Size))
            print("|  |" * (Grid_Size))


        print("----" * (Grid_Size))
        return True

    else:
        return False
    
            


            

            



   
