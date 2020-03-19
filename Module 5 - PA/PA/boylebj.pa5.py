#CIS 221 Programming Assignment 11/16/17
#Brendan Boyle
#My submission of this program indicates that I have neither received nor given substantial assistance in writing this program.


#files must be read first
#prompt user to select read file first
def firstChoice():
    print("Menu of choices")
    print("\t(r)ead employee data")
    print("\t(p)rint employee payroll")
    print("\t(d)isplay an employee by name")
    print("\tfind (h)ighest paid employee")
    print("\tfind (l)owest paid employee")
    print("\t(q)uit")
    print('\n')
    choices = input("Please enter your choice: ")
    if choices == 'q':
        quit0()
    elif choices != 'r':
        print("The file must be read first, please select \'r\'.")
        firstChoice()
    else:
        readFile()
           
#Orignial Lists
employeeNames = []
employeeWages = []
employeeHoursWorked = []

#Main function
def main():
    firstChoice()

#Menu Function   
def menu():
    print("Menu of choices")
    print("\t(r)ead employee data")
    print("\t(p)rint employee payroll")
    print("\t(d)isplay an employee by name")
    print("\tfind (h)ighest paid employee")
    print("\tfind (l)owest paid employee")
    print("\t(q)uit")
    print('\n')
    choices()

#Choices Function    
def choices():
    choice = input("Please enter your choice: ")
    list1 = ['p', 'r', 'd', 'h', 'l', 'q']

    if choice not in list1:
        print("Invalid. Please enter another choice.")
        menu()
    elif choice.lower() == "r":
        readFile()
    elif choice.lower() == "p":
        empPayroll()
    elif choice.lower() == "d":
        displayEmp()
    elif choice.lower() == "h":
        highestPay()
    elif choice.lower() == "l":
        lowestPay()
    elif choice.lower() == "q":
        quit0()

#File Function
def readFile():
    
    global employeeNames
    global employeeWages
    global employwwHoursWorked

    #ask for file and open it 
    fileName = input("Enter the file name: ")
    if fileName == "empwages.txt":
        file1 = open(fileName, 'r')
        file2 = file1.readlines()

        number = []
        #entries in the first column of the file are names
        file2.sort()
        for columns in file2:
            employeeNames.append(columns.split("\t")[0])
        #entries in the second column of the file are wages
        for columns in file2:
            employeeWages.append(columns.split("\t")[1])
        #entries in the rest of the columns of the file are hours
        for columns in file2:
            number.append(columns.replace("\n", "").split("\t")[2:])
        for i in range(len(employeeNames)):
            readTotal = 0
            for j in range(len(number[0])):
                readTotal += eval(number[i][j])
            employeeHoursWorked.append(readTotal)
        print("File has been read")
        print()
        print()
    else:
        print("Can't find file", fileName)
        print()
        print()
    
    menu()

#Payroll Function
def empPayroll():
    print("Name \tHours \tPay")
    print()
    #have two variables, one for the total pay, and one for the individual pay
    totalPay = 0
    for i in range(len(employeeNames)):
        perPay = (eval(employeeWages[i]) * employeeHoursWorked[i])
        print(employeeNames[i], "\t", employeeHoursWorked[i], "\t", format(perPay, ".2f"))
        totalPay += perPay
    print()
    print("Total pay = $" + format(totalPay, ".2f"))
    print()
    print()
    menu()

#Display Function
def displayEmp():
    empName = input("Enter an Employee's name: ")
    empName = empName.title()
    #linear search for the name across the file
    def linearSearch(employeeNames, empName):
        for i in range(len(employeeNames)):
            if empName == employeeNames[i]:
                return i
        return -1
    #display employee and hours worked and payrate and total pay
    i = linearSearch(employeeNames,empName) 
    totalPay = (eval(employeeWages[i]) * employeeHoursWorked[i])

    if empName == employeeNames[i]:
        print(empName, "worked", employeeHoursWorked[i], "hours at $", employeeWages[i], "per hour and earned $", totalPay)
    else:
        print("Employee not found.")
    print()
    print()
    menu()
    

#Highest Paid Function
def highestPay():
    global employeeHoursWorked
    global employeeWages
    #add new variables so global variables don't change
    employeeHoursWorked0 = []
    employeeWages0 = []
    employeeHoursWorked0 = employeeHoursWorked
    employeeWages0 = employeeWages
    #find highest paid employee
    for i in range(len(employeeHoursWorked)):
        employeeHoursWorked0 = [float(i) for i in employeeHoursWorked]
        employeeWages0 = [float(i) for i in employeeWages]
        employeePay = []
        employeePay = [a * b for a,b in zip(employeeHoursWorked0, employeeWages0)]
    print(employeeNames[employeePay.index(max(employeePay))], "earned $", (max(employeePay)))
    print()
    print()
    menu()
    

#Lowest Paid Function
def lowestPay():
    #do the same thing as Highest Paid Function except find the min
    global employeeHoursWorked
    global employeeWages
    #add new variables so global variables don't change
    employeeHoursWorked0 = []
    employeeWages0 = []
    employeeHoursWorked0 = employeeHoursWorked
    employeeWages0 = employeeWages
    #find lowest paid employee
    for i in range(len(employeeHoursWorked)):
        employeeHoursWorked0 = [float(i) for i in employeeHoursWorked]
        employeeWages0 = [float(i) for i in employeeWages]
        employeePay = []
        employeePay = [a * b for a,b in zip(employeeHoursWorked0, employeeWages0)]
    print(employeeNames[employeePay.index(min(employeePay))], "earned $", (min(employeePay)))
    print()
    print()
    menu()

#Quit Function
def quit0():
    import sys
    print("Program Closing.")
    sys.exit()

#Call back to main function
main()
    
