#CIS 221 Programming Assignment: Decisions
#Brendan Boyle
#My submission of this program indicates that I have neither received nor given substantial assistance in writing this program.
#Question Comment: For me, going through the progrmaming without python and then with python to see what the code will program is the best learning tool for me in this class.

#-------------------------------------------------------------------------------
#Ask user for name of phone that begins with an alphabetic character and includes nothing else besides spaces and numbers.
import sys
newPhone = (input("What is the name of the new phone?           "))
if newPhone[0].isdigit():
    print("Please enter valid name.")
    sys.exit()
elif all(x.isalnum() or x.isspace() for x in newPhone):
    print("Name of the new phone is:                   ", newPhone)
else:
    print("Please enter valid name.")
    sys.exit()
print()


#-------------------------------------------------------------------------------
#Ask user for sales price; number must be an integer and be at least 100
salesPrice = input("What is the sales price of the new phone?    ")
if salesPrice.isalpha():
    print("Price must be numeric.")
    sys.exit()
salesPrice = float(salesPrice)
if float(salesPrice) < 100:
    print("Price must be at least $100.")
    sys.exit()
else:
    print("Sales price is:                            $", format(salesPrice,".2f"))
print()


#-------------------------------------------------------------------------------        
#Ask user which chipset the phone uses, S or K
chipset = str(input("Which chipset - Snapdragon 810 or Kirin 940? "))
if chipset[0].upper() == "S":
    print("The chipset is:                              Snapdragon 810")
elif chipset[0].upper() == "K":
    print("The chipset is:                              Kirin 940")
    chipset = str(input("Do you qualify for the Kirin 940 discount?   "))
    if chipset[0].upper() == "Y":
        print("You qualify for the discount!")
    elif chipset[0].upper() == "N":
        print("You do not qualify for the discount!")
    else:
        print("Please enter \'Y\' or \'N\' to answer the question")
        sys.exit()
                  
else:
    print("Please enter either a \'K\' or a \'S\' for Kirin or Snapdragon.")
    sys.exit()
print()
print()


#-------------------------------------------------------------------------------
#Calculate chipset cost, memory cost, other expenses, total cost, and net profit
print("The name of the phone is ", newPhone.upper())
print(" ")
print("Price of phone    $" + format(float(salesPrice),".2f").rjust(9))
print("The costs are:")

#Chipset
if chipset[0].upper() == "S":
    chipsetPrice = (float(salesPrice) * .6)
elif chipset[0].upper() == "Y":
    chipsetPrice = (float(salesPrice) * .4)
elif chipset[0].upper() == "N":
    chipsetPrice = (float(salesPrice) * .5)
print("\tChipset   $" + format(chipsetPrice,".2f").rjust(9))

#Memory
if float(salesPrice) < 300:
    memoryCost = 80
elif float(salesPrice) < 500:
    memoryCost = 90
else:
    memoryCost = 100
print("\tMemory    $" + format(memoryCost,".2f").rjust(9))

#Other expenses
cameraCost = float(salesPrice)*.05
batteryCost = float(salesPrice)//22
displayCost = ord(newPhone[0])
totalCost = (chipsetPrice + memoryCost + cameraCost + batteryCost + displayCost)
netProfit = (float(salesPrice) - totalCost)
print("\tCamera    $" + format(cameraCost,".2f").rjust(9))
print("\tBattery   $" + format(batteryCost,".2f").rjust(9))
print("\tDisplay   $" + format(displayCost,".2f").rjust(9))

#Total Cost
print("  Total Cost      $" + format(totalCost,".2f").rjust(9))

#Net Profit
if netProfit < 0:
    print("Net Profit        $" + format(netProfit,".2f").rjust(9))
    print("WARNING: You will not make an profit at this price!")
    sys.exit()
else:
    print("Net Profit        $" + format(netProfit,".2f").rjust(9))
print()


#-------------------------------------------------------------------------------
#Ask user if they want to see profit in Euros, Rupees, and Yen

euros = input("Would you like to see profit in Euros (Y/N)? ")
if not (euros[0].upper() == "Y" or euros[0].upper() == "N"):
    print("Please enter \'Y\' or \'N\' to answer the questio.")
    sys.exit
rupees = input("Would you like to see profit in Ruppes (Y/N)? ")
if not (rupees[0].upper() == "Y" or rupees[0].upper() == "N"):
    print("Please enter \'Y\' or \'N\' to answer the question.")
    sys.exit
yen = input("Would you like to see profit in Yen (Y/N)? ")
if not (yen[0].upper() == "Y" or yen[0].upper() == "N"):
    print("Please enter \'Y\' or \'N\' to answer the question.")
    sys.exit


if euros[0].upper() == "Y":
    euros = (netProfit * .94)
    print("Profit of $", format(netProfit,".2f"), "is $", format(euros,".4f") + "\u20AC")
if rupees[0].upper() == "Y":
    rupees = (netProfit * 67.06)
    print("Profit of $", format(netProfit,".2f"), "is $", format(rupees,".4f") + "\u00A5")
if yen[0].upper() == "Y":
    yen = (netProfit * 112.82)
    print("Profit of $", format(netProfit,".2f"), "is $", format(yen,".4f") + "\u20B9")






    

    


