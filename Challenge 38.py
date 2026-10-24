#Curtis Lincoln
#Challenge 38

Number = int(input("Type in a number: "))
Factors = []

for Digit in range(1,Number+1):
    if Number % Digit == 0:
        Factors.append(Digit)

print(Factors)
            
