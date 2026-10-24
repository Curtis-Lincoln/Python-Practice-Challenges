#Curtis Lincoln
#Challenge 31

import random

Numbers = []

for _ in range(11):
    Numbers.append(random.randint(0,9))

Start_Telephone = ""
for Number in range(5):
    Start_Telephone = Start_Telephone + str(Numbers[Number])

End_Telephone = ""
for Number in range(6):
    End_Telephone = End_Telephone + str(Numbers[Number+5])

print(f"({Start_Telephone}){End_Telephone}")
