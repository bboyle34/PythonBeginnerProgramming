#Program Name: PA 4
#Student: Brendan Boyle
##My submission of this program indicates that I have neither received nor given unauthorized assistance in writing this program
#Write a program that lets the user enter the loan amount and
#loan period in number of years and displays the monthly and
#total payments for each interest rate starting from 5% to 8%,
#with an increment of 1/8

import sys

#ask for Loan Amount
loanAmount = input("Enter Loan amount: $")
if loanAmount.isalpha():
    print("Please enter a number.")
    sys.exit()
elif int(loanAmount) < 10000:
    
    print("Please enter a number between 10000 and 100000.")
    sys.exit()
elif int(loanAmount) > 100000:
    print("Please enter a number between 10000 and 100000.")
    sys.exit()
else:
    print("Loan Amount is $", format(int(loanAmount),".2f"))
print()

#ask for Loan period
numYears = input("Enter number of years: ")
if numYears.isalpha():
    print("Please enter a number.")
    sys.exit()
elif int(numYears) < 3:
    print("Please enter a value between 3 and 7.")
    sys.exit()
elif int(numYears) > 7:
    print("Please enter a value between 3 and 7.")
    sys.exit()
else:
    print("Number of years is " + numYears)
print()

#ask for annual interest rate
annualInterestRate = input("Enter annual interst rate: ")
if annualInterestRate.isalpha():
    print("Please enter a number.")
    sys.exit()
else:
    print("Annual Interest Rate is " + annualInterestRate)
print()

#print information
print("Annual InterestRate", end = " ")
print("Monthly Payment".rjust(25), end = " ")
print("Total Cost".rjust(16))
print()

#format loan rate
interestRate = annualInterestRate
print(format(interestRate, ".3f") + "%", end = " ")

#convert variables to integers
annualInterestRate = int(annualInterestRate)
loanAmount = int(loanAmount)
numYears = int(numYears)

#find monthly interest
monthlyInterestRate = (annualInterestRate) / 1200

#find payments
monthlyPayment = loanAmount * monthlyInterestRate / (1 - 1 / (1 + monthlyInterestRate) ** (numYears * 12))
monthlyPayment = format(monthlyPayment,".2f")
print(monthlyPayment.rjust(25), end = " ")
monthlyPayment = float(monthlyPayment)

totalPayment = monthlyPayment * 23 + loanAmount
totalPayment = format(totalPayment, ".2f")
print(totalPayment.rjust(25))

for i in range (numYears - 1):
    interestRate = interestRate + (.125)
    print(format(interestRate, ".3f") + "%", end = " ")

    #final prints
    monthlyInterestRate = interestRate / 1200
    monthlyPayment = loanAmount * monthlyInterestRate / (1 - 1/ (1 + monthlyInterestRate) ** (numYears * 12))
    monthlyPayment = format(monthlyPayment, ".2f")
    monthlyPayment = str(monthlyPayment)
    print(monthlyPayment.rjust(25), end = " ")
    monthlyPayment = float(monthlyPayment)

    totalPayment = monthlyPayment * 12 + loanAmount
    totalPayment = format(totalPayment, ".2f")
    totalyPayment = str(totalPayment)
    print(totalPayment.rjust(25))









