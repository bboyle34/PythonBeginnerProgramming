#Client name: Professor Laura Atkins
#Programmer name: Brendna Boyle
#PA Purpose:
#My submission of this program indicates that I have neither received nor given substantial assistance in writing this program.

#Information given
employee = (input("Enter Employee's name:"))
hoursWorked = eval(input("Enter number of hours worked:"))
hourlyPay = eval(input("Enter hourly pay rate: $"))
marriage = (input("Specify whether you are married or single:"))
stateTax = eval(input("Enter the State tax rate where you reside:"))
grossPay = (hoursWorked * hourlyPay)


print("\n\nEmployee's name:", employee)
print("Number of hours worked:", hoursWorked)
print("Hourly Pay rate: $" + format(hourlyPay,".2f"))
print("Weekly income: $" + format(grossPay,".2f"))


#Assigning Variables
firstOne = marriage[0:1]
stateTax2 = (stateTax * grossPay)
if firstOne.upper() == "M":
    marriageTax = (.1)
if firstOne.upper() == "S":
    marriageTax = (.15)
fedTax = (marriageTax * grossPay)
totalDeductions = (fedTax + stateTax2)
finalPay = (grossPay - totalDeductions)

#Deductions
print("\nDeductions:")

print("\tFederal withholding is: $" + format(fedTax,".2f"))
print("\tState withholding is: $" + format(stateTax2,".2f"))
print("\tTotal deductions are: $" + format(totalDeductions,".2f"))
print("\n" + employee + '\'s', "final weekly paycheck is: $" + format(finalPay,".2f"))

#Access Code
access1 = employee[(len(employee)//3):8]
access2 = (employee.upper()[-3:])
access3 = min(employee) + max(employee)
accessCode = (access1 + access2 + access3)

#Print results
print("You're new access code is:", accessCode)







