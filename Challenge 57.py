#Curtis Lincoln
#Challenge 57

def Route_Optimiser(Directions):
    Index = 1
    New_List = []
    for _ in range(len(Directions)+1):
        if len(Directions) > 1:
            if Directions[Index] == "N" and Directions[Index-1] == "S":
                Directions = list(New_List) + Directions[Index+1:]
                New_List = []
                Index = 1
            elif Directions[Index] == "S" and Directions[Index-1] == "N":
                Directions = list(New_List) + Directions[Index+1:]
                New_List = []
                Index = 1
            elif Directions[Index] == "E" and Directions[Index-1] == "W":
                Directions = list(New_List) + Directions[Index+1:]
                New_List = []
                Index = 1
            elif Directions[Index] == "W" and Directions[Index-1] == "E":
                Directions = list(New_List) + Directions[Index+1:]
                New_List = []
                Index = 1
            else:
                New_List = list(New_List) + list(Directions[Index-1])
                Index += 1
            

            if Index > len(Directions)-1:
                Index = 1

    return Directions

def Ten_Minute_Walk(Route):
    Time = len(Route)
    Route = Route_Optimiser(Route)
    if Time == 10 and Route == []:
        return True
    else:
        return False

#Extension
def Custom_Time_Walk(Route, Target_Time):
    Time = len(Route)
    Route = Route_Optimiser(Route)
    if Time == Target_Time and Route == []:
        return True
    else:
        return False
    
