#Curtis Lincoln
#Challenge 52
def Progressive_Taxation(Income):
    if Income < 10000:
        return Tax
    elif Income >= 10000 and Income < 50000:
        Tax = (Income-10000)*0.2
        return Tax
    else:
        Tax = (Income-50000)*0.4
        Tax = Tax + (40000 *0.2)
        return Tax

def National_Insurance(Monthly_Income):
    if Monthly_Income < 700:
        return Tax
    elif Monthly_Income >= 700 and Monthly_Income < 4000:
        Tax = (Monthly_Income-700) *  0.12
        return Tax
    else: 
        Tax = (Monthly_Income-4000)*0.02
        Tax = Tax + (3300 * 0.12)
        return Tax

def Pension_Contribution(Salary):
    Pension = int(Salary)*0.075
    return Pension

def Payslip(Monthly):
    Annual_Income = Monthly * 12
    Progessive = Progressive_Taxation(Annual_Income)
    National = National_Insurance(Monthly)
    Pension = Pension_Contribution(Annual_Income)
    Total_Pension = (Annual_Income*0.025)+ Pension
    Costs = Progessive + National + Pension
    print(f"Amount paid into pension: £{Total_Pension}")
    return f"Gross Pay: £{Annual_Income}, Net Pay: £{Annual_Income-Costs}"
    
