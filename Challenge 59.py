#Curtis Lincoln
#Challenge 59

Dictionary = {}
Name = ""
while Name != "STOP":
    Name = input("Type in your name: Type STOP to end ")
    if Name != "STOP":
        Score = input("Type in your score: ")
        Subject = input("Type in the subject: ")
        Dictionary.setdefault(Name, {})[Subject] = Score
    else:
        Lookup_Name = input("What name do you want to look up: ")
        if Lookup_Name in Dictionary.keys():
            print(Lookup_Name, Dictionary[Lookup_Name])
        Lookup_Subject = input("Do you want to look up a subject? y/n: ")
        if Lookup_Subject == "y":
            Lookup_Subject = input("What subject do you want to look up: ")
            for keys,values in Dictionary.items():
                for key in values.keys():
                    if key == Lookup_Subject:
                        print(Lookup_Subject, keys, Dictionary[keys][Lookup_Subject])

            
