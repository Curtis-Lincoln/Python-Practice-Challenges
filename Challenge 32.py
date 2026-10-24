#Curtis Lincoln
#Challenge 32

def Fahrenheit_Centigrade(Temperature):
    if Temperature[0] == "-":
        Temperature = Temperature.replace("-", "")
        if Temperature.replace(".","").isnumeric():
            Centigrade = ((5/9) * (float(Temperature) - 32)) * -1
            return Centigrade

        else:
            return -999
    else:
        if Temperature.replace(".","").isnumeric():
            Centigrade = (5/9) * (float(Temperature) - 32)
            return Centigrade

        else:
            return -999
    

def Centigrade_Fahrenheit(Temperature):
    if Temperature[0] == "-":
        Temperature = Temperature.replace("-","")
        if Temperature.replace(".","").isnumeric():
            Fahrenheit = ((float(Temperature) * 9/5) + 32) * -1
            return Fahrenheit
        else:
            return -999

    else:
        if Temperature.replace(".","").isnumeric():
            Fahrenheit = ((float(Temperature) * 9/5) + 32)
            return Fahrenheit
        else:
            return -999
        


