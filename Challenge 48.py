#Curtis Lincoln
#Challenge 48
import datetime
Valid = False 
while not Valid:
    try:
        Date = input("Type in a date in the form DD/MM/YYYY: ")
        Date = Date.replace("/"," ",2)
        Date = Date.split()
        Date_1 = datetime.datetime(int(Date[2]),int(Date[1]),int(Date[0]))
        Date_1 = Date_1.strftime("%d/%m/%y")
        Valid = True
    except:
        print("Date not valid.")

if int(Date[2]) % 4 == 0 and int(Date[2]) % 100 != 0:
    print("Leap year.")
elif int(Date[2]) % 100 == 0 and int(Date[2]) % 400 == 0:
    print("Leap year.")
else:
    print("Not a leap year")


    
