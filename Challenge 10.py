#Curtis Lincoln
#Challenge 10


Valid = False
Min = 99999
Max = 0

while not Valid:

    Number = int(input("Enter a number: "))
    if Number >= 0:
        
        if Number < Min:
            Min = Number
        if Number > Max:
            Max = Number
            
    else:
        if Min == 99999:
            Min = 0
        print(f"The smallest number is {Min}")
        print(f"The largest number is {Max}")
        Valid = True

















        
        

