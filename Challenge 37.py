#Curtis Lincoln
#Challenge 37

Max_Number = int(input("Type in a number: "))
Not_Prime = []
Prime_Numbers = []

for Digit in range(2, Max_Number+1):
    for Number in range(2,Digit):
        if (Digit%Number) == 0:
            Not_Prime.append(Digit)

for x in range(2, Max_Number):
    if x not in Not_Prime:
        Prime_Numbers.append(x)

print(Prime_Numbers)
        




            
        


        

                    


        
