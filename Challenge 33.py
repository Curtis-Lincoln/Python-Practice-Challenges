#Curtis Lincoln
#Challenge 33

Number = input("Type in a number: ")
Palindrome = False

while not Palindrome:
    
    if Number[::-1] == Number:
        print(Number)
        Palindrome = True

    else:
        print(Number)
        Number = str(int(Number) + int(Number[::-1]))
           








            
        
    
    
