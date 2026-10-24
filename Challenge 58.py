#Curtis Lincoln
#Challenge 58

Dictionary = {}
Name = ""
while Name != "STOP":
    Name = input("Type in your name: Type STOP to end ")
    if Name != "STOP":
        Score = input("Type in your score: ")
        Dictionary.update({Name: Score})
    else:
        Lookup_Name = input("What name do you want to look up: ")
        if Lookup_Name in Dictionary.keys():
            if Dictionary[Lookup_Name] == "":
                print("Person has no score.")
            else:
                print(Lookup_Name ,Dictionary[Lookup_Name])
        else:
            print("Person not in dictionary.")
        
        
    
