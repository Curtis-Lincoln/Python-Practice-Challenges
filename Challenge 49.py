#Curtis Lincoln
#Challenge 49

def Progressive_Taxation(Income):
    if Income < 10000:
        return "Tax: £0" 
    elif Income >= 10000 and Income < 50000:
        Tax = (Income-10000)*0.2
        return f"Tax: £{Tax}"
    else:
        Tax = (Income-50000)*0.4
        Tax = Tax + (40000 *0.2)
        return f"Tax: £{Tax}"
            
            
