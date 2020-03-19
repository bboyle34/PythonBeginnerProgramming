
#Define the main function
def main():
    menu()

#Define the choices function
def choices():
    
    choice = input("Please enter your choice: ").lower()
    list1 = ['p', 'r', 'd', 'h', 'l', 'q']
    
    if choice not in list1:
        print("Invalid list. Please try again.")
        menu()
    elif choice == "r":
        filename()
    elif choice == "p":
        payroll()
    elif choice == "d":
        display()
    elif choice == "h":
        highestPaid()
    elif choice == "l":
        lowestPaid()
    else:
        quit1()

#Original lists
names = []
wages = []
hoursWorked = []

#Define the file function
def filename():
    try:

        global names
        global wages
        global hoursWorked
    
        fileName = input("Enter the file name: ").strip()
        file1 = open (fileName, 'r')
        file2 = file1.readlines()
        file2.sort()
    
        hours = []
        #separate data into 3 lists of names, wages, and hours worked
        for objects in file2:
            names.append(objects.split('\t')[0])
            wages.append(objects.split('\t')[1])
        for line in file2:
            hours.append(line.replace("\n", "").split("\t")[2:])
    
        for x in range(len(names)):
            appendtotal = 0
            for y in range(len(hours[0])):
                appendtotal += eval(hours[x][y])
            hoursWorked.append(appendtotal)
        #confirm file has been read
        print("File has been read")

    
    #print outcomes for errors
    except IOError:
        print("Error reading file " + fileName)
    except:
        print("Bad data in file")

    print("\n\n")
    
    menu()

#Define payroll function
def payroll():
    #set up format for payroll
    print("Name\t Hours\t Pay")
    print('----\t -----\t ---')
    
    #format so dollar sign is included, comma when over one thousand, and 2 decimal places
    fmt = '${:,.2f}'
    
    total_employee_payroll = 0
    for i in range(len(names)):
        total_pay_per_employee = (eval(wages[i]) * hoursWorked[i])
        print(names[i],'\t', hoursWorked[i], '\t' , fmt.format(total_pay_per_employee))
        total_employee_payroll += float(total_pay_per_employee)
    print("Total payroll =\t", fmt.format(total_employee_payroll))
    print("\n\n")

    choices()

#Define display function
def display():
    employeeName = input("Enter the employee's name: ").capitalize()
    
    #conduct a linear search of the names
    def linearSearch(names, employeeName):
        for i in range(len(names)):
            if employeeName == names[i]:
                return i
        return -1

    i = linearSearch(names, employeeName)
    employeePay = (eval(wages[i]) * hoursWorked[i])

    if employeeName == names[i]:
        print(employeeName, "worked", hoursWorked[i], "hours at $", format(eval(wages[i]), '.2f'), "per hour, and earned $", format(employeePay, '.2f'))
    
    else:
        print("That employee's name is not in the file.")

    print("\n\n")

    choices()
    
#Define highest paid employee function
def highestPaid():
    
    fmt = '${:,.2f}'
    #add new variables so that global variables aren't changed
    global hoursWorked
    global wages
    hoursWorked1 = []
    wages1 = []
    hoursWorked1 = hoursWorked
    wages1 = wages
    #find max paid employee
    for i in range (len(hoursWorked)):
        hoursWorked1 = [float(i) for i in hoursWorked]
        wages1 = [float(i) for i in wages]
        pay = []
        pay = [a * b for a,b in zip(hoursWorked1, wages1)]
    print(names[pay.index(max(pay))], "earned $", fmt.format(max(pay)))

    print("\n\n")
    choices()

        
#Define lowest paid employee function
def lowestPaid():
        
    fmt = '${:,.2f}'
    #add new variables so that global variables aren't changed
    global hoursWorked
    global wages
    hoursWorked1 = []
    wages1 = []
    hoursWorked1 = hoursWorked
    wages1 = wages
    #find min paid employee
    for i in range (len(hoursWorked)):
        hoursWorked1 = [float(i) for i in hoursWorked]
        wages1 = [float(i) for i in wages]
        pay = []
        pay = [a * b for a,b in zip(hoursWorked1, wages1)]
    print(names[pay.index(min(pay))], "earned $", fmt.format(min(pay)))

    print("\n\n")
    choices()



#Define quit function
def quit1():
    import sys
    print("Goodbye")
    sys.exit()
    
        
#Define menu function
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

#Call the main function
main()
    
