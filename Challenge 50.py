#Curtis Lincoln
#Challenge 50

def National_Insurance(Monthly_Income):
    if Monthly_Income < 700:
        return "Tax: £0"
    elif Monthly_Income >= 700 and Monthly_Income < 4000:
        Tax = (Monthly_Income-700) *  0.12
        return f"Tax: £{Tax}"
    else: 
        Tax = (Monthly_Income-4000)*0.02
        Tax = Tax + (3300 * 0.12)
        return f"Tax: £{Tax}"



#Extension 1
def National_Insurance(Monthly_Income):
    Tax = 0
    if Monthly_Income < 700:
        return Tax
    elif Monthly_Income >= 700 and Monthly_Income < 4000:
        Tax = (Monthly_Income-700) *  0.12
        return Tax
    else: 
        Tax = (Monthly_Income-4000)*0.02
        Tax = Tax + (3300 * 0.12)
        return Tax
    
def Progressive_Taxation(Income):
    Tax = 0
    if Income < 10000:
        return Tax 
    elif Income >= 10000 and Income < 50000:
        Tax = (Income-10000)*0.2
        return Tax 
    else:
        Tax = (Income-50000)*0.4
        Tax = Tax + (40000 *0.2)
        return Tax

def main(Income, Monthly_Income):
    Tax_1 = National_Insurance(Monthly_Income)
    Tax_2 = Progressive_Taxation(Income)
    return f"Total Tax: £{Tax_1+Tax_2}"
    

