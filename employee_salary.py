# A code to calculate the salary of an employee given his basic pay.

# Taking input from the user
basic_pay = int(input("Enter basic pay: "))

# Calculations
HRA = 0.1*basic_pay # House Rent Allowance
print("HRA = ",HRA)
TA = 0.05*basic_pay # Tax Allowance
print("TA = ",TA)
Gross_Salary = basic_pay + HRA + TA
print("Gross Salary = ",Gross_Salary)
Tax = 0.02*Gross_Salary
print("Tax = ",Tax)
Net_Salary = Gross_Salary - Tax
print("Net Salary = ", Net_Salary)