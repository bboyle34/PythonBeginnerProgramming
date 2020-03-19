#Client name: Professor Laura Atkins
#Programmer name: Brendan Boyle
#PA Purpose: Given the information that this savings account has an annual interest rate, the program prompts the user to decide how much money per month and shows the month by month increasing balance of the savings account.
#My submission of this program indicates that I have neither received nor given substantial assistance in writing this program.

print("This savings account has an annual interest rate of 5%")
savings = eval(input("Enter the monthly saving amount:"))
oneMonth = (savings * (1 + .00417))
twoMonth = ((savings + oneMonth) * (1 + 0.00417))
threeMonth = ((savings + twoMonth) * (1 + 0.00417))
fourMonth = ((savings + threeMonth) * (1 + 0.00417))
fiveMonth = ((savings + fourMonth) * (1 + 0.00417))
sixMonth = ((savings + fiveMonth) * (1 + 0.00417))
oneMonthR = (round(oneMonth,2))
twoMonthR = (round(twoMonth,2))
threeMonthR = (round(threeMonth,2))
fourMonthR = (round(fourMonth,2))
fiveMonthR = (round(fiveMonth,2))
sixMonthR = (round(sixMonth,2))


print("Your balance after 1 month in the savings account is:$", oneMonthR)
print("Your balance after 2 months in the savings account is:$", twoMonthR)
print("Your balance after 3 months in the savings account is:$", threeMonthR)
print("Your balance after 4 months in the savings account is:$", fourMonthR)
print("Your balance after 5 months in the savings account is:$", fiveMonthR)
print("Your balance after 6 months in the savings account is:$", sixMonthR)
