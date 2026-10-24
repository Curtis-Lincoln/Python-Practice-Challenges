#Curtis Lincoln
#Challenge 47

xCoordinate_1 = int(input("What is the x-coordinate?: "))
yCoordinate_1 = int(input("What is the Y-coordinate?: "))
print(f"Coordinate_1: {xCoordinate_1,yCoordinate_1}")

xCoordinate_2 = int(input("What is the x-coordinate?: "))
yCoordinate_2 = int(input("What is the Y-coordinate?: "))
print(f"Coordinate_2: {xCoordinate_2,yCoordinate_2}")

Distance = ((xCoordinate_2-xCoordinate_1)**2+(yCoordinate_2-yCoordinate_1)**2)**1/2
print(Distance)

#Extension 1
def Distance():
    End = False
    Coordinates = []
    while not End:
        x_Coordinate = int(input("What is the x-coordinate?: "))
        y_Coordinate = int(input("What is the y-coordinate?: "))
        Coordinate = x_Coordinate,y_Coordinate
        Coordinates.append(Coordinate)
        
        Stop = input("Type YES if you want to continue otheriwse press any key: ")

        if Stop != "YES":
            End = True

    Start_Pointer = 0
    Shortest_Distance = 999999
    Furthest_Distance = -1
    
    for _ in range(int(len(Coordinates))):
        End_Pointer = int(len(Coordinates)-1)
        while Start_Pointer != End_Pointer:
            Distance = 0
            for Digit in Coordinates[Start_Pointer]:
                for Char in Coordinates[End_Pointer]:
                    Distance = Distance + (Char-Digit)**2
            Distance = int(Distance **1/2)
            if Distance < Shortest_Distance:
                Shortest_Distance = Distance
                Shortest = Coordinates[Start_Pointer],Coordinates[End_Pointer]
            elif Distance > Furthest_Distance:
                Furthest_Distance = Distance
                Furthest = Coordinates[Start_Pointer],Coordinates[End_Pointer]

            End_Pointer = End_Pointer - 1

        Start_Pointer = Start_Pointer + 1
            
        


    return f"Shortest: {Shortest},{Shortest_Distance}, Furthest: {Furthest},{Furthest_Distance}"
                
             
                

    
    

    

        


    
