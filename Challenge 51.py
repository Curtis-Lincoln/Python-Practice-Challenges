#Curtis Lincoln
#Challenge 51

def Pension_Contribution(Salary):
    Employee_Contribution = int(Salary)*0.075
    Employer_Contribution = int(Salary)*0.025
    Pension = Employee_Contribution + Employer_Contribution 
    return f"Pension: £{Pension}, Employee Contribution: £{Employee_Contribution}, Employer Contribution: £{Employer_Contribution}"
    
